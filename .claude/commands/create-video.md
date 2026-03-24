---
description: Cria vídeo (VSL, Creative, Apresentação) a partir de briefing ou output de agente
argument-hint: [tipo] --tema "..." [--expert "..."] [--style bold|minimal|gradient]
---

# /create-video — Gerador de Vídeo (Remotion)

> **Versão:** 1.0.0
> **Módulo:** `video/`
> **Agentes:** Video Creator + Video Editor
> **Output:** `video/output/*.mp4`

---

## SINTAXE

```
/create-video [tipo] --tema "..." [--expert "..."] [--style bold|minimal|gradient]
```

| Flag | Descrição | Obrigatório |
|------|-----------|-------------|
| `tipo` | `vsl`, `creative`, `presentation` | Sim |
| `--tema` | Tema/assunto do vídeo | Sim |
| `--expert` | Expert do DNA a usar como fonte | Não |
| `--style` | Estilo visual (creative only) | Não |
| `--brand-color` | Cor principal (hex) | Não (default: #FF6B00) |
| `--duration` | Duração alvo em segundos | Não (auto-calculado) |

---

## EXEMPLOS

```bash
# VSL sobre oferta irresistível baseado em Hormozi
/create-video vsl --tema "Grand Slam Offer" --expert "Alex Hormozi"

# Criativo para ad de Meta
/create-video creative --tema "Agende sua sessão estratégica" --style bold

# Apresentação do DNA de Cole Gordon
/create-video presentation --tema "Framework de Vendas High-Ticket" --expert "Cole Gordon"

# VSL sem expert específico (usa DNA geral)
/create-video vsl --tema "Como dobrar seu faturamento em 90 dias"
```

---

## FLUXO DE EXECUÇÃO

Ao receber `/create-video`, JARVIS deve:

### FASE 1: ATIVAR VIDEO CREATOR

```
1. Carregar AGENT.md do Video Creator:
   agents/cargo/content/video-creator/AGENT.md

2. Carregar SOUL.md:
   agents/cargo/content/video-creator/SOUL.md

3. Carregar DNA-CONFIG.yaml:
   agents/cargo/content/video-creator/DNA-CONFIG.yaml
```

### FASE 2: GERAR CONTEÚDO

```
SE --expert fornecido:
   → Carregar DNA do expert especificado
   → Extrair conteúdo relevante para o tema
   → Estruturar usando frameworks do expert

SE --expert NÃO fornecido:
   → Usar AGGs relevantes ao tema
   → Combinar múltiplas fontes

PARA tipo = vsl:
   → Gerar: hook, problem, agitate, solution, proof, offer, cta
   → Cada cena com texto impactante (max 2 linhas)
   → Duration: 90-150 frames por cena (3-5s)

PARA tipo = creative:
   → Gerar: headline, body, ctaText
   → Headline: max 8 palavras
   → Body: max 20 palavras
   → CTA: max 3 palavras

PARA tipo = presentation:
   → Gerar: title, subtitle, slides[]
   → Cada slide: title + 3-5 bullets
   → Duration: 150 frames por slide (5s)
```

### FASE 3: CRIAR JSON

```
1. Estruturar dados no formato esperado pelo Remotion
2. Salvar JSON em: video/output/[tipo]-[tema-kebab]-[timestamp].json
3. MOSTRAR o JSON no chat para aprovação
```

### FASE 4: RENDERIZAR

```
APÓS aprovação do usuário:

cd video && node render.mjs \
  --input output/[arquivo].json \
  --composition [VSL|Creative|Presentation] \
  --output output/[arquivo].mp4

Mostrar progresso de renderização no chat.
```

### FASE 5: ENTREGA

```
1. Reportar:
   - Path do vídeo: video/output/[arquivo].mp4
   - Duração: Xs
   - Tamanho: X.XMB
   - Composição usada

2. Perguntar:
   - "Quer que o Video Editor crie variações?"
   - "Quer ajustar timing ou conteúdo?"
   - "Quer versão para outro formato (reels, stories)?"
```

---

## FLUXO VISUAL

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  /create-video vsl --tema "X" --expert "Y"                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐                │
│  │ VIDEO CREATOR │ ──→ │   JSON DATA  │ ──→ │   REMOTION   │               │
│  │               │     │              │     │              │               │
│  │ • Carrega DNA │     │ • scenes[]   │     │ • Bundle     │               │
│  │ • Gera script │     │ • branding   │     │ • Compose    │               │
│  │ • Estrutura   │     │ • timing     │     │ • Render     │               │
│  └──────────────┘     └──────────────┘     └──────┬───────┘               │
│                                                     │                      │
│                                              ┌──────▼───────┐              │
│                                              │    MP4 FILE   │              │
│                                              │               │              │
│                                              │ video/output/ │              │
│                                              └──────┬───────┘              │
│                                                     │                      │
│                              ┌───────────────────────┘                      │
│                              │                                              │
│                       ┌──────▼───────┐                                      │
│                       │ VIDEO EDITOR │  (opcional)                          │
│                       │              │                                      │
│                       │ • Variações  │                                      │
│                       │ • A/B hooks  │                                      │
│                       │ • Formatos   │                                      │
│                       └──────────────┘                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## COMPOSIÇÕES DISPONÍVEIS

| Tipo | Composição | Dimensão | Duração Default | Scenes |
|------|-----------|----------|-----------------|--------|
| `vsl` | VSL | 1920x1080 | 30-120s | hook, problem, agitate, solution, proof, offer, cta |
| `creative` | Creative | 1080x1080 | 15s | headline, body, cta (tela única animada) |
| `presentation` | Presentation | 1920x1080 | 30-180s | title slide + N content slides |

---

## PRÉ-REQUISITOS

Na primeira vez, instalar dependências:

```bash
cd video && npm install
```

Remotion inclui Chrome Headless Shell e FFmpeg automaticamente.

---

## INTEGRAÇÃO COM CONCLAVE

Quando o Conclave produz um output deliberativo que deve virar vídeo:

```
/conclave "Como estruturar nossa oferta high-ticket?"
    │
    ▼ (output do conselho)
    │
/create-video vsl --tema "Oferta High-Ticket" --expert "Alex Hormozi"
    │
    ▼ (usa output do conclave + DNA do expert)
    │
   MP4 renderizado
```

O Video Creator DEVE usar o output do conclave como base de conteúdo, enriquecido pelo DNA do expert especificado.

---

## NOTAS

- Vídeos são salvos em `video/output/` (gitignored — arquivos grandes)
- JSON sources são mantidos para re-renderização futura
- Use `npx remotion studio src/index.ts` (dentro de `video/`) para preview visual
- Cada composição aceita props customizáveis via JSON
