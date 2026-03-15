# HANDOFF: RB-MM-06 IN PROGRESS — Script Needs Fix

## Status
- **RB-MM-06 (Greatest Hits 4 RB files): EXTRACTION DONE, INSERTION PENDING**
- **DNA.yaml RESTORED** to pre-attempt state (git checkout)
- Script `scripts/rb_mm06_greatest_hits_insert.py` has all 51 elements written but insertion logic broken

## What Happened
- All 4 files read and analyzed successfully
- 51 DNA elements extracted (PHI:10, MM:10, HEUR:19, FW:8, MET:4)
- Insertion script created at `scripts/rb_mm06_greatest_hits_insert.py`
- Script failed: DNA.yaml uses `layers:` → nested `philosophies:` etc., NOT top-level section headers
- Section finder returned -1 for all layers (searching `\nphilosophies:` but actual pattern is `  philosophies:` indented under `layers:`)
- DNA.yaml restored to clean state via git checkout

## Fix Needed
The script's `find_last_entry_end` logic needs to search for INDENTED section headers:
- `  philosophies:` (2-space indent under `layers:`)
- `  mental_models:` etc.
- Or find by last ID per layer: PHI-RB-175, MM-RB-155, HEUR-RB-252, FW-RB-150, MET-RB-094

**Easiest fix:** Search for last ID in each layer and insert after its `module_sources` line.

## Elements Ready (all in the script)
| Layer | Count | IDs |
|-------|-------|-----|
| PHI | 10 | PHI-RB-176 to PHI-RB-185 |
| MM | 10 | MM-RB-156 to MM-RB-165 |
| HEUR | 19 | HEUR-RB-253 to HEUR-RB-271 |
| FW | 8 | FW-RB-151 to FW-RB-158 |
| MET | 4 | MET-RB-095 to MET-RB-098 |
| **Total** | **51** | |

## DNA Counts After (expected)
- L1 (PHI): 213, max ID=PHI-RB-185
- L2 (MM): 193, max ID=MM-RB-165
- L3 (HEUR): 328, max ID=HEUR-RB-271
- L4 (FW): 206, max ID=FW-RB-158
- L5 (MET): 120, max ID=MET-RB-098
- **Total: 1060 elements**

## Next Steps (this session's continuation)
1. Fix script: change section search to indented headers or use last-ID approach
2. Run fixed script to insert all 51 elements
3. Verify DNA.yaml integrity (YAML parse test)
4. Update metadata (GH source block + counts)
5. Save handoff for RB-MM-07 (Todd Brown 2 files)

## Remaining Batches After MM-06
| Batch | Content | Files | Status |
|-------|---------|-------|--------|
| RB-MM-07 | Todd Brown Swipe | 2 | PENDING |
| RB-MM-08 | Welcome + extras | ~1 | PENDING |

## Key Content Summary (Greatest Hits)
- **Jan 2022:** $4 EPC membership funnel, radical imbalance, ecomm offer stacking, negotiate-crazy-ask
- **Feb 2022:** Invisible virtual event ($25K coaching x259), achievement vs fulfillment, event horizons
- **Mar 2022:** Evergreen webinar ($3.2M/90min), SLO segmentation, WHY philosophy, multiple versions
- **Apr 2022:** Pre-funnels 80% cost reduction, DK media economics, 4 levels of value (implementation→imagination)
