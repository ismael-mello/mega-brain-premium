# SESSION: DK Referral Machine Pipeline

> **Date:** 2026-03-16
> **Status:** PHASES 1-6 COMPLETE | PHASES 7-8 PENDING
> **Model:** Phases 1-2 (Sonnet) → 3-6 (Opus) ✅ | 7-8 (Sonnet) PENDING
> **Source:** Dan Kennedy - The Ultimate No BS Referral Machine (RM)

---

## WHAT WAS DONE

### Phase 1: Initialization ✅
- 62 files moved from `inbox/Dan Kennedy - The Ultimate No BS Referral Machine/` to `knowledge/external/sources/dan-kennedy/raw/referral-machine/`
- Structure: Main Course (5 CDs + 4 DVDs) + Bonuses (6 files)
- Total: 619KB, zero empty files

### Phase 2: Chunking ✅
- DVDs overlap CDs 1-4 (same content, <2% difference) → used DVDs as primary
- CD5 (Newsletter Secrets with Sean Buck) has no DVD equivalent → used CD tracks
- 3 logical batches:
  - DK-RM-01: DVD Sessions 1+2 (~87KB)
  - DK-RM-02: DVD Sessions 3+4 + CD5 (~135KB)
  - DK-RM-03: All Bonuses (~233KB)

### Phase 3-4: Entity Resolution + Insight Extraction ✅ (OPUS)
- 65 new DNA elements extracted via `scripts/dk_rm_extract.py`
  - L1 Philosophies: 18 (FIL-DK-560..577)
  - L2 Mental Models: 12 (MM-DK-560..571)
  - L3 Heuristics: 15 (HEUR-DK-729..743)
  - L4 Frameworks: 10 (FW-DK-729..738)
  - L5 Methodologies: 10 (MET-DK-613..622)
- DNA.yaml updated: v26.0.0, 2482 total elements, 10 sources

### Phase 5-6: Synthesis + Dossier ✅ (OPUS)
- DNA-CONFIG.yaml: Source 10 (referral-machine) added + 7 new domains
- DOSSIER-DAN-KENNEDY.md: v3.0.0 updated with RM section
- Key themes: referral marketing, WOW packages, gifting, newsletters, stealth referrals, events, testimonials, reactivation

---

## WHAT REMAINS (Phases 7-8 — use SONNET)

### Phase 7: Agent Enrichment (Cargo Agents)
- [ ] CLOSER: add referral-related sales insights (direct ask, overcoming referral objections)
- [ ] CMO: add referral marketing strategy (newsletter, gifting, omnipresence, events)
- [ ] CRO: add internal marketing ROI, customer segmentation ABC, LTV/referral math
- [ ] Sales Manager: add staff training methodology, compliance system
- [ ] Update MEMORY.md for each enriched cargo agent

### Phase 8: Finalization
- [ ] Create SOURCE-RM.md in `knowledge/external/sources/dan-kennedy/`
- [ ] Update AGENT-INDEX.yaml (sources: 10)
- [ ] Clean inbox: remove `inbox/Dan Kennedy - The Ultimate No BS Referral Machine/`
- [ ] Update AGG-VENDAS.yaml with referral elements
- [ ] Update auto-memory MEMORY.md with final state
- [ ] Commit

---

## KEY FILES MODIFIED
- `knowledge/external/dna/persons/dan-kennedy/DNA.yaml` → v26.0.0 (+65 elements)
- `agents/external/dan-kennedy/DNA-CONFIG.yaml` → source 10 added
- `knowledge/external/dossiers/persons/DOSSIER-DAN-KENNEDY.md` → v3.0.0
- `knowledge/external/sources/dan-kennedy/raw/referral-machine/` → 62 files
- `scripts/dk_rm_extract.py` → extraction script (reusable)

## NEXT IDS
- FIL-DK-578, MM-DK-572, HEUR-DK-744, FW-DK-739, MET-DK-623
