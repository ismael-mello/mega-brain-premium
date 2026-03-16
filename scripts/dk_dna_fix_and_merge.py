#!/usr/bin/env python3
"""
DK DNA Fix & Merge Script
- Parses broken DNA.yaml (manual, line-by-line)
- Parses 8 MH wave files
- Deduplicates cross-wave and against existing
- Merges and writes clean DNA.yaml
"""
import re
import sys
import os
import hashlib

# Fix Windows encoding
os.environ.setdefault('PYTHONIOENCODING', 'utf-8')
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
from collections import defaultdict
from datetime import date

BASE = Path(__file__).resolve().parent.parent
DNA_PATH = BASE / "knowledge" / "external" / "dna" / "persons" / "dan-kennedy" / "DNA.yaml"
MH_DIR = BASE / "knowledge" / "external" / "sources" / "dan-kennedy" / "raw" / "mind-hijacking"
BACKUP_PATH = DNA_PATH.with_suffix(".yaml.bak")

# Layer mapping (normalize different naming conventions)
LAYER_MAP = {
    'L1': 'L1_PHILOSOPHIES',
    'L2': 'L2_MENTAL_MODELS',
    'L3': 'L3_HEURISTICS',
    'L4': 'L4_FRAMEWORKS',
    'L5': 'L5_METHODOLOGIES',
}

LAYER_ORDER = ['L1_PHILOSOPHIES', 'L2_MENTAL_MODELS', 'L3_HEURISTICS', 'L4_FRAMEWORKS', 'L5_METHODOLOGIES']

LAYER_KEY_PATTERNS = {
    'L1_PHILOSOPHIES': re.compile(r'L1_(?:FILOSOFIAS|PHILOSOPHIES)'),
    'L2_MENTAL_MODELS': re.compile(r'L2_(?:MODELOS_MENTAIS|MENTAL_MODELS)'),
    'L3_HEURISTICS': re.compile(r'L3_(?:HEURISTICAS|HEURISTICS)'),
    'L4_FRAMEWORKS': re.compile(r'L4_(?:FRAMEWORKS)'),
    'L5_METHODOLOGIES': re.compile(r'L5_(?:METODOLOGIAS|METHODOLOGIES)'),
}

ID_PREFIXES = {
    'L1_PHILOSOPHIES': 'FIL-DK-',
    'L2_MENTAL_MODELS': 'MM-DK-',
    'L3_HEURISTICS': 'HEUR-DK-',
    'L4_FRAMEWORKS': 'FW-DK-',
    'L5_METHODOLOGIES': 'MET-DK-',
}


def detect_layer_from_id(item_id: str) -> str:
    """Detect which layer an item belongs to based on its ID prefix."""
    if item_id.startswith('FIL-DK-'):
        return 'L1_PHILOSOPHIES'
    elif item_id.startswith('MM-DK-'):
        return 'L2_MENTAL_MODELS'
    elif item_id.startswith('HEUR-DK-'):
        return 'L3_HEURISTICS'
    elif item_id.startswith('FW-DK-'):
        return 'L4_FRAMEWORKS'
    elif item_id.startswith('MET-DK-'):
        return 'L5_METHODOLOGIES'
    return None


def normalize_item(item: dict) -> dict:
    """Normalize item to consistent format: id, title, content, source, context."""
    result = {}

    # ID - strip quotes
    raw_id = item.get('id', '')
    result['id'] = raw_id.strip('"').strip("'")

    # Title
    result['title'] = (
        item.get('title') or
        item.get('titulo') or
        item.get('name') or
        item.get('text', '')[:80] or
        ''
    ).strip()

    # Content
    result['content'] = (
        item.get('content') or
        item.get('descricao') or
        item.get('description') or
        item.get('text') or
        ''
    ).strip()

    # Source
    result['source'] = (
        item.get('source_file') or
        item.get('fonte') or
        item.get('source') or
        ''
    ).strip()

    # Context (optional)
    ctx = item.get('context') or item.get('citacao') or ''
    if ctx:
        result['context'] = ctx.strip()

    # Domain (optional)
    domain = item.get('domain') or ''
    if domain:
        result['domain'] = domain.strip()

    # Extra fields to preserve
    for key in ['valor', 'componentes', 'passos', 'steps', 'principles']:
        if key in item:
            result[key] = item[key]

    return result


def parse_dna_yaml_manual(filepath: Path) -> dict:
    """Parse the broken DNA.yaml line by line, extracting all items."""
    items_by_layer = defaultdict(list)
    seen_ids = set()

    text = filepath.read_text(encoding='utf-8')
    lines = text.split('\n')

    current_section = None
    current_item = None
    current_key = None
    multiline_value = False
    multiline_indent = 0
    list_key = None
    list_items = []
    in_sumario = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip empty/comment lines
        if not stripped or stripped.startswith('#'):
            # But if we're collecting multiline, empty line might end it
            if multiline_value and not stripped:
                if current_item and current_key:
                    current_item[current_key] = current_item.get(current_key, '').rstrip()
                multiline_value = False
            i += 1
            continue

        # Detect section header (L1_FILOSOFIAS:, L2_MODELOS_MENTAIS_ACC:, etc.)
        section_match = re.match(r'^(L[1-5]_\w+):', stripped)
        if section_match and not stripped.startswith('-'):
            raw_section = section_match.group(1)
            # Map to canonical layer name
            for canon, pattern in LAYER_KEY_PATTERNS.items():
                if pattern.match(raw_section):
                    current_section = canon
                    break
            in_sumario = False

            # Save pending item
            if current_item and current_item.get('id'):
                _save_item(current_item, current_section or detect_layer_from_id(current_item['id']),
                          items_by_layer, seen_ids)
            current_item = None
            current_key = None
            multiline_value = False
            i += 1
            continue

        # Detect sumario_geral
        if stripped.startswith('sumario_geral:'):
            in_sumario = True
            if current_item and current_item.get('id'):
                layer = current_section or detect_layer_from_id(current_item['id'])
                _save_item(current_item, layer, items_by_layer, seen_ids)
            current_item = None
            current_section = None
            i += 1
            continue

        # Detect metadata section
        if stripped.startswith('metadata:') or stripped.startswith('layers:'):
            if current_item and current_item.get('id'):
                layer = current_section or detect_layer_from_id(current_item['id'])
                _save_item(current_item, layer, items_by_layer, seen_ids)
            current_item = None
            i += 1
            continue

        # Detect item start: "- id:" at any indentation
        id_match = re.match(r'^[\s-]*id:\s*(.+)', stripped)
        if stripped.startswith('- id:') or (stripped.startswith('id:') and line.lstrip().startswith('- ')):
            # Save previous item
            if current_item and current_item.get('id'):
                layer = current_section or detect_layer_from_id(current_item['id'])
                if layer:
                    _save_item(current_item, layer, items_by_layer, seen_ids)

            # Extract ID
            id_val = re.search(r'id:\s*["\']?([^"\'#\n]+)', stripped)
            current_item = {'id': id_val.group(1).strip() if id_val else ''}
            current_key = None
            multiline_value = False

            # If in sumario, items here belong to a layer (detect from ID)
            if in_sumario and current_item['id']:
                detected = detect_layer_from_id(current_item['id'])
                if detected:
                    current_section = detected
                    in_sumario = False

            i += 1
            continue

        # Check for "- id:" with dash on the line
        dash_id = re.match(r'^\s*-\s+id:\s*["\']?([^"\'#\n]+)', line)
        if dash_id:
            if current_item and current_item.get('id'):
                layer = current_section or detect_layer_from_id(current_item['id'])
                if layer:
                    _save_item(current_item, layer, items_by_layer, seen_ids)
            current_item = {'id': dash_id.group(1).strip()}
            current_key = None
            multiline_value = False
            i += 1
            continue

        # If collecting multiline value
        if multiline_value and current_item and current_key:
            indent = len(line) - len(line.lstrip())
            if indent >= multiline_indent:
                current_item[current_key] = current_item.get(current_key, '') + ' ' + stripped
                i += 1
                continue
            else:
                current_item[current_key] = current_item.get(current_key, '').strip()
                multiline_value = False
                # Fall through to process this line

        # If inside an item, parse key: value pairs
        if current_item is not None:
            # List items (componentes, passos, etc.)
            if stripped.startswith('- "') or stripped.startswith("- '"):
                if list_key and list_key in current_item:
                    val = stripped[2:].strip().strip('"').strip("'")
                    if isinstance(current_item[list_key], list):
                        current_item[list_key].append(val)
                i += 1
                continue

            kv_match = re.match(r'^[\s]*(\w+):\s*(.*)', line)
            if kv_match:
                key = kv_match.group(1).strip()
                val = kv_match.group(2).strip()

                if key == 'id':
                    # Already handled above
                    i += 1
                    continue

                # Skip sumario keys
                if key in ('elementos', 'proximos_ids', 'total_elementos', 'layers_total'):
                    i += 1
                    continue

                # Multiline indicator
                if val == '>' or val == '|':
                    current_key = key
                    current_item[key] = ''
                    multiline_value = True
                    multiline_indent = len(line) - len(line.lstrip()) + 2
                    i += 1
                    continue

                # List indicator
                if not val and key in ('componentes', 'passos', 'steps', 'principles'):
                    list_key = key
                    current_item[key] = []
                    i += 1
                    continue

                # Regular value
                val = val.strip('"').strip("'")
                current_item[key] = val
                current_key = key
                list_key = None

        i += 1

    # Save last item
    if current_item and current_item.get('id'):
        layer = current_section or detect_layer_from_id(current_item['id'])
        if layer:
            _save_item(current_item, layer, items_by_layer, seen_ids)

    return dict(items_by_layer), seen_ids


def _save_item(item, layer, items_by_layer, seen_ids):
    """Save item to the appropriate layer, skip duplicates."""
    if not layer or not item.get('id'):
        return
    item_id = item['id'].strip('"').strip("'")
    if item_id in seen_ids:
        return
    seen_ids.add(item_id)
    normalized = normalize_item(item)
    items_by_layer[layer].append(normalized)


def parse_wave_file(filepath: Path) -> dict:
    """Parse a MH wave YAML file."""
    items_by_layer = defaultdict(list)
    text = filepath.read_text(encoding='utf-8')
    lines = text.split('\n')

    current_layer = None
    current_item = None
    current_key = None
    multiline = False
    multiline_indent = 0

    for line in lines:
        stripped = line.strip()

        if not stripped or stripped.startswith('#'):
            if multiline and not stripped:
                multiline = False
            continue

        # Layer header
        for canon, pattern in LAYER_KEY_PATTERNS.items():
            lm = re.match(r'^\s*(' + pattern.pattern + r'):', stripped)
            if lm:
                if current_item and current_item.get('id'):
                    items_by_layer[current_layer].append(normalize_item(current_item))
                current_layer = canon
                current_item = None
                multiline = False
                break

        # Item start
        dash_id = re.match(r'^\s*-\s+id:\s*["\']?([^"\'#\n]+)', line)
        if dash_id:
            if current_item and current_item.get('id') and current_layer:
                items_by_layer[current_layer].append(normalize_item(current_item))
            current_item = {'id': dash_id.group(1).strip()}
            multiline = False
            continue

        if multiline and current_item and current_key:
            indent = len(line) - len(line.lstrip())
            if indent >= multiline_indent:
                current_item[current_key] = current_item.get(current_key, '') + ' ' + stripped
                continue
            else:
                current_item[current_key] = current_item.get(current_key, '').strip()
                multiline = False

        if current_item is not None:
            kv = re.match(r'^\s+(\w+):\s*(.*)', line)
            if kv:
                key = kv.group(1)
                val = kv.group(2).strip()
                if key == 'id':
                    continue
                if val in ('>', '|'):
                    current_key = key
                    current_item[key] = ''
                    multiline = True
                    multiline_indent = len(line) - len(line.lstrip()) + 2
                    continue
                current_item[key] = val.strip('"').strip("'")

    # Save last item
    if current_item and current_item.get('id') and current_layer:
        items_by_layer[current_layer].append(normalize_item(current_item))

    return dict(items_by_layer)


def content_hash(text: str) -> str:
    """Hash content for dedup comparison."""
    # Normalize whitespace and case for comparison
    normalized = re.sub(r'\s+', ' ', text.lower().strip())
    return hashlib.md5(normalized.encode()).hexdigest()[:16]


def dedup_items(existing: list, new_items: list, threshold=0.85) -> list:
    """Remove new items that are duplicates of existing ones (by content similarity)."""
    existing_hashes = {}
    for item in existing:
        h = content_hash(item.get('content', '') or item.get('title', ''))
        existing_hashes[h] = item['id']

    # Also build set of existing content words for fuzzy match
    existing_contents = {}
    for item in existing:
        content = (item.get('content', '') or '') + ' ' + (item.get('title', '') or '')
        words = set(re.findall(r'\w+', content.lower()))
        if len(words) >= 5:
            existing_contents[item['id']] = words

    unique = []
    dupes = []

    for item in new_items:
        h = content_hash(item.get('content', '') or item.get('title', ''))

        # Exact hash match
        if h in existing_hashes:
            dupes.append((item['id'], existing_hashes[h], 'exact'))
            continue

        # Fuzzy match (Jaccard similarity)
        content = (item.get('content', '') or '') + ' ' + (item.get('title', '') or '')
        words = set(re.findall(r'\w+', content.lower()))

        is_dupe = False
        if len(words) >= 5:
            for eid, ewords in existing_contents.items():
                intersection = words & ewords
                union = words | ewords
                similarity = len(intersection) / len(union) if union else 0
                if similarity >= threshold:
                    dupes.append((item['id'], eid, f'fuzzy:{similarity:.2f}'))
                    is_dupe = True
                    break

        if not is_dupe:
            unique.append(item)

    return unique, dupes


def id_number(item_id: str) -> int:
    """Extract numeric part from ID like FIL-DK-492 -> 492."""
    m = re.search(r'(\d+)$', item_id)
    return int(m.group(1)) if m else 0


def write_clean_yaml(items_by_layer: dict, output_path: Path,
                     total_elements: int, sources_list: list,
                     mh_stats: dict, version: str):
    """Write a clean, properly structured DNA.yaml."""

    lines = []
    lines.append(f"# DNA COGNITIVO - DAN KENNEDY")
    lines.append(f"# Sources: {' + '.join(sources_list)}")
    lines.append(f"# Version: {version}")
    lines.append(f"# Date: {date.today().isoformat()}")
    lines.append(f"# Total Elements: {total_elements}")
    lines.append("")
    lines.append("metadata:")
    lines.append('  person: "Dan Kennedy"')
    lines.append("  sources:")
    for s in sources_list:
        lines.append(f'    - "{s}"')
    lines.append('  source_type: "MASTERCLASS_MULTI"')
    lines.append(f'  version: "{version}"')
    lines.append(f'  created: "{date.today().isoformat()}"')
    lines.append(f"  total_elements: {total_elements}")
    lines.append("")

    layer_counts = {}

    for layer_key in LAYER_ORDER:
        items = items_by_layer.get(layer_key, [])
        # Sort by ID number
        items.sort(key=lambda x: id_number(x['id']))
        layer_counts[layer_key] = len(items)

        lines.append(f"# {'=' * 70}")
        lines.append(f"# {layer_key} — {len(items)} elements")
        lines.append(f"# {'=' * 70}")
        lines.append(f"{layer_key}:")

        for item in items:
            lines.append(f'  - id: "{item["id"]}"')

            title = item.get('title', '')
            if title:
                # Escape quotes in title
                title = title.replace('"', '\\"')
                lines.append(f'    title: "{title}"')

            content = item.get('content', '')
            if content:
                # Use folded scalar for long content
                if len(content) > 120 or '\n' in content:
                    lines.append('    content: >')
                    # Wrap at ~100 chars
                    words = content.split()
                    current_line = ''
                    for word in words:
                        if len(current_line) + len(word) + 1 > 100:
                            lines.append(f'      {current_line}')
                            current_line = word
                        else:
                            current_line = f'{current_line} {word}'.strip()
                    if current_line:
                        lines.append(f'      {current_line}')
                else:
                    content = content.replace('"', '\\"')
                    lines.append(f'    content: "{content}"')

            source = item.get('source', '')
            if source:
                source = source.replace('"', '\\"')
                lines.append(f'    source: "{source}"')

            context = item.get('context', '')
            if context:
                context = context.replace('"', '\\"')
                lines.append(f'    context: "{context}"')

            domain = item.get('domain', '')
            if domain:
                lines.append(f'    domain: "{domain}"')

            # List fields
            for list_key in ('componentes', 'passos', 'steps', 'principles'):
                if list_key in item and isinstance(item[list_key], list):
                    lines.append(f'    {list_key}:')
                    for lv in item[list_key]:
                        lv = str(lv).replace('"', '\\"')
                        lines.append(f'      - "{lv}"')

            valor = item.get('valor', '')
            if valor:
                lines.append(f'    valor: "{valor}"')

            lines.append('')  # blank line between items

    # Summary section
    lines.append(f"# {'=' * 70}")
    lines.append("# SUMMARY")
    lines.append(f"# {'=' * 70}")
    lines.append("summary:")
    lines.append(f"  total_elements: {total_elements}")
    lines.append(f"  layers:")
    for layer_key in LAYER_ORDER:
        count = layer_counts.get(layer_key, 0)
        short = layer_key.split('_')[0]
        lines.append(f"    {layer_key}: {count}")

    layer_str = ' '.join(f"{lk.split('_')[0]}:{layer_counts.get(lk, 0)}" for lk in LAYER_ORDER)
    lines.append(f'  layers_compact: "{layer_str}"')
    lines.append(f"  sources_count: {len(sources_list)}")
    lines.append(f"  version: \"{version}\"")

    # Next IDs
    lines.append("  next_ids:")
    for layer_key in LAYER_ORDER:
        items = items_by_layer.get(layer_key, [])
        if items:
            max_num = max(id_number(it['id']) for it in items)
            prefix = ID_PREFIXES[layer_key]
            lines.append(f'    {layer_key}: "{prefix}{max_num + 1}"')

    output_path.write_text('\n'.join(lines), encoding='utf-8')


def main():
    print("=" * 70)
    print("DK DNA Fix & Merge Script")
    print("=" * 70)

    # Step 1: Backup
    print(f"\n[1/6] Backing up DNA.yaml → {BACKUP_PATH.name}")
    if DNA_PATH.exists():
        BACKUP_PATH.write_bytes(DNA_PATH.read_bytes())
        print(f"  Backup created: {BACKUP_PATH.stat().st_size:,} bytes")

    # Step 2: Parse existing DNA.yaml
    print(f"\n[2/6] Parsing existing DNA.yaml ({DNA_PATH.stat().st_size:,} bytes)...")
    existing_items, existing_ids = parse_dna_yaml_manual(DNA_PATH)

    total_existing = sum(len(v) for v in existing_items.values())
    print(f"  Parsed {total_existing} items from existing DNA:")
    for layer in LAYER_ORDER:
        count = len(existing_items.get(layer, []))
        print(f"    {layer}: {count}")

    # Step 3: Parse MH wave files
    print(f"\n[3/6] Parsing 8 MH wave files...")
    mh_items = defaultdict(list)
    mh_ids = set()

    for wave_num in range(1, 9):
        wave_path = MH_DIR / f"DNA-MH-WAVE-{wave_num}.yaml"
        if not wave_path.exists():
            print(f"  WARNING: {wave_path.name} not found!")
            continue

        wave_data = parse_wave_file(wave_path)
        wave_count = sum(len(v) for v in wave_data.values())
        print(f"  Wave {wave_num}: {wave_count} items")

        for layer, items in wave_data.items():
            for item in items:
                if item['id'] not in mh_ids:
                    mh_ids.add(item['id'])
                    mh_items[layer].append(item)

    total_mh_raw = sum(len(v) for v in mh_items.values())
    print(f"\n  Total MH (cross-wave dedup): {total_mh_raw}")
    for layer in LAYER_ORDER:
        count = len(mh_items.get(layer, []))
        if count > 0:
            print(f"    {layer}: {count}")

    # Step 4: Dedup MH against existing
    print(f"\n[4/6] Deduplicating MH against existing...")
    unique_mh = defaultdict(list)
    all_dupes = []

    for layer in LAYER_ORDER:
        existing_layer = existing_items.get(layer, [])
        mh_layer = mh_items.get(layer, [])

        if not mh_layer:
            continue

        unique, dupes = dedup_items(existing_layer, mh_layer, threshold=0.80)
        unique_mh[layer] = unique
        all_dupes.extend(dupes)

        if dupes:
            print(f"  {layer}: {len(mh_layer)} → {len(unique)} ({len(dupes)} dupes removed)")
        else:
            print(f"  {layer}: {len(mh_layer)} → {len(unique)} (no dupes)")

    total_mh_unique = sum(len(v) for v in unique_mh.values())
    print(f"\n  MH unique after dedup: {total_mh_unique} (removed {total_mh_raw - total_mh_unique})")

    if all_dupes:
        print(f"\n  Duplicates found:")
        for new_id, existing_id, method in all_dupes[:20]:
            print(f"    {new_id} ≈ {existing_id} ({method})")
        if len(all_dupes) > 20:
            print(f"    ... and {len(all_dupes) - 20} more")

    # Step 5: Merge
    print(f"\n[5/6] Merging...")
    merged = defaultdict(list)

    for layer in LAYER_ORDER:
        merged[layer] = list(existing_items.get(layer, []))
        merged[layer].extend(unique_mh.get(layer, []))

    total_merged = sum(len(v) for v in merged.values())
    print(f"  Total merged: {total_merged}")
    for layer in LAYER_ORDER:
        ex_count = len(existing_items.get(layer, []))
        mh_count = len(unique_mh.get(layer, []))
        total = len(merged[layer])
        print(f"    {layer}: {ex_count} + {mh_count} = {total}")

    # Step 6: Write clean YAML
    sources = [
        "The Copywriting Clinic (CC)",
        "7-Figure Academy (7FA)",
        "12 Business Building Strategies (12BBS)",
        "Advanced Coaching & Consulting (ACC)",
        "Magnetic Marketing (MM)",
        "Make Them Buy Now (MTBN)",
        "Greatest Hits Newsletters (GH)",
        "Living Legend Formula (LLF)",
        "Mind Hijacking (MH)",
    ]

    version = "25.0.0"

    mh_stats = {
        'raw': total_mh_raw,
        'unique': total_mh_unique,
        'dupes': total_mh_raw - total_mh_unique,
    }

    print(f"\n[6/6] Writing clean DNA.yaml (v{version})...")
    write_clean_yaml(merged, DNA_PATH, total_merged, sources, mh_stats, version)

    new_size = DNA_PATH.stat().st_size
    print(f"  Written: {new_size:,} bytes")
    print(f"  Backup: {BACKUP_PATH.stat().st_size:,} bytes")

    # Final summary
    print(f"\n{'=' * 70}")
    print(f"SUMMARY")
    print(f"{'=' * 70}")
    print(f"  Before: {total_existing} elements (v24.0.0, 8 sources)")
    print(f"  MH raw: {total_mh_raw} → unique: {total_mh_unique}")
    print(f"  After:  {total_merged} elements (v{version}, 9 sources)")
    print(f"  Delta:  +{total_mh_unique} elements")

    layer_str = ' '.join(f"{lk.split('_')[0]}:{len(merged.get(lk, []))}" for lk in LAYER_ORDER)
    print(f"  Layers: {layer_str}")

    # Next IDs
    print(f"\n  Next IDs:")
    for layer_key in LAYER_ORDER:
        items = merged.get(layer_key, [])
        if items:
            max_num = max(id_number(it['id']) for it in items)
            prefix = ID_PREFIXES[layer_key]
            print(f"    {prefix}{max_num + 1}")

    print(f"\n  Done. Consider it done, senhor.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
