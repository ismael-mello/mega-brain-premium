# HANDOFF: Dan Kennedy — Make Them Buy Now (MTBN)
# Phases 1-2 COMPLETE → Aguardando OPUS para Phases 3-6

> **Data:** 2026-03-15
> **Status:** PAUSED — Troca de modelo necessária
> **Contexto:** /jarvis-full inbox yolo mode

---

## ⚠️ REGRA MÁXIMA — TROCA DE MODELO OBRIGATÓRIA

```
┌────────────────────────────────────────────────────────────────────────┐
│ ⚠️ TROCA DE MODELO NECESSÁRIA                                          │
│ A próxima fase requer: OPUS                                            │
│ Modelo atual: claude-sonnet-4-6                                        │
│ Use /model para trocar. Como deseja prosseguir?                        │
│ → [1] Vou trocar agora  → [2] Continuar em Sonnet (qualidade reduzida) │
└────────────────────────────────────────────────────────────────────────┘
```

---

## O Que Foi Feito

### ✅ Phase 1: Initialization
- 89 arquivos movidos para `knowledge/external/sources/dan-kennedy/raw/make-them-buy-now/`
- Source ID definido: **MTBN**

### ✅ Phase 2: Chunking
- 78 arquivos com conteúdo real identificados
- 11 placeholders identificados (skip — apenas page numbers)
- 14 batches definidos
- `knowledge/external/sources/dan-kennedy/SOURCE-MTBN.md` criado

### ⏳ Inbox original ainda presente
- `inbox/Dan Kennedy - Make them buy now/` → pode ser removido após confirmar raw ok

---

## DK DNA State (antes do MTBN)

- **Total elementos:** 1750 (v22.0.0)
- **Next IDs:**
  - FIL-DK-409 (Philosophies)
  - MM-DK-349 (Mental Models)
  - HEUR-DK-507 (Heuristics)
  - FW-DK-293 (Frameworks)
  - MET-DK-206 (Methodologies)
- **DNA file:** `knowledge/external/dna/persons/dan-kennedy/DNA.yaml` (565KB)

---

## Batch Plan (14 batches para OPUS processar)

| Batch | Files | Sub-program | DNA Focus |
|-------|-------|-------------|-----------|
| BATCH-MTBN-01 | 4 | One To Many Selling (Audio CD1-4) | FW, MET |
| BATCH-MTBN-02 | 4 | Selling One To Many (Video 1-4) | FW, MET |
| BATCH-MTBN-03 | 5 | PDFs One to Many (Modules 1-4 + Manual) | FW, MET |
| BATCH-MTBN-04 | 10 | Secrets (Audio CD1-5 + Video 1-5) | FW, HEUR |
| BATCH-MTBN-05 | 5 | PDFs Secrets Modules 1-5 | FW, MET |
| BATCH-MTBN-06 | 6 | Sorcery (Audio+Video+PDFs Sorcery) | FIL, FW |
| BATCH-MTBN-07 | 7 | PDFs System (System1-3, System8-9, Exhibits) | HEUR, FW |
| BATCH-MTBN-08 | 4 | Bonus 1 - Marketing to Affluent | FIL, MM, HEUR |
| BATCH-MTBN-09 | 4 | Bonus 2 - Time Management | FIL, HEUR |
| BATCH-MTBN-10 | 6 | Bonus 3+4 - Sales Assets + Operations | FW, HEUR |
| BATCH-MTBN-11 | 5 | Bonus 5 - Cart Closing (Guest Speakers) | HEUR (attributed) |
| BATCH-MTBN-12 | 6 | Bonus 6 - Magnetic Marketing 2014 | FIL, MM, FW |
| BATCH-MTBN-13 | 8 | Bonus 8 - Lords of List Building | FW, HEUR, MET |
| BATCH-MTBN-14 | 5 | Bonus 9 - Cash Flow Surge + Ask Experts | HEUR, FW |

### Arquivos a SKIP (placeholders):
- System4Bullets, System5Offers, System10Testimonials, System11CallToAction
- System12Templates, System13OrderForms, System14Checklist
- System6Objections, System7Guarantees (< 500 bytes)
- Four_Day_Cash_Machine_by_Frank_Kern.txt (336 bytes)
- SorceryExhibits13-25.txt (591 bytes)

---

## Instrução para OPUS

### Processo por batch:
1. Ler todos os arquivos do batch
2. Extrair elementos DNA:
   - **FIL-DK-XXX**: Philosophies/beliefs sobre marketing, copy, vendas
   - **MM-DK-XXX**: Mental models, frameworks cognitivos
   - **HEUR-DK-XXX**: Heurísticas práticas, regras de decisão com números
   - **FW-DK-XXX**: Frameworks estruturados, processos
   - **MET-DK-XXX**: Metodologias step-by-step
3. Salvar como YAML em `knowledge/external/sources/dan-kennedy/mtbn-extraction/BATCH-MTBN-XX.yaml`
4. Atualizar next IDs após cada batch
5. Ao final: consolidar todos em DNA.yaml

### Formato YAML (igual ao OMC extraction):
```yaml
batch: "MTBN-01"
program: "One To Many Selling"
extraction_date: "2026-03-15"
elements:
  L1_PHILOSOPHIES:
    - id: "FIL-DK-409"
      text: "..."
      source: "MTBN-OTM-CD1"
  L2_MENTAL_MODELS: []
  L3_HEURISTICS: []
  L4_FRAMEWORKS: []
  L5_METHODOLOGIES: []
```

### Temas principais esperados:
1. **One-to-Many / Platform Selling** — arquitetura de apresentação em grupo
2. **Direct Response Copywriting** — headlines, bullets, USP, openings, CTAs
3. **Sales Psychology** — mind control, persuasão, storytelling em copy
4. **Affluent Marketing** — vendendo para mercado premium/HNW
5. **Magnetic Marketing** — geração de leads, atração (versão 2014)
6. **List Building** — direct mail, email, multi-medium
7. **Cash Flow** — táticas de revenue surge imediato
8. **Time Leverage** — filosofia de gestão de tempo No B.S.

---

## Próximos Passos (após OPUS)

1. Phases 3-6 (OPUS): Extrair DNA dos 14 batches → ~200-400 novos elementos
2. Phase 7 (SONNET): Enriquecer cargo agents (CMO copy, CRO platform selling)
3. Phase 8 (SONNET): Atualizar AGENT.md, MEMORY.md, SOUL.md do DK agent
4. Limpar inbox: remover `inbox/Dan Kennedy - Make them buy now/`
5. Commit: `feat(dk): MTBN extraction — ~300 new DNA elements`

---

## Raw Files Location
```
knowledge/external/sources/dan-kennedy/raw/make-them-buy-now/
├── Make Them Buy Now/
│   ├── Bonuses/ (5 bonus folders)
│   ├── One To Many Selling/ (CD1-4)
│   ├── PDFs/ (modules + system)
│   ├── Secrets/ (CD1-5 + mp4 1-5)
│   ├── Selling One To Many/ (mp4 1-4)
│   └── Sorcery/ (CD1-2 + mp4 1-2)
└── More Bonuses/
    ├── 6 Magnetic Marketing 2014/ (mp4 1-5 + PDF)
    ├── 7 Ask the Experts/ (Make Them Say Yes PDF)
    ├── 8 Lords of List Building/ (mp3 1-5 + 2 PDFs)
    └── 9 Cash Flow Surge Generator/ (mp3+mp4+3 PDFs)
```
