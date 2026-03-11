# SESSION: STATE.json Propagation Fix
## Date: 2026-03-01
## Status: PARCIALMENTE COMPLETO

---

## O QUE FOI FEITO

### Fix 1: session_end.py - COMPLETO
- Adicionada funcao `sync_metrics_from_filesystem()` que escaneia:
  - artifacts/insights/ (extraction files)
  - knowledge/dna/persons/ (DNA sources)
  - agents/persons/ e agents/cargo/ (agents count)
  - knowledge/dossiers/ (person + theme dossiers)
  - knowledge/playbooks/ (playbooks count)
  - knowledge/dna/aggregated/ (aggregated DNAs)
- Adicionada funcao `sync_from_session_log()` que:
  - Le session logs recentes para extrair metricas precisas
  - Busca files_processed, dna_elements, completed missions
  - Nunca decrementa valores (usa max())
- Ambas funcoes chamadas em main() ANTES de salvar STATE.json

### Fix 2: session_autosave_v2.py - PENDENTE
- **Bug:** Linha 62 aponta para `PROJECT_DIR / "system" / "JARVIS-STATE.json"` (path ERRADO)
- **Correto:** Deveria ser `PROJECT_DIR / ".claude" / "jarvis" / "STATE.json"`
- **Acao necessaria:** Corrigir Config.JARVIS_STATE path
- **Bonus:** Adicionar chamada a sync_metrics no save() do autosave tambem

## PROXIMA SESSAO

1. Abrir `session_autosave_v2.py`
2. Linha 62: Mudar `JARVIS_STATE = PROJECT_DIR / "system" / "JARVIS-STATE.json"` para `JARVIS_STATE = PROJECT_DIR / ".claude" / "jarvis" / "STATE.json"`
3. No metodo `save()` (linha 494), apos atualizar mission_state, adicionar chamada para sync STATE.json
4. Testar ambos hooks com `/verify`

---
Session ID: SESSION-2026-03-01-STATE-FIX
