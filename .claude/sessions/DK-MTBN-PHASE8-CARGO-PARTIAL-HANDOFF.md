# DK MTBN Phase 8 — Cargo Enrichment PARTIAL HANDOFF
# Data: 2026-03-15 | Modelo: SONNET ✅

## STATUS
- Phase 8 = SONNET (não trocar modelo)
- Task 8.7: DONE (27 elementos BATCH-04 reintegrados)
- Task 8.8: PARCIALMENTE DONE (versões bumped, IDs ainda não inseridos)
- DNA running total: ~1973 elementos

## FEITO NESTA SESSÃO (Task 8.8 parcial)
- Closer DNA-CONFIG: versao bumped 3.5.0 → 3.6.0 (changelog ok)
- CMO DNA-CONFIG: versao bumped 3.8.0 → 3.9.0 (changelog ok)

## PENDENTE — Task 8.8 (inserir IDs)

### Closer — agents/cargo/sales/closer/DNA-CONFIG.yaml
Localizar seção `pessoa: "dan-kennedy"` → campo `insight_ids:` (linha ~434)
ADICIONAR após `"FIL-DK-435"`:
```yaml
        - "FW-DK-293"   # MTBN closing framework
        - "FW-DK-294"   # MTBN closing framework
        - "FW-DK-295"   # MTBN closing framework
        - "FW-DK-306"   # MTBN stage closing
        - "FW-DK-307"   # MTBN stage closing
        - "MET-DK-206"  # MTBN selling methodology
        - "MET-DK-207"  # MTBN selling methodology
```

### CMO — agents/cargo/c-level/cmo/DNA-CONFIG.yaml
Localizar seção `elementos_mtbn:` do DK (linha ~484)
ADICIONAR ao final da lista:
```yaml
        - "FIL-DK-420 (Direct Response = Half Psychology Half Math)"
        - "FIL-DK-421 (Stories Have Equity — proprietary and protected)"
        - "FIL-DK-422 (MTBN copy element)"
        - "FW-DK-308 (MTBN framework)"
        - "FW-DK-309 (MTBN framework)"
        - "FW-DK-310 (MTBN framework)"
        - "HEUR-DK-527 (MTBN heuristic)"
        - "HEUR-DK-528 (MTBN heuristic)"
        - "HEUR-DK-529 (MTBN heuristic)"
        - "MET-DK-213 (MTBN methodology)"
        - "MET-DK-214 (MTBN methodology)"
```

### CRO — agents/cargo/c-level/cro/DNA-CONFIG.yaml
1. versao: "3.7.0" → "3.8.0"
2. ultima_atualizacao: manter "2026-03-15"
3. Adicionar ao CHANGELOG:
   `# v3.8.0 (2026-03-15): DK-MTBN Phase 8 — closing systems, affluent revenue, one-to-many revenue ops`
   `#                      - Added 8 MTBN DK insight_ids (FW-DK-293/294/295/296, MET-DK-206/209, MM-DK-358/360)`
4. Localizar `elementos_mtbn:` do DK, ADICIONAR:
```yaml
        - "FW-DK-296 (MTBN framework)"
        - "MET-DK-209 (MTBN methodology)"
        - "MM-DK-358 (MTBN mental model)"
        - "MM-DK-360 (Single Emotion Channel — curiosity displaces skepticism)"
```
   (FW-DK-293/294/295 e MET-DK-206 já estão listados nos elementos existentes? Verificar antes de duplicar)

### COO — agents/cargo/c-level/coo/DNA-CONFIG.yaml
1. versao: "3.4.0" → "3.5.0"
2. ultima_atualizacao: "2026-03-13" → "2026-03-15"
3. Adicionar ao CHANGELOG header:
   `# v3.5.0 (2026-03-15): DK-MTBN Phase 8 — operational systems, list building ops`
   `#                      - Added 2 MTBN DK elements (MET-DK-215, MM-DK-362)`
4. Localizar seção `pessoa: "dan-kennedy"`, após `dominios_acc:`, ADICIONAR:
```yaml
      # MTBN enrichment (2026-03-15 Phase 8)
      elementos_mtbn:
        - "MET-DK-215 (MTBN operational methodology)"
        - "MM-DK-362 (MTBN mental model — operations)"
      dominios_mtbn:
        - "mtbn-operations"
        - "list-building-ops"
```

## Task 8.9 — Commit final (após todos os IDs inseridos)
```
git add agents/cargo/sales/closer/DNA-CONFIG.yaml
git add agents/cargo/c-level/cmo/DNA-CONFIG.yaml
git add agents/cargo/c-level/cro/DNA-CONFIG.yaml
git add agents/cargo/c-level/coo/DNA-CONFIG.yaml
git add knowledge/external/dna/persons/dan-kennedy/
git commit -m "feat(dk): MTBN Phase 8 complete — 1973 elements, cargo enrichment (Closer/CMO/CRO/COO)"
```

## Next IDs para novos elementos DK
FIL-DK-462 | MM-DK-403 | HEUR-DK-587 | FW-DK-348 | MET-DK-245

## REGRA DE MODELO (INQUEBRÁVEL)
- Phase 8 = SONNET ✅ (não trocar)
- Se trabalhar OMC Phases 5-6 depois = OPUS obrigatório (pausar + confirmar troca ANTES de iniciar)
