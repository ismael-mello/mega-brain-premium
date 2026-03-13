---
description: Executa pipeline completo (ingest + process + enrich) sem paradas
argument-hint: [URL or path] [--verbose] [--dry-run] [--person "Name"]
---

# /jarvis-full - Execução Completa do Pipeline

> **Versão:** 1.1.0
> **Alias:** /jf
> **Workflow:** `core/workflows/wf-pipeline-full.yaml`
> **Templates:** `core/templates/phases/narrative-metabolism.md`

---

## DESCRIÇÃO

Executa o pipeline completo desde ingestão até enrichment, sem paradas humanas.
Combina `/ingest` + `/process-jarvis --auto-enrich` em um único comando.

---

## SINTAXE

```
/jarvis-full [URL ou PATH] [FLAGS]
```

| Flag | Descrição |
|------|-----------|
| (nenhuma) | Progresso mínimo + FULL PIPELINE REPORT ao final |
| `--verbose` | Todos os logs aparecem durante execução |
| `--dry-run` | Mostra o que faria sem executar |
| `--person "Nome"` | Define pessoa manualmente |
| `--type TIPO` | Define tipo (PODCAST, MASTERCLASS, COURSE) |

---

## ESTRATÉGIA DE MODELOS POR FASE

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              MODEL ROUTING — /jarvis-full                                   │
├──────┬────────────────────────────────┬────────────────────────────────────┤
│ FASE │ NOME                           │ MODELO                             │
├──────┼────────────────────────────────┼────────────────────────────────────┤
│  1   │ Initialization                 │ Sonnet  (estrutural)               │
│  2   │ Chunking                       │ Sonnet  (mecânico)                 │
├──────┼────────────────────────────────┼────────────────────────────────────┤
│  3   │ Entity Resolution              │ ★ OPUS  (clone começa aqui)        │
│  4   │ Insight Extraction             │ ★ OPUS  (DNA 5 camadas)            │
│  5   │ Narrative Synthesis            │ ★ OPUS  (voz + identidade)         │
│  6   │ Dossier / Narrative Metabolism │ ★ OPUS  (documento vivo)           │
├──────┼────────────────────────────────┼────────────────────────────────────┤
│  7   │ Agent Enrichment               │ Sonnet  (cascateamento)            │
│  8   │ Finalization                   │ Sonnet  (logs + validação)         │
└──────┴────────────────────────────────┴────────────────────────────────────┘

Lógica: Opus nas fases 3–6 (onde o clone é construído — identidade, voz, DNA).
        Sonnet nas fases 1–2 e 7–8 (estruturais/operacionais, sem perda de qualidade).
Resultado: ~50% Opus + ~50% Sonnet = qualidade máxima no clone, tokens equilibrados.
```

### ⚠️ REGRA DE TROCA DE MODELO (OBRIGATÓRIA)

**Antes de iniciar qualquer fase que exija modelo diferente do ativo**, o sistema DEVE pausar e exibir:

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  ⚠️  TROCA DE MODELO NECESSÁRIA                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  A próxima fase requer: [OPUS / SONNET]                                      ║
║  Modelo atual:          [MODEL_ATUAL]                                        ║
║                                                                              ║
║  Use /model para trocar antes de continuar.                                  ║
║                                                                              ║
║  Como deseja prosseguir?                                                     ║
║  → [1] Vou trocar agora   — execute /model e me avise quando pronto          ║
║  → [2] Continuar assim mesmo — seguir com modelo atual (qualidade reduzida)  ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

A próxima fase **só executa após a resposta do usuário** (opção 1 ou 2).

**Pontos de troca no pipeline:**

| Transição | De → Para | Motivo |
|-----------|-----------|--------|
| Fase 2 → 3 | Sonnet → **Opus** | Clone começa: Entity Resolution |
| Fase 6 → 7 | **Opus** → Sonnet | Clone concluído: Enrichment operacional |

---

## COMPORTAMENTO

### Step 1: Ingest (se URL/Path novo)
```
IF input is URL:
  EXECUTE /ingest [URL]
  WAIT for transcript

IF input is local file:
  COPY to inbox/{PERSON}/{TYPE}/
  GENERATE Source ID
```

### Step 2: Pipeline Jarvis (auto-enrich)
```
EXECUTE /process-jarvis "{SOURCE_ID}" --auto-enrich

# 📖 NARRATIVE METABOLISM é aplicado AUTOMATICAMENTE em Phase 6
# Ver: core/templates/phases/narrative-metabolism.md
# Estrutura: TL;DR → Filosofia → Modus Operandi → Arsenal → Armadilhas → Citações → Metadados
# Voz PERSONS: 1ª pessoa | Voz THEMES: Narrador neutro | Densidade: ◯-◐

SHOW minimal progress:
  ⏳ Phase 1: Initialization [Sonnet]... ✅
  ⏳ Phase 2: Chunking ({N} chunks) [Sonnet]... ✅
  ⚠️  → TROCAR PARA OPUS antes de continuar
  ⏳ Phase 3: Entity Resolution [Opus]... ✅
  ⏳ Phase 4: Insight Extraction ({N} insights) [Opus]... ✅
  ⏳ Phase 5: Narrative Synthesis [Opus]... ✅
  ⏳ Phase 6: Dossier Compilation (Narrative Metabolism) [Opus]... ✅
  ⚠️  → TROCAR PARA SONNET antes de continuar
  ⏳ Phase 7: Agent Enrichment [Sonnet]... ✅
  ⏳ Phase 8: Finalization [Sonnet]... ✅
```

### Step 3: Full Pipeline Report
```
GENERATE FULL PIPELINE REPORT (LOG 7)
SAVE to /logs/FULL/FULL-{SOURCE_ID}-{TIMESTAMP}.md
DISPLAY report
```

---

## OUTPUT

### Durante Execução (modo padrão)
```
═══════════════════════════════════════════════════════════════════════════════
                         JARVIS FULL AUTO
                         {SOURCE_ID} - {PERSON_NAME}
═══════════════════════════════════════════════════════════════════════════════

⏳ Ingerindo material... ✅
⏳ Phase 1: Initialization... ✅
⏳ Phase 2: Chunking (28 chunks)... ✅
⏳ Phase 3: Entity Resolution... ✅
⏳ Phase 4: Insight Extraction (14 insights)... ✅
⏳ Phase 5: Narrative Synthesis... ✅
⏳ Phase 6: Dossier Compilation... ✅
⏳ Phase 7: Agent Enrichment... ✅
⏳ Phase 8: Finalization... ✅

✅ COMPLETO em 3m 42s

[FULL PIPELINE REPORT segue abaixo]
```

### Ao Final
```
[FULL PIPELINE REPORT - LOG 7 completo]
```

---

## EQUIVALENTE A

```bash
# Comando único
/jarvis-full https://youtube.com/watch?v=abc123

# É equivalente a:
/ingest https://youtube.com/watch?v=abc123
/process-jarvis "{PATH_GERADO}" --auto-enrich
```

---

## EXEMPLOS

```bash
# YouTube video
/jarvis-full https://youtube.com/watch?v=abc123

# YouTube com pessoa definida
/jarvis-full https://youtube.com/watch?v=abc123 --person "Cole Gordon"

# Arquivo local
/jarvis-full "/path/to/transcript.txt" --person "Jeremy Haynes" --type PODCAST

# Dry run (preview)
/jarvis-full https://youtube.com/watch?v=abc123 --dry-run

# Verbose (todos os logs)
/jarvis-full https://youtube.com/watch?v=abc123 --verbose
```

---

## QUANDO USAR

| Situação | Comando |
|----------|---------|
| Quer controle total | `/ingest` + `/process-jarvis` |
| Quer revisar antes de enriquecer | `/process-jarvis` (checkpoint em Phase 6) |
| **Quer automação total** | `/jarvis-full` ✅ |
| Múltiplos arquivos | `/process-inbox --all --auto-enrich` |

---

## LOGS GERADOS

| Log | Localização |
|-----|-------------|
| INGEST REPORT | Exibido durante execução |
| EXECUTION REPORT | `/logs/EXECUTION/` |
| AGENT ENRICHMENT | Incluído no FULL PIPELINE REPORT |
| **FULL PIPELINE REPORT** | `/logs/FULL/FULL-{SOURCE_ID}-{TIMESTAMP}.md` |

---

## ERROS COMUNS

| Erro | Causa | Solução |
|------|-------|---------|
| "Pessoa não identificada" | URL sem metadata clara | Usar `--person "Nome"` |
| "Transcrição falhou" | Vídeo privado ou indisponível | Verificar URL, tentar local |
| "Source ID já existe" | Material já processado | Verificar `/inbox` ou forçar novo ID |

---

## CHANGELOG

| Versão | Data | Mudança |
|--------|------|---------|
| 1.2.0 | 2026-03-12 | Model routing por fase: Opus fases 3–6, Sonnet fases 1–2 e 7–8. Pause obrigatório nas transições. |
| 1.1.0 | 2025-12-20 | Integração automática com NARRATIVE-METABOLISM-PROTOCOL |
| 1.0.0 | 2025-12-19 | Criação inicial |
