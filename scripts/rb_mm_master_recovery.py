#!/usr/bin/env python3
"""
RB-MM Master Recovery Script
Inserts 177 elements from MM-04 + MM-05 + MM-06 into DNA.yaml

MM-04 (ES LIVE): 73 elements (PHI:11 MM:13 HEUR:26 FW:13 MET:10)
MM-05 (TS LIVE): 53 elements (PHI:12 MM:12 HEUR:15 FW:9 MET:5)
MM-06 (Greatest Hits): 51 elements (PHI:10 MM:10 HEUR:19 FW:8 MET:4)

Strategy: Extract YAML blocks from existing scripts, fix MM-06 formatting,
insert before each layer's next-section separator in DNA.yaml.
"""
import re
import pathlib
import sys
import shutil
from datetime import datetime

DNA_PATH = pathlib.Path("knowledge/external/dna/persons/russell-brunson/DNA.yaml")
SCRIPTS = pathlib.Path("scripts")


def extract_string_vars(filepath):
    """Extract triple-quoted string variables from a Python script."""
    content = filepath.read_text(encoding='utf-8')
    result = {}

    # Match VARNAME = """...""" (non-raw)
    for m in re.finditer(r'(\w+)\s*=\s*"""(.*?)"""', content, re.DOTALL):
        result[m.group(1)] = m.group(2)

    # Match VARNAME = r'''...''' (raw)
    for m in re.finditer(r"(\w+)\s*=\s*r'''(.*?)'''", content, re.DOTALL):
        result[m.group(1)] = m.group(2)

    return result


def fix_mm06_block(block):
    """Fix MM-06 formatting: 4->6 space indent for items, quote IDs."""
    lines = block.split('\n')
    fixed = []
    for line in lines:
        if line.strip():
            line = '  ' + line
        # Quote unquoted IDs: - id: PHI-RB-176 -> - id: "PHI-RB-176"
        line = re.sub(
            r'(- id: )((?:PHI|MM|HEUR|FW|MET)-RB-\d+)',
            r'\1"\2"',
            line
        )
        fixed.append(line)
    return '\n'.join(fixed)


def main():
    if not DNA_PATH.exists():
        print(f"ERROR: DNA file not found: {DNA_PATH}")
        sys.exit(1)

    # Backup
    backup = DNA_PATH.with_suffix('.yaml.bak')
    shutil.copy2(DNA_PATH, backup)
    print(f"Backup: {backup}")

    # Read DNA
    dna = DNA_PATH.read_text(encoding='utf-8')
    original_size = len(dna)

    # Count original elements
    orig_ids = dna.count('- id: "')
    print(f"Original: {orig_ids} quoted id entries, {original_size} bytes")

    # ── Extract blocks from scripts ──
    print("\nExtracting from scripts...")

    mm04 = extract_string_vars(SCRIPTS / "rb_mm04_eslive_insert.py")
    print(f"  MM-04: {len(mm04)} variables found: {list(mm04.keys())}")

    mm05 = extract_string_vars(SCRIPTS / "rb_mm05_tslive_insert.py")
    print(f"  MM-05: {len(mm05)} variables found: {list(mm05.keys())}")

    mm06_raw = extract_string_vars(SCRIPTS / "rb_mm06_greatest_hits_insert.py")
    print(f"  MM-06: {len(mm06_raw)} variables found: {list(mm06_raw.keys())}")

    # Fix MM-06 formatting (indent + quote IDs)
    mm06 = {k: fix_mm06_block(v) for k, v in mm06_raw.items()}

    # ── Define layer mappings ──
    # For each layer: which variables from each batch, and where to insert
    # Insert BEFORE the separator of the NEXT section
    layer_config = [
        {
            'name': 'L1_PHILOSOPHIES',
            'blocks': [
                mm04.get('L1_BLOCK', ''),
                mm05.get('NEW_L1', ''),
                mm06.get('PHILOSOPHIES', ''),
            ],
            'separator_text': '  # L2: MENTAL MODELS',
        },
        {
            'name': 'L2_MENTAL_MODELS',
            'blocks': [
                mm04.get('L2_BLOCK', ''),
                mm05.get('NEW_L2', ''),
                mm06.get('MENTAL_MODELS', ''),
            ],
            'separator_text': '  # L3: HEURISTICS',
        },
        {
            'name': 'L3_HEURISTICS',
            'blocks': [
                mm04.get('L3_BLOCK', ''),
                mm05.get('NEW_L3', ''),
                mm06.get('HEURISTICS', ''),
            ],
            'separator_text': '  # L4: FRAMEWORKS',
        },
        {
            'name': 'L4_FRAMEWORKS',
            'blocks': [
                mm04.get('L4_BLOCK', ''),
                mm05.get('NEW_L4', ''),
                mm06.get('FRAMEWORKS', ''),
            ],
            'separator_text': '  # L5: METHODOLOGIES',
        },
        {
            'name': 'L5_METHODOLOGIES',
            'blocks': [
                mm04.get('L5_BLOCK', ''),
                mm05.get('NEW_L5', ''),
                mm06.get('METHODOLOGIES', ''),
            ],
            'separator_text': '  # L1: PHILOSOPHIES - OMG ADDITIONS',
        },
    ]

    # ── Insert in REVERSE order to preserve positions ──
    print("\nInserting elements...")
    for layer in reversed(layer_config):
        sep_text = layer['separator_text']

        # Find the separator line in DNA
        sep_idx = dna.find(sep_text)
        if sep_idx < 0:
            print(f"  ERROR: separator not found: {sep_text}")
            sys.exit(1)

        # Find the ========== line BEFORE the separator text
        block_start = dna.rfind('  # ==========', 0, sep_idx)
        if block_start < 0:
            print(f"  ERROR: ====== line not found before {sep_text}")
            sys.exit(1)

        # Combine all blocks for this layer
        combined_parts = []
        for b in layer['blocks']:
            # Only strip leading/trailing newlines, NOT spaces (preserve indentation)
            stripped = b.strip('\n\r')
            if stripped.strip():
                combined_parts.append(stripped)

        if not combined_parts:
            print(f"  {layer['name']}: no elements to insert, skipping")
            continue

        combined = '\n\n'.join(combined_parts) + '\n\n'

        # Insert before the separator block
        dna = dna[:block_start] + combined + dna[block_start:]

        # Count inserted ids
        inserted_count = sum(
            b.count('- id:') for b in layer['blocks']
        )
        print(f"  {layer['name']}: {inserted_count} elements inserted before '{sep_text}'")

    # ── Update metadata counts ──
    print("\nUpdating metadata...")

    # Old counts (verified from file): PHI:157 MM:137 HEUR:230 FW:157 MET:88 total:775
    # Added: PHI:33 MM:35 HEUR:60 FW:30 MET:19 = 177
    # New: PHI:190 MM:172 HEUR:290 FW:187 MET:107 total:952
    metadata_updates = {
        '  total_unique_elements: 775': '  total_unique_elements: 952',
        '    philosophies: 157': '    philosophies: 190',
        '    mental_models: 137': '    mental_models: 172',
        '    heuristics: 230': '    heuristics: 290',
        '    frameworks: 157': '    frameworks: 187',
        '    methodologies: 88': '    methodologies: 107',
    }

    for old, new in metadata_updates.items():
        count = dna.count(old)
        if count == 0:
            print(f"  WARNING: not found: {old}")
        elif count > 1:
            # Replace only the LAST occurrence (the by_layer totals at end of file)
            idx = dna.rfind(old)
            dna = dna[:idx] + new + dna[idx + len(old):]
            print(f"  Updated (last occurrence): {old.strip()} -> {new.strip()}")
        else:
            dna = dna.replace(old, new)
            print(f"  Updated: {old.strip()} -> {new.strip()}")

    # Add source metadata block before total_unique_elements
    mm_source_metadata = """  # EXPERT SECRETS LIVE WORKSHOP (merged via RB-MM-04 recovery)
  eslive_source_files: 12
  eslive_elements_appended: 73
  eslive_by_layer:
    philosophies: 11
    mental_models: 13
    heuristics: 26
    frameworks: 13
    methodologies: 10
  eslive_era: "~2017 (Expert Secrets book launch era, Magnetic Marketing bonus 3-day workshop)"
  eslive_note: "12 video sessions across 3 days. Mass Movement, Prolific Index, Perfect Webinar mechanics, Dream 100 implementation, PW as email/launch mapping."
  # TRAFFIC SECRETS LIVE WORKSHOP (merged via RB-MM-05 recovery)
  tslive_source_files: 9
  tslive_elements_appended: 53
  tslive_by_layer:
    philosophies: 12
    mental_models: 12
    heuristics: 15
    frameworks: 9
    methodologies: 5
  tslive_era: "~2018-2019 (Traffic Secrets book pre-write, Two Comma Club X bonus)"
  tslive_note: "9 video sessions. Dream Customer Avatar, Search vs Interruption, 3 Traffic Types, RFM+S, Your Show, HSO at every funnel level."
  # GREATEST HITS NEWSLETTER (merged via RB-MM-06 recovery)
  gh_source_files: 4
  gh_elements_appended: 51
  gh_by_layer:
    philosophies: 10
    mental_models: 10
    heuristics: 19
    frameworks: 8
    methodologies: 4
  gh_era: "Jan-Apr 2022 (Magnetic Marketing Behind The Scenes newsletter)"
  gh_note: "4 monthly issues. Ecomm offer stacking, invisible virtual events, evergreen webinar funnel, pre-funnels, radical imbalance, 4 levels of value."
"""

    target = '  total_unique_elements: 952'
    if target in dna:
        dna = dna.replace(target, mm_source_metadata + target, 1)
        print("  Source metadata blocks added")
    else:
        print("  WARNING: could not add source metadata")

    # ── Write ──
    DNA_PATH.write_text(dna, encoding='utf-8')
    new_size = len(dna)
    print(f"\nWritten: {new_size} bytes (was {original_size})")

    # ── Validate YAML ──
    print("\nValidating YAML...")
    try:
        import yaml
        data = yaml.safe_load(DNA_PATH.read_text(encoding='utf-8'))
        if data:
            print("YAML VALIDATION: PASSED")
        else:
            print("YAML VALIDATION: PASSED (empty doc)")
    except Exception as e:
        print(f"YAML VALIDATION: FAILED - {e}")
        print("Restoring backup...")
        shutil.copy2(backup, DNA_PATH)
        print("Backup restored. Fix the issue and retry.")
        sys.exit(1)

    # ── Count final elements ──
    final = DNA_PATH.read_text(encoding='utf-8')
    counts = {
        'PHI': final.count('- id: "PHI-RB-'),
        'MM': final.count('- id: "MM-RB-'),
        'HEUR': final.count('- id: "HEUR-RB-'),
        'FW': final.count('- id: "FW-RB-'),
        'MET': final.count('- id: "MET-RB-'),
    }
    # Also count unquoted (shouldn't exist after fix, but check)
    unquoted = {
        'PHI': final.count('- id: PHI-RB-'),
        'MM': final.count('- id: MM-RB-'),
        'HEUR': final.count('- id: HEUR-RB-'),
        'FW': final.count('- id: FW-RB-'),
        'MET': final.count('- id: MET-RB-'),
    }
    total_quoted = sum(counts.values())
    total_unquoted = sum(unquoted.values())

    print(f"\n{'='*60}")
    print(f"  RB-MM MASTER RECOVERY COMPLETE")
    print(f"{'='*60}")
    print(f"  PHI: {counts['PHI']} | MM: {counts['MM']} | HEUR: {counts['HEUR']} | FW: {counts['FW']} | MET: {counts['MET']}")
    print(f"  Total quoted IDs: {total_quoted}")
    if total_unquoted > 0:
        print(f"  WARNING: {total_unquoted} unquoted IDs found!")
    print(f"  Expected: 775 + 177 = 952 (main layers)")
    print(f"  Backup at: {backup}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
