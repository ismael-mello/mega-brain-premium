# DK — HANDOFF CONSOLIDADO (OMC + MTBN)
# Data: 2026-03-15 | Proxima sessao: OPUS para steps 1-5, SONNET para steps 6-9

## DESCOBERTA DESTA SESSAO

OMC Phases 5-6 foram PARCIALMENTE executados em sessao anterior.
Artefatos principais JA EXISTEM mas estao desatualizados (mostram 1750, falta MTBN).

## ARTEFATOS QUE JA EXISTEM E ESTAO COMPLETOS

- SOURCE-OMC.md (v1.0.0, 391 elements) — COMPLETO
- SOURCE-MTBN.md — EXISTE
- DOSSIER-OPPORTUNITY-MARKETING.md (v1.0.0) — COMPLETO
- AGENT.md (v6.0.0, 2029 elements, lista MTBN) — COMPLETO

## 4 ARQUIVOS QUE PRECISAM ATUALIZACAO (steps 1-4, OPUS)

### 1. DNA-CONFIG.yaml (CRITICO)
- Path: agents/external/dan-kennedy/DNA-CONFIG.yaml
- Atual: v1.0.0, total_elements: 1750, 6 sources
- ADICIONAR: MTBN source entry (source: "make-them-buy-now", files: 89, elements: ~279, 14 batches, 18 sub-programs)
- ATUALIZAR: total_elements para ~2029
- ATUALIZAR: breakdown para L1:446 L2:386 L3:555 L4:326 L5:233
- ADICIONAR: domains_mtbn (urgency-psychology, scarcity-mechanics, action-triggers, buying-resistance, closing-psychology, impulse-architecture, deadline-strategies, risk-reversal)
- MTBN raw: knowledge/external/sources/dan-kennedy/raw/make-them-buy-now/
- MTBN extraction: knowledge/external/sources/dan-kennedy/mtbn-extraction/
- MTBN IDs: FIL-DK-409..461, MM-DK-349..402, HEUR-DK-507..586, FW-DK-293..347, MET-DK-206..244

### 2. DOSSIER-DAN-KENNEDY.md (MEDIO)
- Path: knowledge/external/dossiers/persons/DOSSIER-DAN-KENNEDY.md
- Atual: v1.0.0, 1750 elements, 7 sources, 545 raw files
- ADICIONAR: Secao 8 MTBN (Make Them Buy Now) com key contributions
- ATUALIZAR: totals para 2029 elements, 8 sources, 634 raw files
- ATUALIZAR: metadata section

### 3. SOUL.md (MENOR)
- Path: agents/external/dan-kennedy/SOUL.md
- Atual: v7.0.0, header "1750 elementos"
- ATUALIZAR: header para 2029 elementos, adicionar MTBN na lista de fontes
- ADICIONAR: MTBN voice patterns/beliefs em secoes relevantes (se distintos do que ja esta)

### 4. MEMORY.md (MENOR)
- Path: agents/external/dan-kennedy/MEMORY.md
- Atual: v4.0.0, ja lista MTBN como fonte #7
- ADICIONAR: 5-10 MTBN-specific insights ao TOP 50 (apos #50)
- ADICIONAR: MTBN thinking patterns

## APOS COMPLETAR STEPS 1-4 → TROCAR PARA SONNET

### Steps 6-9 (SONNET — Phase 7-8)
6. CFO cargo enrichment com DK (unico cargo sem DK)
7. Limpar inbox/Dan Kennedy - Make them buy now/
8. Atualizar AGENT-INDEX.yaml (source counts AH + RB + DK)
9. Commit final

## NEXT IDs DK (pos-MTBN)
FIL-DK-462 | MM-DK-403 | HEUR-DK-587 | FW-DK-348 | MET-DK-245

## CARGO STATUS
Closer 3.6.0 | CMO 3.9.0 | CRO 3.8.0 | COO 3.5.0 (todos com MTBN+OMC done)
CFO: PENDENTE (nenhum DK ainda)
