# SESSION: DNA MIGRATION - Legacy to Unified Format
> **Date:** 2026-03-02
> **Status:** IN PROGRESS - 6/9 sources migrated, The Scalable Company next
> **Session ID:** SESSION-2026-03-02-DNA-MIGRATION
> **Saved at:** 2026-03-02T~16:00:00

---

## ESTADO DA MISSÃO
- **Missão**: DNA MIGRATION - Legacy 5-yaml → Unified DNA.yaml
- **Fase**: Migration (not pipeline phase - this is a format migration task)
- **Progresso**: 4/8 sources migrated (144/4,276 elements = ~3.4%)

## OBJECTIVE
Migrate 8 legacy DNA sources from separate 5-yaml format to unified DNA.yaml (Russell Brunson format).

## WHAT WAS DONE THIS SESSION
1. Audited all 9 DNA sources (CONFIG.yaml read for each)
2. Identified scope: 4,276 elements across 8 legacy sources
3. Read ALL 5 layer files for 3 smallest sources via parallel agents
4. WROTE unified DNA.yaml for 3 sources (across 2 context windows):
   - Sam Ovens (21 elements) - DNA.yaml WRITTEN ✅
   - Richard Linder (24 elements) - DNA.yaml WRITTEN ✅
   - Jordan Lee (26 elements) - DNA.yaml WRITTEN ✅
5. Cole Gordon: All 5 layer files READ (output saved to tool-results JSON). Context exhausted before WRITE.

## ARQUIVOS MODIFICADOS
- `knowledge/dna/persons/sam-oven/DNA.yaml` - CREATED (unified format, 21 elements)
- `knowledge/dna/persons/richard-linder/DNA.yaml` - CREATED (unified format, 24 elements)
- `knowledge/dna/persons/jordan-lee/DNA.yaml` - CREATED (unified format, 26 elements)
- `.claude/sessions/SESSION-2026-03-02-DNA-MIGRATION.md` - Updated with progress

## DECISÕES TOMADAS
- **Rich metadata preserved**: Unified DNA.yaml keeps all legacy fields (peso, chunks, fontes, citacao, aplicacao, threshold, componentes, etapas) while restructuring into single-file format
- **Field name standardization**: Legacy Portuguese field names mapped to English (titulo→title, descricao→statement, peso→weight, pergunta_gerada→trigger_question, etc.)
- **Format**: `unified-dna-v1` - compatible with Russell Brunson DNA.yaml structure but enriched with legacy metadata

## WHAT REMAINS
### Immediate (next session):
- WRITE unified DNA.yaml for Cole Gordon (73 elem)
- Cole Gordon data already READ - re-read the 5 legacy files (tool-results JSON may not persist across sessions)
- Cole Gordon CONFIG.yaml already read: 12 filosofias, 10 modelos mentais, 22 heuristicas, 19 frameworks, 10 metodologias

### Future sessions:
| Priority | Source | Elements | Status |
|----------|--------|----------|--------|
| ✅ | Sam Ovens | 21 | DONE |
| ✅ | Richard Linder | 24 | DONE |
| ✅ | Jordan Lee | 26 | DONE |
| ✅ | Cole Gordon | 73 | DONE (this session) |
| ⏳ | Alex Hormozi | 260 | Pending |
| ⏳ | The Scalable Company | 393 | Pending |
| ⏳ | Jeremy Miner | 1,199 | Pending |
| ⏳ | Jeremy Haynes | 2,280 | Pending |

## TARGET FORMAT (Russell Brunson DNA.yaml)
```yaml
person:
  name: "Name"
  source: "Source description"

layers:
  L1_PHILOSOPHIES:
    count: N
    items:
      - id: "PHI-XX-001"
        statement: "..."
        context: "..."
        source_ids: [...]
  L2_MENTAL_MODELS:
    count: N
    items: [...]
  L3_HEURISTICS:
    count: N
    items: [...]
  L4_FRAMEWORKS:
    count: N
    items: [...]
  L5_METHODOLOGIES:
    count: N
    items: [...]
```

## LEGACY FORMAT (per source)
- CONFIG.yaml (metadata + synthesis + connections)
- FILOSOFIAS.yaml (L1)
- MODELOS-MENTAIS.yaml (L2)
- HEURISTICAS.yaml (L3)
- FRAMEWORKS.yaml (L4)
- METODOLOGIAS.yaml (L5)

## DECISION: Keep rich metadata
The legacy format has MORE detail per item (evidencias, chunk_ids, implicacoes, peso, etc.)
The new format is simpler. DECISION: Unified DNA.yaml preserves rich metadata from legacy.

## RESUME INSTRUCTIONS
1. Read this file
2. Jeremy Miner is NEXT (1,199 elem) - ALL 5 LEGACY FILES WERE READ this session but context exhausted before WRITE
3. DO NOT re-read legacy files - go straight to WRITING DNA.yaml
4. Use cole-gordon/DNA.yaml as format reference (first 80 lines read this session)
5. Legacy file counts: FILOSOFIAS=25 items, MODELOS-MENTAIS=15, HEURISTICAS=50, FRAMEWORKS=20, METODOLOGIAS=15 (125 documented items, 1199 total from source)
6. Then Jeremy Haynes (2,280) - largest source, may need multiple sessions
7. FORMAT: unified-dna-v1 with person/layers/L1-L5 structure, fields: id, title, statement, quote, weight, chunk_ids, source_ids, domains, implications

## PENDÊNCIAS
- [x] Cole Gordon DNA.yaml (73 elem) ✅ DONE 2026-03-02
- [x] Alex Hormozi DNA.yaml (59 actual elem in files, CONFIG claimed 260) ✅ DONE 2026-03-02
- [x] The Scalable Company DNA.yaml (393 elem) ✅ DONE 2026-03-02 (196.2 KB, all 393 verified)
- [ ] Jeremy Miner DNA.yaml (1,199 elem) ← NEXT (all 5 legacy files READ, context exhausted before WRITE)
- [ ] Jeremy Haynes DNA.yaml (2,280 elem)

## NOTAS IMPORTANTES
- Cole Gordon is the MOST COMPLEX small source (73 elem, v3.0.0, 8 batch sources, 373 insights processed)
- Cole Gordon has rich CONFIG.yaml with voz, padroes_comportamentais, sintese sections
- For larger sources (Hormozi+), consider splitting into multiple context windows
- Legacy files are NOT deleted after migration - both formats coexist

---
*Consider it done, senhor. JARVIS nunca esquece.*
