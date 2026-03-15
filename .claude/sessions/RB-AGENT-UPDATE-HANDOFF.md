# HANDOFF: RB Agent Update + Cargo Enrichment

## STATUS: PAUSED (context limit)

## O QUE FOI FEITO
- Leitura completa de todos os arquivos do agent RB (AGENT.md, SOUL.md, MEMORY.md, DNA-CONFIG.yaml)
- Verificação: DNA.yaml tem **1.013 elementos reais** (contagem Python confirmada)
- DNA-CONFIG.yaml version bumped: 17.0.0 → 18.0.0
- DK agent já está completo (v5.0.0, 1358 elementos, MM incluído)

## DISCREPÂNCIA CRÍTICA IDENTIFICADA
- **AGENT.md diz:** 1.312 elementos, L1:257 L2:239 L3:398 L4:264 L5:168
- **DNA-CONFIG.yaml diz:** 1.327 (statistics section)
- **DNA.yaml REAL:** 1.013 elementos, L1:169 L2:150 L3:262 L4:173 L5:243 (+16 OMG)
- **Causa:** Recovery scripts (Phase A/B/C) reconstruíram DNA.yaml mas estimativas acumuladas no DNA-CONFIG e AGENT ficaram infladas
- **DNA.yaml `count` fields internos** também desatualizados (somam ~604 vs 1013 real)

## PENDÊNCIAS (em ordem de prioridade)

### 1. DNA-CONFIG.yaml (PARCIALMENTE FEITO)
- [x] Version bump 17→18
- [ ] Adicionar MM sources (6 programas: Funnel Labs, Funnelology, DCS LIVE, ES LIVE, TS LIVE, Welcome)
- [ ] Atualizar `dna_statistics` section:
  - `total_unique_elements: 1013` (era 1327)
  - `by_layer: L1:169, L2:150, L3:262, L4:173, L5:243`
  - Adicionar MM stats: `mm_total_new: 275` (Phase A:177 + Phase B:84 + Phase C:14)
  - `modules_processed: 28` (era 27, +MM)
- [ ] Atualizar `ultima_atualizacao` para "2026-03-15-v28-magnetic-marketing-complete"
- [ ] Adicionar domínios MM: "magnetic-marketing", "lead-magnets", "direct-mail"

### 2. AGENT.md (CRÍTICO - múltiplas referências)
Substituir TODAS as ocorrências (usar replace_all ou grep+edit):
- `1.312` → `1.013` (aparece ~10 vezes: linhas 45, 149, 172, 384, 453, 639, 969, 992, 1020)
- `L1:257 L2:239 L3:398 L4:264 L5:168` → `L1:169 L2:150 L3:262 L4:173 L5:243`
- `26 fontes` → `27 fontes` (ou 28 com MM como fonte separada)
- `v26` → `v28`
- `2026-03-10` (ultima atualização) → `2026-03-15`
- Adicionar seção MM na tabela MINHA FORMACAO

### 3. MEMORY.md
- [ ] Adicionar MM materials na tabela "MATERIAIS PROCESSADOS":
  ```
  | Magnetic Marketing (6 programs via DK-MM) | Recovery/Cross-DNA | Funnel Labs + Funnelology + DCS LIVE + ES LIVE + TS LIVE + Welcome | 51 | 2026-03-15 |
  ```
- [ ] Atualizar "Total verificado" de 759 → 1013
- [ ] Adicionar MM stats: Phase A +177, Phase B +84, Phase C +14
- [ ] Atualizar "Total estimado" para match 1013

### 4. SOUL.md
- [ ] Adicionar conceitos MM-chave ao vocabulário/filosofias:
  - Speak-to-Sell (from ES LIVE)
  - Five Fatal Flaws of Follow-Up (from Funnel Labs)
  - Pest-to-Guest Sequence (from TS LIVE)
  - Stack Slide Architecture (from DCS LIVE)
- [ ] Bump versão 1.3 → 1.4

### 5. DNA.yaml `count` fields
- [ ] Corrigir counts internos em cada layer (L1 count=129 mas actual=169, etc.)
- Script sugerido:
```python
import yaml
with open('knowledge/external/dna/persons/russell-brunson/DNA.yaml', 'r') as f:
    data = yaml.safe_load(f)
for layer_name, layer_data in data['layers'].items():
    if isinstance(layer_data, dict) and 'items' in layer_data:
        layer_data['count'] = len(layer_data['items'])
with open('knowledge/external/dna/persons/russell-brunson/DNA.yaml', 'w') as f:
    yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False, width=200)
```

### 6. Cargo Enrichment
- [ ] **Closer** (agents/cargo/sales/closer/): speak-to-sell, Stack Slide, conviction closing
- [ ] **CMO** (agents/cargo/c-level/cmo/): Five Fatal Flaws, Pest-to-Guest, lead magnets
- [ ] **CRO** (agents/cargo/c-level/cro/): funnel stacking from MM, direct mail integration
- [ ] Update DNA-CONFIG.yaml de cada cargo com RB weight e MM refs

### 7. Cleanup
- [ ] Remover `knowledge/external/dna/persons/russell-brunson/DNA.yaml.bak_phase_c`
- [ ] Limpar scripts de recovery em `scripts/rb_mm*.py` (opcional, manter como referência)

## DADOS PARA REFERÊNCIA RÁPIDA
```
DNA.yaml REAL (confirmado Python):
  L1_PHILOSOPHIES: 169
  L2_MENTAL_MODELS: 150
  L3_HEURISTICS: 262
  L4_FRAMEWORKS: 173
  L5_METHODOLOGIES: 243
  OMG layers: 16 (3+3+5+3+2)
  GRAND TOTAL: 1013

Next IDs: PHI-RB-201, MM-RB-181, HEUR-RB-306, FW-RB-181, MET-RB-111

MM Recovery commits:
  Phase A (MM-04/05/06): a54d636 (+177)
  Phase B (MM-01/02/03): ab9ae20 (+84)
  Phase C (MM-08 Welcome): 8c07e96 (+14)
```

## MODELO RECOMENDADO
Opus para escrita de agentes (Fase 5 = Opus obrigatório)

---
Session ID: RB-AGENT-UPDATE-HANDOFF
Saved at: 2026-03-15
