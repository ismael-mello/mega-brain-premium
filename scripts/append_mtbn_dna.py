#!/usr/bin/env python3
"""
Append MTBN elements to DK DNA.yaml
Phase 8.1 — Dan Kennedy MTBN DNA Integration
"""
import pathlib
import re
import sys

BASE = pathlib.Path("C:/Users/ISMAEL_MELLO/Downloads/mega-brain-premium")
DNA_FILE = BASE / "knowledge/external/dna/persons/dan-kennedy/DNA.yaml"
MTBN_DIR = BASE / "knowledge/external/sources/dan-kennedy/mtbn-extraction"

BATCH_FILES = [
    "BATCH-MTBN-01-OTM-AUDIO.yaml",
    "BATCH-MTBN-03-OTM-PDFS.yaml",
    "BATCH-MTBN-04-SECRETS-AUDIO.yaml",
    "BATCH-MTBN-05-SECRETS-PDFS.yaml",
    "BATCH-MTBN-06-SORCERY.yaml",
    "BATCH-MTBN-07-SYSTEM-PDFS.yaml",
    "BATCH-MTBN-08-MARKETING-AFFLUENT.yaml",
    "BATCH-MTBN-09-TIME-MANAGEMENT.yaml",
    "BATCH-MTBN-10-SALES-ASSETS.yaml",
    "BATCH-MTBN-11-SALES-OPERATIONS.yaml",
    "BATCH-MTBN-13-MAGNETIC-MARKETING-2014.yaml",
    "BATCH-MTBN-14-MORE-BONUSES.yaml",
]

# Layer section names in extraction files -> DNA.yaml Portuguese names
LAYER_MAP = {
    "L1_PHILOSOPHIES": "L1_FILOSOFIAS_MTBN",
    "L1_FILOSOFIAS": "L1_FILOSOFIAS_MTBN",
    "L2_MENTAL_MODELS": "L2_MODELOS_MENTAIS_MTBN",
    "L2_MENTAL_MODELS:": "L2_MODELOS_MENTAIS_MTBN",
    "L3_HEURISTICS": "L3_HEURISTICAS_MTBN",
    "L4_FRAMEWORKS": "L4_FRAMEWORKS_MTBN",
    "L5_METHODOLOGIES": "L5_METODOLOGIAS_MTBN",
}

def extract_layer_blocks(content):
    """Extract elements from each layer in an extraction file."""
    layers = {
        "L1": [],
        "L2": [],
        "L3": [],
        "L4": [],
        "L5": [],
    }

    lines = content.split("\n")
    current_layer = None
    in_elements = False
    element_lines = []
    collecting = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Detect layer section headers
        if re.match(r'^(L1_|layers:\s*$)', line) and 'L1_' in line:
            if 'L1_PHIL' in line or 'L1_FILO' in line:
                current_layer = "L1"
                collecting = True
                i += 1
                continue
        elif re.match(r'^(L2_)', line):
            if 'L2_MENTAL' in line or 'L2_MODAL' in line or 'L2_MODEL' in line:
                current_layer = "L2"
                collecting = True
                i += 1
                continue
        elif re.match(r'^(L3_)', line):
            if 'L3_HEUR' in line:
                current_layer = "L3"
                collecting = True
                i += 1
                continue
        elif re.match(r'^(L4_)', line):
            if 'L4_FRAME' in line:
                current_layer = "L4"
                collecting = True
                i += 1
                continue
        elif re.match(r'^(L5_)', line):
            if 'L5_METH' in line or 'L5_METOD' in line:
                current_layer = "L5"
                collecting = True
                i += 1
                continue

        # Stop collecting at summary/batch_info/next_ids sections
        if collecting and re.match(r'^(summary|batch_info|next_ids|notes|cross_references|batch_id|source|files|element|running|layers:$)', stripped.split(':')[0] if ':' in stripped else stripped):
            if current_layer and element_lines:
                layers[current_layer].extend(element_lines)
                element_lines = []
            collecting = False
            current_layer = None

        # In nested layers: block (like in BATCH-06/07)
        if re.match(r'^\s{4}L[1-5]_', line):
            layer_match = re.match(r'\s+L(\d)_', line)
            if layer_match:
                ln = layer_match.group(1)
                if element_lines and current_layer:
                    layers[current_layer].extend(element_lines)
                    element_lines = []
                current_layer = f"L{ln}"
                collecting = True
                i += 1
                continue

        if collecting and current_layer:
            element_lines.append(line)

        i += 1

    if current_layer and element_lines:
        layers[current_layer].extend(element_lines)

    return layers


def clean_layer_block(lines):
    """Remove empty lines at start/end, keep content."""
    # Strip trailing empty lines
    while lines and not lines[-1].strip():
        lines.pop()
    while lines and not lines[0].strip():
        lines.pop(0)
    return lines


def build_dna_block_for_layer(layer_key, elements_lines, batch_source="MTBN"):
    """Build a YAML block for a layer section."""
    # Map layer key to Portuguese DNA name
    name_map = {
        "L1": "L1_FILOSOFIAS_MTBN",
        "L2": "L2_MODELOS_MENTAIS_MTBN",
        "L3": "L3_HEURISTICAS_MTBN",
        "L4": "L4_FRAMEWORKS_MTBN",
        "L5": "L5_METODOLOGIAS_MTBN",
    }
    section_name = name_map[layer_key]
    lines = [f"\n{section_name}:"]
    lines.extend(elements_lines)
    return "\n".join(lines)


def count_ids_in_layer(lines, prefix):
    """Count how many IDs matching prefix exist in lines."""
    count = 0
    for line in lines:
        if f'id: {prefix}' in line or f"id: \"{prefix}" in line or f"id: '{prefix}" in line:
            count += 1
    return count


def process_batch_06_07_nested(content, batch_name):
    """Special handler for BATCH-06 and 07 which use nested layers: structure."""
    layers = {"L1": [], "L2": [], "L3": [], "L4": [], "L5": []}

    lines = content.split("\n")
    current_layer = None
    collecting = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Match nested layer headers like "    L1_PHILOSOPHIES:" or "  L1_PHILOSOPHIES:"
        nested_match = re.match(r'^\s+(L(\d)_[A-Z_]+):', line)
        top_match = re.match(r'^(L(\d)_[A-Z_]+):', line)

        if nested_match or top_match:
            match = nested_match or top_match
            ln = match.group(2)
            current_layer = f"L{ln}"
            collecting = True
            i += 1
            continue

        # Stop at summary/batch sections
        stripped = line.strip()
        if re.match(r'^(summary:|next_ids:|notes:|cross_references:|batch_info:)', stripped):
            collecting = False
            current_layer = None

        if collecting and current_layer and stripped:
            layers[current_layer].append(line)

        i += 1

    return layers


def main():
    print("=" * 60)
    print("DK MTBN DNA Append Script — Phase 8.1")
    print("=" * 60)

    # Read current DNA
    dna_content = DNA_FILE.read_text(encoding="utf-8")
    original_lines = dna_content.count("\n")
    print(f"DNA.yaml: {len(dna_content):,} bytes, ~{original_lines:,} lines")

    # Collect all elements per layer across all batches
    all_layers = {"L1": [], "L2": [], "L3": [], "L4": [], "L5": []}
    total_elements = 0

    for batch_file in BATCH_FILES:
        batch_path = MTBN_DIR / batch_file
        if not batch_path.exists():
            print(f"  WARNING: {batch_file} not found, skipping")
            continue

        batch_content = batch_path.read_text(encoding="utf-8")
        print(f"\nProcessing: {batch_file}")

        # Check if this is a nested structure (06/07 style)
        if "layers:" in batch_content and re.search(r'^\s{2,}L[1-5]_', batch_content, re.MULTILINE):
            layers = process_batch_06_07_nested(batch_content, batch_file)
        else:
            layers = extract_layer_blocks(batch_content)

        for ln in ["L1", "L2", "L3", "L4", "L5"]:
            block = clean_layer_block(layers[ln])
            if block:
                count = count_ids_in_layer(block, "FIL-DK-" if ln == "L1" else
                                           "MM-DK-" if ln == "L2" else
                                           "HEUR-DK-" if ln == "L3" else
                                           "FW-DK-" if ln == "L4" else "MET-DK-")
                print(f"  {ln}: {count} elements")
                total_elements += count
                all_layers[ln].extend(block)
                all_layers[ln].append("")  # blank line between batches

    print(f"\nTotal elements collected: {total_elements}")

    # Build the MTBN appendix block
    layer_names = {
        "L1": "L1_FILOSOFIAS_MTBN",
        "L2": "L2_MODELOS_MENTAIS_MTBN",
        "L3": "L3_HEURISTICAS_MTBN",
        "L4": "L4_FRAMEWORKS_MTBN",
        "L5": "L5_METODOLOGIAS_MTBN",
    }

    append_block = "\n\n# ═══════════════════════════════════════════════════════════════\n"
    append_block += "# MAKE THEM BUY NOW (MTBN) — 279 elementos\n"
    append_block += "# Batches: 01, 03-11, 13, 14 | Extracted: 2026-03-15\n"
    append_block += "# ═══════════════════════════════════════════════════════════════\n"

    for ln in ["L1", "L2", "L3", "L4", "L5"]:
        section_name = layer_names[ln]
        block_lines = all_layers[ln]
        if block_lines:
            append_block += f"\n{section_name}:\n"
            append_block += "\n".join(block_lines)
            append_block += "\n"

    # Write updated DNA
    new_content = dna_content.rstrip() + append_block

    # Backup first
    backup_path = DNA_FILE.parent / "DNA.yaml.bak"
    backup_path.write_text(dna_content, encoding="utf-8")
    print(f"\nBackup saved: {backup_path}")

    DNA_FILE.write_text(new_content, encoding="utf-8")
    new_size = len(new_content)
    print(f"DNA.yaml updated: {new_size:,} bytes (+{new_size - len(dna_content):,} bytes)")
    print(f"Total elements appended: {total_elements}")

    # Verify IDs
    print("\nVerifying IDs in updated DNA...")
    for prefix, label in [("FIL-DK-", "L1"), ("MM-DK-", "L2"), ("HEUR-DK-", "L3"),
                           ("FW-DK-", "L4"), ("MET-DK-", "L5")]:
        matches = re.findall(rf'{prefix}(\d+)', new_content)
        if matches:
            nums = [int(x) for x in matches]
            print(f"  {label} ({prefix}): max={max(nums)}, count={len(nums)}")

    return total_elements


if __name__ == "__main__":
    total = main()
    print(f"\nDone. {total} MTBN elements appended to DNA.yaml.")
