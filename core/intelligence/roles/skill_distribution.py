#!/usr/bin/env python3
"""
SKILL DISTRIBUTION ENGINE v1.0
===============================
Maps extracted skills to the correct cargo agents and injects them
into MEMORY.md automatically.

Pipeline: SKILL.md files → Domain classification → Cargo routing → MEMORY.md injection

This closes the gap between skill_generator.py (extraction) and cargo agents (consumption).
Skills are classified by domain keywords and routed to the cargo agent(s) whose
DNA-CONFIG.yaml covers that domain.

Version: 1.0.0
Date: 2026-03-22
"""

import json
import re
import sys
from datetime import UTC, datetime
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# PATHS
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

try:
    sys.path.insert(0, str(BASE_DIR))
    from core.paths import AGENTS_CARGO, KNOWLEDGE_EXTERNAL, LOGS
except ImportError:
    AGENTS_CARGO = BASE_DIR / "agents" / "cargo"
    KNOWLEDGE_EXTERNAL = BASE_DIR / "knowledge" / "external"
    LOGS = BASE_DIR / "logs"

SKILLS_DIR = KNOWLEDGE_EXTERNAL / "dna" / "skills"
SKILLS_REGISTRY = KNOWLEDGE_EXTERNAL / "dna" / "_dna-skills-registry.yaml"
AGG_DIR = KNOWLEDGE_EXTERNAL / "dna" / "aggregated"
DISTRIBUTION_LOG = LOGS / "skill-distribution.jsonl"

# ---------------------------------------------------------------------------
# DOMAIN → CARGO ROUTING MAP
# ---------------------------------------------------------------------------
# Maps domain keywords to cargo agent paths (relative to AGENTS_CARGO).
# A skill can match multiple cargos. Order = priority.
DOMAIN_TO_CARGO: dict[str, list[str]] = {
    # Sales domains
    "vendas": ["c-level/cro", "sales/closer", "sales/sales-manager"],
    "sales": ["c-level/cro", "sales/closer", "sales/sales-manager"],
    "closing": ["sales/closer", "c-level/cro"],
    "fechamento": ["sales/closer", "c-level/cro"],
    "objection": ["sales/closer", "sales/sales-manager"],
    "prospecting": ["sales/sdr", "sales/sales-manager"],
    "outbound": ["sales/sdr", "c-level/cro"],
    "discovery": ["sales/closer", "sales/sdr"],
    "qualification": ["sales/sdr", "sales/closer"],
    "negotiation": ["sales/closer", "c-level/cro"],
    "pipeline": ["sales/sales-manager", "c-level/cro"],
    "hiring-sales": ["sales/sales-manager", "c-level/cro"],
    "compensation": ["sales/sales-manager", "c-level/cro", "c-level/cfo"],
    "script": ["sales/closer", "sales/sdr"],
    # Marketing domains
    "marketing": ["c-level/cmo", "marketing/copywriter"],
    "copywriting": ["marketing/copywriter", "c-level/cmo"],
    "copy": ["marketing/copywriter", "c-level/cmo"],
    "headlines": ["marketing/copywriter", "c-level/cmo"],
    "email": ["marketing/copywriter", "c-level/cmo"],
    "storytelling": ["marketing/copywriter", "c-level/cmo"],
    "brand": ["c-level/cmo"],
    "positioning": ["c-level/cmo", "c-level/cro"],
    "launch": ["c-level/cmo", "c-level/cro"],
    "webinar": ["c-level/cmo", "c-level/cro"],
    "funnel": ["c-level/cmo", "c-level/cro"],
    "content": ["c-level/cmo", "marketing/copywriter"],
    # Traffic domains
    "traffic": ["marketing/media-buyer", "c-level/cmo"],
    "paid-media": ["marketing/media-buyer", "c-level/cmo"],
    "facebook-ads": ["marketing/media-buyer", "c-level/cmo"],
    "google-ads": ["marketing/media-buyer", "c-level/cmo"],
    "youtube-ads": ["marketing/media-buyer", "c-level/cmo"],
    "retargeting": ["marketing/media-buyer", "c-level/cmo"],
    "creative": ["marketing/media-buyer", "c-level/cmo"],
    "scaling": ["marketing/media-buyer", "c-level/cmo", "c-level/cro"],
    # Finance domains
    "finance": ["c-level/cfo"],
    "pricing": ["c-level/cfo", "c-level/cro"],
    "unit-economics": ["c-level/cfo", "c-level/cro"],
    "ltv": ["c-level/cfo", "c-level/cro"],
    "cac": ["c-level/cfo", "c-level/cro", "c-level/cmo"],
    "margin": ["c-level/cfo"],
    "cash-flow": ["c-level/cfo"],
    "revenue": ["c-level/cro", "c-level/cfo"],
    # Operations domains
    "operations": ["operations/ops-manager", "c-level/coo"],
    "process": ["operations/ops-manager", "c-level/coo"],
    "systems": ["operations/ops-manager", "c-level/coo"],
    "automation": ["operations/ops-manager", "c-level/coo"],
    "delivery": ["operations/ops-manager", "c-level/coo"],
    "hiring": ["c-level/coo", "operations/ops-manager"],
    "team": ["c-level/coo", "operations/ops-manager"],
    "leadership": ["c-level/coo", "c-level/cro"],
    # Offers domains
    "offers": ["c-level/cro", "c-level/cmo"],
    "offer-creation": ["c-level/cro", "c-level/cmo"],
    "value-stack": ["c-level/cro", "c-level/cmo"],
    "guarantee": ["c-level/cro", "sales/closer"],
    "irresistible-offer": ["c-level/cro", "c-level/cmo"],
    # Movement / community
    "movement": ["c-level/cmo"],
    "community": ["c-level/cmo"],
    "influence": ["c-level/cmo", "sales/closer"],
    "persuasion": ["sales/closer", "marketing/copywriter", "c-level/cmo"],
}

# ---------------------------------------------------------------------------
# SKILL CLASSIFICATION
# ---------------------------------------------------------------------------


def classify_skill_domains(skill_path: Path) -> list[str]:
    """Read a SKILL.md file and extract domain keywords from its content."""
    if not skill_path.exists():
        return []

    text = skill_path.read_text(encoding="utf-8").lower()
    matched_domains: list[str] = []

    for domain_key in DOMAIN_TO_CARGO:
        # Check domain keyword in text (word boundary match)
        pattern = rf"\b{re.escape(domain_key)}\b"
        if re.search(pattern, text):
            matched_domains.append(domain_key)

    return matched_domains


def route_skill_to_cargos(domains: list[str]) -> dict[str, float]:
    """Given a list of matched domains, return cargo paths with relevance scores.

    Returns dict of {cargo_path: relevance_score} where score is 0.0-1.0.
    Higher score = more domains matched for that cargo.
    """
    cargo_scores: dict[str, float] = {}
    total_domains = max(len(domains), 1)

    for domain in domains:
        cargos = DOMAIN_TO_CARGO.get(domain, [])
        for i, cargo in enumerate(cargos):
            # First cargo in list gets higher weight (primary match)
            weight = 1.0 - (i * 0.2)
            weight = max(weight, 0.3)
            cargo_scores[cargo] = cargo_scores.get(cargo, 0) + weight

    # Normalize scores to 0.0-1.0
    if cargo_scores:
        max_score = max(cargo_scores.values())
        cargo_scores = {k: round(v / max_score, 2) for k, v in cargo_scores.items()}

    return cargo_scores


# ---------------------------------------------------------------------------
# MEMORY.MD INJECTION
# ---------------------------------------------------------------------------

SKILL_ENTRY_TEMPLATE = """| SK-{idx:03d} | {name} | {domains} | {source} | {confidence} |"""


def inject_skills_into_memory(
    cargo_path: Path,
    skills: list[dict],
    dry_run: bool = False,
) -> dict:
    """Inject skill entries into a cargo agent's MEMORY.md.

    Args:
        cargo_path: Absolute path to cargo agent directory
        skills: List of skill dicts with keys: name, domains, source, confidence
        dry_run: If True, don't write, just return what would be written

    Returns:
        dict with status, entries_added, cargo_path
    """
    memory_path = cargo_path / "MEMORY.md"
    if not memory_path.exists():
        return {"status": "skip", "reason": "MEMORY.md not found", "cargo": str(cargo_path)}

    content = memory_path.read_text(encoding="utf-8")

    # Check if skills section already exists
    skills_header = "## HABILIDADES DISTRIBUÍDAS"
    if skills_header not in content:
        # Add skills section before the last section or at the end
        table_header = f"""

---

{skills_header}

> Habilidades extraídas automaticamente pelo Skill Distribution Engine.
> Cada habilidade é rastreável à fonte original via skill_id.

| ID | Habilidade | Domínios | Fonte | Relevância |
|----|-----------|---------|-------|------------|
"""
        content += table_header

    # Add new skill entries
    existing_ids = set(re.findall(r"SK-(\d+)", content))
    next_idx = max((int(x) for x in existing_ids), default=0) + 1
    new_entries = []

    for skill in skills:
        entry = SKILL_ENTRY_TEMPLATE.format(
            idx=next_idx,
            name=skill["name"],
            domains=", ".join(skill["domains"][:3]),
            source=skill.get("source", "auto-extracted"),
            confidence=skill.get("confidence", "média"),
        )
        new_entries.append(entry)
        next_idx += 1

    if new_entries:
        # Find the last table row and append after it
        lines = content.split("\n")
        insert_idx = len(lines)
        for i in range(len(lines) - 1, -1, -1):
            if lines[i].strip().startswith("| SK-") or lines[i].strip().startswith("|----"):
                insert_idx = i + 1
                break

        for j, entry in enumerate(new_entries):
            lines.insert(insert_idx + j, entry)

        content = "\n".join(lines)

        # Update version if present
        version_match = re.search(r"\*\*Versão:\*\*\s*(\d+\.\d+\.\d+)", content)
        if version_match:
            old_v = version_match.group(1)
            parts = old_v.split(".")
            parts[1] = str(int(parts[1]) + 1)
            parts[2] = "0"
            new_v = ".".join(parts)
            content = content.replace(
                f"**Versão:** {old_v}",
                f"**Versão:** {new_v}",
            )

        # Update timestamp
        today = datetime.now(UTC).strftime("%Y-%m-%d")
        content = re.sub(
            r"\*\*Última atualização:\*\*\s*\d{4}-\d{2}-\d{2}",
            f"**Última atualização:** {today}",
            content,
        )

        if not dry_run:
            memory_path.write_text(content, encoding="utf-8")

    return {
        "status": "injected",
        "entries_added": len(new_entries),
        "cargo": str(cargo_path.relative_to(BASE_DIR)),
        "skills": [s["name"] for s in skills],
    }


# ---------------------------------------------------------------------------
# MAIN DISTRIBUTION PIPELINE
# ---------------------------------------------------------------------------


def distribute_all_skills(dry_run: bool = False) -> dict:
    """Main entry point: scan all SKILL.md files, classify, route, inject.

    Returns summary dict with distribution results.
    """
    results = {
        "timestamp": datetime.now(UTC).isoformat(),
        "skills_scanned": 0,
        "skills_classified": 0,
        "distributions": [],
        "cargo_summary": {},
        "unrouted_skills": [],
    }

    if not SKILLS_DIR.exists():
        results["error"] = f"Skills directory not found: {SKILLS_DIR}"
        return results

    # Collect all skill files
    skill_files = sorted(SKILLS_DIR.glob("*.md"))
    results["skills_scanned"] = len(skill_files)

    # Classify and route each skill
    cargo_skills: dict[str, list[dict]] = {}

    for sf in skill_files:
        if sf.name.startswith("_"):
            continue

        domains = classify_skill_domains(sf)
        if not domains:
            results["unrouted_skills"].append(sf.name)
            continue

        results["skills_classified"] += 1
        cargo_routes = route_skill_to_cargos(domains)

        skill_info = {
            "name": sf.stem.replace("-", " ").replace("_", " ").title(),
            "file": sf.name,
            "domains": domains,
            "source": sf.stem,
            "confidence": "alta" if len(domains) >= 3 else "média" if len(domains) >= 2 else "baixa",
        }

        # Route to cargos with relevance >= 0.4
        for cargo_path_str, relevance in cargo_routes.items():
            if relevance >= 0.4:
                cargo_full = AGENTS_CARGO / cargo_path_str
                if cargo_full.exists():
                    if cargo_path_str not in cargo_skills:
                        cargo_skills[cargo_path_str] = []
                    skill_entry = {**skill_info, "relevance": relevance}
                    cargo_skills[cargo_path_str].append(skill_entry)

    # Inject into each cargo MEMORY.md
    for cargo_rel, skills in cargo_skills.items():
        cargo_full = AGENTS_CARGO / cargo_rel
        injection_result = inject_skills_into_memory(cargo_full, skills, dry_run=dry_run)
        results["distributions"].append(injection_result)
        results["cargo_summary"][cargo_rel] = len(skills)

    # Log results
    if not dry_run:
        DISTRIBUTION_LOG.parent.mkdir(parents=True, exist_ok=True)
        with open(DISTRIBUTION_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(results, ensure_ascii=False) + "\n")

    return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    """CLI entry point."""
    dry_run = "--dry-run" in sys.argv
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    print("=" * 60)
    print("SKILL DISTRIBUTION ENGINE v1.0")
    print("=" * 60)

    if dry_run:
        print("[DRY RUN] No files will be modified.\n")

    results = distribute_all_skills(dry_run=dry_run)

    print(f"\nSkills scanned:    {results['skills_scanned']}")
    print(f"Skills classified: {results['skills_classified']}")
    print(f"Unrouted:          {len(results.get('unrouted_skills', []))}")
    print(f"\nDistributions:")

    for dist in results.get("distributions", []):
        status = dist.get("status", "unknown")
        cargo = dist.get("cargo", "?")
        count = dist.get("entries_added", 0)
        print(f"  {cargo}: +{count} skills ({status})")

    if verbose and results.get("unrouted_skills"):
        print(f"\nUnrouted skills:")
        for s in results["unrouted_skills"]:
            print(f"  - {s}")

    print(f"\nLog: {DISTRIBUTION_LOG}")
    print("Done.")


if __name__ == "__main__":
    main()
