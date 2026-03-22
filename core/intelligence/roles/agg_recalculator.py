#!/usr/bin/env python3
"""
AGG RECALCULATOR v1.0
======================
Recalculates total_elementos for all AGG-*.yaml files by:
1. Summing elementos_contribuidos from each fonte entry
2. If fonte lacks elementos_contribuidos, estimates from the person's DNA.yaml
3. Updates the total_elementos field in the AGG header

Version: 1.0.0
Date: 2026-03-22
"""

import re
import sys
from datetime import UTC, datetime
from pathlib import Path

import yaml

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

try:
    sys.path.insert(0, str(BASE_DIR))
    from core.paths import KNOWLEDGE_EXTERNAL
except ImportError:
    KNOWLEDGE_EXTERNAL = BASE_DIR / "knowledge" / "external"

AGG_DIR = KNOWLEDGE_EXTERNAL / "dna" / "aggregated"
DNA_PERSONS_DIR = KNOWLEDGE_EXTERNAL / "dna" / "persons"


def count_dna_elements(person_slug: str) -> int:
    """Count total elements in a person's DNA.yaml."""
    dna_path = DNA_PERSONS_DIR / person_slug / "DNA.yaml"
    if not dna_path.exists():
        return 0

    try:
        content = dna_path.read_text(encoding="utf-8")
        # Count lines that look like DNA entries (ID patterns like FIL-XX-NNN, MM-XX-NNN, etc.)
        pattern = r'^\s*-\s*"?(?:FIL|MM|HEUR|FW|MET|PHI)-[A-Z]{2,4}-\d+'
        matches = re.findall(pattern, content, re.MULTILINE)
        if matches:
            return len(matches)

        # Fallback: count all list items under layer keys
        data = yaml.safe_load(content)
        if not data:
            return 0

        total = 0
        layer_keys = ["L1_PHILOSOPHIES", "L2_MENTAL_MODELS", "L3_HEURISTICS",
                       "L4_FRAMEWORKS", "L5_METHODOLOGIES", "layers"]

        if "layers" in data and isinstance(data["layers"], dict):
            for layer_name, items in data["layers"].items():
                if isinstance(items, list):
                    total += len(items)
        else:
            for key in layer_keys:
                if key in data and isinstance(data[key], list):
                    total += len(data[key])

        return total
    except Exception:
        return 0


def recalculate_agg(agg_path: Path, dry_run: bool = False) -> dict:
    """Recalculate total_elementos for a single AGG file."""
    result = {
        "file": agg_path.name,
        "old_total": 0,
        "new_total": 0,
        "sources_updated": 0,
        "updated": False,
    }

    try:
        content = agg_path.read_text(encoding="utf-8")
        data = yaml.safe_load(content)
        if not data:
            return result

        result["old_total"] = data.get("total_elementos", 0)
        fontes = data.get("fontes_consolidadas", [])
        total = 0
        sources_fixed = 0

        for fonte in fontes:
            elem = fonte.get("elementos_contribuidos", 0) or fonte.get("elementos_relevantes", 0)
            if elem and elem > 0:
                total += elem
            else:
                # Estimate from person's DNA
                slug = fonte.get("fonte", "")
                if slug:
                    estimated = count_dna_elements(slug)
                    if estimated > 0:
                        fonte["elementos_contribuidos"] = estimated
                        total += estimated
                        sources_fixed += 1

        result["new_total"] = total
        result["sources_updated"] = sources_fixed

        if total != result["old_total"] or sources_fixed > 0:
            result["updated"] = True

            if not dry_run:
                # Update total_elementos in raw content (preserve comments/formatting)
                if "total_elementos:" in content:
                    content = re.sub(
                        r"total_elementos:\s*\d+",
                        f"total_elementos: {total}",
                        content,
                    )
                else:
                    # Add after ultima_atualizacao or atualizado_em (header area only)
                    if re.search(r"^ultima_atualizacao:", content, re.MULTILINE):
                        content = re.sub(
                            r"(^ultima_atualizacao:\s*\"[^\"]+\"[^\n]*\n)",
                            rf"\1total_elementos: {total}\n",
                            content,
                            count=1,
                            flags=re.MULTILINE,
                        )
                    elif re.search(r"^atualizado_em:", content, re.MULTILINE):
                        content = re.sub(
                            r"(^atualizado_em:\s*\"[^\"]+\"[^\n]*\n)",
                            rf"\1total_elementos: {total}\n",
                            content,
                            count=1,
                            flags=re.MULTILINE,
                        )
                    else:
                        # Fallback: add after first versao line at root level
                        content = re.sub(
                            r"(^versao:\s*\"[^\"]+\"[^\n]*\n)",
                            rf"\1total_elementos: {total}\n",
                            content,
                            count=1,
                            flags=re.MULTILINE,
                        )

                # Update elementos_contribuidos for sources that were estimated
                if sources_fixed > 0:
                    # Re-serialize the fontes section
                    # This is tricky with raw YAML, so we use a targeted approach
                    for fonte in fontes:
                        slug = fonte.get("fonte", "")
                        elem = fonte.get("elementos_contribuidos", 0)
                        if slug and elem > 0:
                            # Find the fonte block and add/update elementos_contribuidos
                            fonte_pattern = rf'(- fonte:\s*"{re.escape(slug)}"[^\n]*\n(?:    [^\n]+\n)*?)'
                            match = re.search(fonte_pattern, content)
                            if match:
                                block = match.group(1)
                                if "elementos_contribuidos:" in block:
                                    block = re.sub(
                                        r"elementos_contribuidos:\s*\d+",
                                        f"elementos_contribuidos: {elem}",
                                        block,
                                    )
                                else:
                                    # Add after peso_dominio or after path
                                    if "peso_dominio:" in block:
                                        block = re.sub(
                                            r"(peso_dominio:\s*[\d.]+[^\n]*\n)",
                                            rf"\1    elementos_contribuidos: {elem}\n",
                                            block,
                                        )
                                    else:
                                        block = re.sub(
                                            r'(path:\s*"[^"]*"[^\n]*\n)',
                                            rf"\1    elementos_contribuidos: {elem}\n",
                                            block,
                                        )
                                content = content[:match.start()] + block + content[match.end():]

                # Update timestamp
                today = datetime.now(UTC).strftime("%Y-%m-%d")
                content = re.sub(
                    r"ultima_atualizacao:\s*\"?\d{4}-\d{2}-\d{2}\"?",
                    f'ultima_atualizacao: "{today}"',
                    content,
                )

                agg_path.write_text(content, encoding="utf-8")

    except Exception as e:
        result["error"] = str(e)

    return result


def recalculate_all(dry_run: bool = False) -> list[dict]:
    """Recalculate all AGG files."""
    results = []
    for agg_file in sorted(AGG_DIR.glob("AGG-*.yaml")):
        result = recalculate_agg(agg_file, dry_run=dry_run)
        results.append(result)
    return results


def main() -> None:
    """CLI entry point."""
    dry_run = "--dry-run" in sys.argv

    print("=" * 60)
    print("AGG RECALCULATOR v1.0")
    print("=" * 60)

    if dry_run:
        print("[DRY RUN] No files will be modified.\n")

    results = recalculate_all(dry_run=dry_run)

    print(f"\n{'File':<35} {'Old':>6} {'New':>6} {'Fixed':>6} {'Status'}")
    print("-" * 75)

    for r in results:
        status = "UPDATED" if r["updated"] else "OK"
        err = r.get("error", "")
        if err:
            status = f"ERROR: {err[:30]}"
        print(f"{r['file']:<35} {r['old_total']:>6} {r['new_total']:>6} {r['sources_updated']:>6} {status}")

    updated = sum(1 for r in results if r["updated"])
    print(f"\n{updated}/{len(results)} AGGs updated.")
    print("Done.")


if __name__ == "__main__":
    main()
