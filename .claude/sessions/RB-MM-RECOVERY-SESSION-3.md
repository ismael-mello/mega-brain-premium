# HANDOFF: RB-MM RECOVERY SESSION 3 — 2026-03-15

## STATUS: SCRIPT MASTER CRIADO, PRONTO PARA EXECUTAR

## O Que Foi Feito Nesta Sessão
- Lidos os 3 scripts existentes (MM-04, MM-05, MM-06) com todos os elementos YAML
- Identificada estrutura exata do DNA.yaml (separadores entre layers, metadata)
- Criado script master `scripts/rb_mm_master_recovery.py` que:
  - Extrai YAML blocks dos 3 scripts automaticamente
  - Fixa MM-06 (indent 4→6 espaços, IDs sem quote → quoted)
  - Insere 177 elementos em reverse order (L5 primeiro) para preservar posições
  - Atualiza metadata (775 → 952)
  - Valida YAML (restaura backup se falhar)
  - Cria backup automático (.yaml.bak)

## Próxima Sessão — FASE A: Executar Script
1. `python3 scripts/rb_mm_master_recovery.py`
2. Se PASSED → `git add knowledge/external/dna/persons/russell-brunson/DNA.yaml && git commit`
3. Se FAILED → verificar erro YAML, ajustar, re-run

## Próxima Sessão — FASE B: Re-extrair MM-01/02/03
- 114 elementos perdidos (nunca commitados, nunca em script)
- MM-01 (Funnel Labs): 47 elem — verificar se fontes existem em inbox
- MM-02 (Funnelology): 40 elem — conceitos em handoff RB-MM-02-PAUSE-HANDOFF.md
- MM-03 (DCS LIVE): 27 elem — IDs+desc em handoff RB-MM-03-READY-HANDOFF.md
- Fontes em: `inbox/Dan Kennedy & Russell Brunson - Magnetic Marketing/`
- NOTA: muitos .txt deletados (git status mostra D prefix) — verificar se dirs têm arquivos

## Próxima Sessão — FASE C: MM-07 + MM-08
- MM-07 (Todd Brown Swipe Files): 2 arquivos pendentes
- MM-08 (Welcome): 1 arquivo pendente

## DNA State
- **Path:** `knowledge/external/dna/persons/russell-brunson/DNA.yaml`
- **Atual:** 775 elementos (pre-MM recovery)
- **Após Fase A:** 952 elementos (775 + 177)
- **Após Fase B:** ~1066 elementos (952 + 114)
- **Após Fase C:** ~1080+ elementos (final)

## REGRA: MODELO POR ETAPA
- Fases 1-2 (download, chunking): SONNET
- Fases 3-6 (entity → dossier, inclui escrita de DNA): **OPUS OBRIGATÓRIO**
- Fases 7-8 (enrichment, finalization): SONNET
- Recovery de DNA = escrita de DNA = Fase 3 = **OPUS**

## Arquivos Relevantes
- Script master: `scripts/rb_mm_master_recovery.py`
- DNA: `knowledge/external/dna/persons/russell-brunson/DNA.yaml`
- Scripts fonte: `scripts/rb_mm04_eslive_insert.py`, `scripts/rb_mm05_tslive_insert.py`, `scripts/rb_mm06_greatest_hits_insert.py`
- Handoffs anteriores: `.claude/sessions/RB-MM-0[1-6]-*-HANDOFF.md`
