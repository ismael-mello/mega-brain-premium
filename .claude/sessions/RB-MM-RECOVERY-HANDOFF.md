# HANDOFF: RB-MM RECOVERY — DNA.yaml Lost MM-01 to MM-05

## Status
- **CRITICAL: DNA.yaml at 775 elements (pre-MM state)**
- MM-01 through MM-05 (234 elements) were LOST in a `git checkout` that restored to last committed state
- MM-06 script exists (`scripts/rb_mm06_greatest_hits_insert.py`) with 51 elements but has insertion bug
- Total target: 775 + 234 + 51 = 1060 elements

## What Happened
- Previous session attempted MM-06 insertion, script failed due to wrong section search
- `git checkout` was used to restore DNA.yaml, but it went back to the ONLY committed version (86aa3f3, directory migration)
- That version had 775 elements — before ANY MM batches
- MM-01 through MM-05 were never committed to git

## DNA.yaml Structure (CRITICAL for script fix)
```
layers:
  L1_PHILOSOPHIES:     # line 18, ends ~line 791
    count: 129
    items:
      - id: "PHI-RB-001"    # IDs ARE QUOTED
        ...
      - id: "PHI-RB-FPD-014"  # Last entry before separator
        ...module_sources: [FPD]

  # ========== separator ==========
  L2_MENTAL_MODELS:    # line 797, ends ~line 1493
    count: 109
    items:
      ...
      - id: "MM-RB-FPD-012"   # Last entry

  # ========== separator ==========
  L3_HEURISTICS:       # line 1499, ends ~line 2654
    count: 173
    items:
      ...
      - id: "HEUR-RB-FPD-028" # Last entry

  # ========== separator ==========
  L4_FRAMEWORKS:       # line 2660, ends ~line 3625
    count: 109
    items:
      ...
      - id: "FW-RB-FPD-028"   # Last entry

  # ========== separator ==========
  L5_METHODOLOGIES:    # line 3631, ends before metadata
    count: 66
    items:
      ...
```

Metadata at end (line ~5440+):
- total_unique_elements: 775
- by_layer: PHI:157 MM:137 HEUR:230 FW:157 MET:88 (= 769, slight mismatch with 775)
- Source blocks: ITH, FHC, FPD, FU2016, MCC, OMG

## Recovery Plan

### Step 1: Check for existing MM insertion scripts
```
ls scripts/rb_mm*.py
```
Previous sessions may have created scripts for MM-01 through MM-05.

### Step 2: Check handoff files for element data
```
.claude/sessions/RB-MM-01-COMPLETE-HANDOFF.md
.claude/sessions/RB-MM-02-PAUSE-HANDOFF.md
.claude/sessions/RB-MM-03-READY-HANDOFF.md
.claude/sessions/RB-MM-04-READY-HANDOFF.md
.claude/sessions/RB-MM-05-READY-HANDOFF.md
```
These may contain the extracted elements or reference scripts that have them.

### Step 3: Fix insertion approach
The script bug: searches for `\nphilosophies:` but actual YAML uses `  L1_PHILOSOPHIES:` under `layers:`.

**Correct approach:** For each layer, find the separator comment line:
```
  # ==========================================================================
  # L2: MENTAL MODELS
```
And insert new entries BEFORE this separator (after the last `module_sources:` line of previous section).

For L5 (last section), insert before the metadata block that starts around line 5440.

### Step 4: Insert all MM batches
Order: MM-01 → MM-02 → MM-03 → MM-04 → MM-05 → MM-06 → update metadata

### Step 5: After recovery
- MM-07 (Todd Brown Swipe, 2 files)
- MM-08 (Welcome + extras, ~1 file)
- COMMIT after each successful insertion!

## Key Details
- DNA path: `knowledge/external/dna/persons/russell-brunson/DNA.yaml`
- IDs are QUOTED in YAML: `"PHI-RB-001"` not `PHI-RB-001`
- Script elements use UNQUOTED IDs — need to add quotes or script will produce invalid YAML
- Current layer counts: PHI:157 MM:137 HEUR:230 FW:157 MET:88 (=769 in items, metadata says 775)
- Section separators are 2-space indented `# ====` comment blocks

## MM-06 Script Location
`scripts/rb_mm06_greatest_hits_insert.py` — has all 51 elements ready, just needs:
1. Fix section search logic
2. Add quotes to IDs in the element strings
3. Verify indentation matches (4-space for items under `items:`)

## IMPORTANT: COMMIT AFTER EACH BATCH
The entire loss happened because changes were never committed. After EACH successful batch insertion + YAML validation, DO A GIT COMMIT.
