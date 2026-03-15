# HANDOFF: RB-MM RECOVERY SESSION 2 — 2026-03-15

## STATUS: RESEARCH COMPLETE, READY TO EXECUTE

## Current DNA State
- **Path:** `knowledge/external/dna/persons/russell-brunson/DNA.yaml`
- **Size:** 385,349 bytes
- **Elements:** 775 (pre-MM, confirmed via metadata)
- **Structure:** `layers:` → `L1_PHILOSOPHIES:` (line 18), `L2_MENTAL_MODELS:` (line 797), `L3_HEURISTICS:` (line 1499), `L4_FRAMEWORKS:` (line 2660), `L5_METHODOLOGIES:` (line 3631)
- **OMG sections:** `L1_PHILOSOPHIES_OMG:` (line 5254) through `L5_METHODOLOGIES_OMG:` (line 5416)
- **Items indent:** 6-space `      - id: "PHI-RB-001"`
- **Metadata:** at end, after `# STATISTICS` comment
- **Total `- id:` entries:** 738 (via grep count)

## What We Have (Scripts with YAML Elements)

| Batch | Script | Elements | Status |
|-------|--------|----------|--------|
| MM-04 (ES LIVE) | `scripts/rb_mm04_eslive_insert.py` | 73 (PHI:11 MM:13 HEUR:26 FW:13 MET:10) | YAML ready, needs insertion fix |
| MM-05 (TS LIVE) | `scripts/rb_mm05_tslive_insert.py` | 53 (PHI:12 MM:12 HEUR:15 FW:9 MET:5) | YAML ready, needs insertion fix |
| MM-06 (Greatest Hits) | `scripts/rb_mm06_greatest_hits_insert.py` | 51 (PHI:10 MM:10 HEUR:19 FW:8 MET:4) | YAML ready, needs insertion fix |
| **Subtotal** | | **177** | |

## What We DON'T Have (No Scripts, No YAML)

| Batch | Source Files | Elements | Status |
|-------|-------------|----------|--------|
| MM-01 (Funnel Labs 1-8) | `inbox/.../05-Funnel Labs/` (dir exists) | 47 (PHI:9 MM:8 HEUR:15 FW:9 MET:6) | Need re-extraction |
| MM-02 (Funnelology 17) | `inbox/.../04-Funnelology/` (dir exists) | 40 (PHI:9 MM:8 HEUR:13 FW:6 MET:4) | Need re-extraction, concepts in handoff |
| MM-03 (DCS LIVE 4) | Unknown location | 27 (PHI:5 MM:5 HEUR:10 FW:4 MET:3) | Need re-extraction, IDs+desc in handoff |
| **Subtotal** | | **114** | |

## Source File Status
- `inbox/Dan Kennedy & Russell Brunson - Magnetic Marketing/` EXISTS
- Only 1 .txt file found in inbox (transcription_mp4_00-Welcome_.txt)
- Subdirs exist: `01-Magnetic Marketing System/05-Funnel Labs/`, `02-Bonuses/04-Funnelology/`
- Most transcription .txt files show as DELETED in git status (D prefix)
- **CRITICAL:** Need to check if Funnel Labs and Funnelology dirs have actual files inside

## Script Insertion Issues (ALL 3 scripts broken for current DNA)

### MM-04 (`rb_mm04_eslive_insert.py`)
- Uses markers like `"  # L2: MENTAL MODELS - DCS LIVE ADDITIONS"` — these DON'T EXIST (added by MM-03, which was lost)
- Needs rewrite to use layer section headers instead

### MM-05 (`rb_mm05_tslive_insert.py`)
- Uses `content.index("  L2_MENTAL_MODELS:")` — inserts at START of section, not END
- Would need to insert at END of each layer (before next section separator)

### MM-06 (`rb_mm06_greatest_hits_insert.py`)
- Searches for `\nphilosophies:` which doesn't exist (real: `  L1_PHILOSOPHIES:`)
- Also has unquoted IDs: `- id: PHI-RB-176` should be `- id: "PHI-RB-176"`

## Correct Insertion Strategy

For the current DNA.yaml (775 elements), each layer's items end before the next section separator comment:
```
      - id: "PHI-RB-FPD-014"   # last item in L1
        ...
        module_sources: [FPD]

  # ==========================================================================
  # L2: MENTAL MODELS
  # ==========================================================================
  L2_MENTAL_MODELS:
```

**Strategy:** For each layer, find the separator comment before the NEXT layer and insert new items BEFORE that separator.

For L5 (last main layer), insert before the OMG sections:
```
  # ==========================================================================
  # L1: PHILOSOPHIES - OMG ADDITIONS
```

## Recommended Next Session Plan

### Phase A: Insert MM-04 + MM-05 + MM-06 (177 elements)
1. Create ONE master insertion script that:
   - Reads current DNA.yaml
   - For each layer, finds the separator before the next section
   - Inserts new elements BEFORE that separator
   - Handles all 3 batches in sequence
   - Quotes all IDs properly
   - Updates metadata counts
2. Run script
3. Validate YAML (python3 -c "import yaml; yaml.safe_load(open(...))")
4. GIT COMMIT immediately

### Phase B: Re-extract MM-01 + MM-02 + MM-03 (114 elements)
1. Check if source files exist in Funnel Labs and Funnelology dirs
2. If yes: read transcriptions, extract elements following DNA extraction protocol
3. If no: check if files can be recovered from git history or other location
4. Create insertion script with extracted elements
5. Run, validate, GIT COMMIT

### Phase C: Finalize
1. Update metadata to final counts
2. Update MEMORY.md
3. Proceed to MM-07 (Todd Brown, 2 files) and MM-08 (Welcome, 1 file)

## Key References
- Recovery handoff: `.claude/sessions/RB-MM-RECOVERY-HANDOFF.md`
- MM-01 handoff: `.claude/sessions/RB-MM-01-COMPLETE-HANDOFF.md` (only counts)
- MM-02 handoff: `.claude/sessions/RB-MM-02-PAUSE-HANDOFF.md` (concept descriptions)
- MM-03 handoff: `.claude/sessions/RB-MM-03-READY-HANDOFF.md` (IDs + short descriptions)
- MM-04 handoff: `.claude/sessions/RB-MM-04-READY-HANDOFF.md` (IDs + descriptions)
- MM-05 handoff: `.claude/sessions/RB-MM-05-READY-HANDOFF.md` (IDs + descriptions)
- MM-06 handoffs: `.claude/sessions/RB-MM-06-READY-HANDOFF.md` and `RB-MM-06-PROGRESS-HANDOFF.md`

## CRITICAL RULES
- COMMIT after each successful batch insertion
- IDs must be QUOTED: `"PHI-RB-001"` not `PHI-RB-001`
- Items use 6-space indent under `items:`
- Modelo OPUS obrigatório para escrita de DNA (Fase 3)
