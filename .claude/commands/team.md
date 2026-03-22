---
description: Diagnostic multi-agent por equipe - todos os agents da equipe relevante respondem sua pergunta
argument-hint: [pergunta] - Ex: "Minha campanha caiu 30% em 3 dias. O que fazer?"
---

# /team - Diagnostic Multi-Agent por Equipe

## Descricao

Roteia sua pergunta para TODOS os cargo agents da equipe relevante.
Cada agent responde da sua perspectiva usando seu DNA.
Resultado: N diagnosticos especializados + 1 plano de acao consolidado.

## Uso
```
/team [pergunta]
/team [equipe] [pergunta]
```

## Exemplos
```
/team "Minha campanha caiu 30% em 3 dias. O que fazer?"
/team vendas "Meu closer ta fechando 12%. Normal?"
/team copywriting "Preciso de uma headline pro meu webinar"
```

---

## INSTRUCOES DE EXECUCAO

### Passo 1: DETECTAR EQUIPE

Se o usuario especificou equipe, usar diretamente.
Se nao, classificar a pergunta por dominio usando estas keywords:

| Keywords na Pergunta | Equipe |
|---------------------|--------|
| campanha, ads, anuncio, trafego, custo por lead, CPL, CPM, ROAS, criativo, escalar | **traffic** |
| vender, fechar, closer, objecao, call, pipeline, meta, comissao, SDR, prospect | **vendas** |
| copy, headline, email, carta, texto, persuasao, gancho, lead magnet | **copywriting** |
| oferta, preco, pricing, valor, stack, garantia, irresistivel | **offers** |
| outbound, cold call, cadencia, prospectar, lista | **outbound** |
| historia, storytelling, narrativa, origem, hook | **storytelling** |
| lideranca, time, equipe, gestao, cultura, contratar | **executive-leadership** |
| financeiro, margem, caixa, cash flow, LTV, CAC, unit economics | **gestao-financeira** |

Se ambiguo, usar TOP 2 equipes mais relevantes.

### Passo 2: MAPEAR AGENTS DA EQUIPE

| Equipe | Agents (em ordem de prioridade) |
|--------|---------------------------------|
| **vendas** | `sales/closer`, `sales/sdr`, `sales/sales-manager`, `c-level/cro` |
| **traffic** | `marketing/media-buyer`, `marketing/paid-media-specialist`, `c-level/cmo` |
| **copywriting** | `marketing/copywriter`, `c-level/cmo` |
| **offers** | `c-level/cro`, `c-level/cmo`, `sales/closer` |
| **outbound** | `sales/sdr`, `sales/sales-manager`, `c-level/cro` |
| **storytelling** | `marketing/copywriter`, `c-level/cmo` |
| **executive-leadership** | `c-level/cro`, `c-level/cfo`, `c-level/cmo`, `c-level/coo` |
| **gestao-financeira** | `c-level/cfo` |

### Passo 3: CARREGAR CADA AGENT (em paralelo)

Para CADA agent da equipe, usar Agent tool em paralelo:

```
Para cada cargo agent:
1. Ler agents/cargo/{nivel}/{slug}/DNA-CONFIG.yaml
2. Ler agents/cargo/{nivel}/{slug}/MEMORY.md
3. Ler agents/cargo/{nivel}/{slug}/SOUL.md (se existir)
4. Identificar AGG relevante: knowledge/external/dna/aggregated/AGG-{DOMINIO}.yaml
5. Carregar heuristicas e frameworks do AGG que matcham a pergunta
```

### Passo 4: GERAR DIAGNOSTICO DE CADA AGENT

Cada agent responde INDIVIDUALMENTE seguindo o formato:

```
[ICONE] @[slug] ([nome]):
"[Diagnostico de 2-4 frases usando DNA do agent]
 [Citacao de framework/heuristica especifica]
 [Recomendacao concreta]"
```

REGRAS:
- Cada agent responde da SUA perspectiva (nao repete os outros)
- Cada resposta DEVE citar pelo menos 1 framework/heuristica do DNA
- Tom deve refletir o SOUL.md do agent
- Maximo 5 linhas por agent

### Passo 5: CONSOLIDAR PLANO DE ACAO

Apos todos os diagnosticos, sintetizar:

```
┌─────────────────────────────────────────────────────────┐
│  PLANO DE ACAO CONSOLIDADO                              │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  DIAGNOSTICO: [Resumo em 1 frase]                       │
│                                                         │
│  ACOES IMEDIATAS:                                       │
│  1. [Acao mais urgente - de qual agent veio]            │
│  2. [Segunda acao - de qual agent veio]                 │
│  3. [Terceira acao - de qual agent veio]                │
│                                                         │
│  CONSENSO: [N] de [N] agents concordam em [X]           │
│  DIVERGENCIAS: [Se houver, listar]                      │
│                                                         │
│  CONFIANCA: [0-100]%                                    │
│  FONTES: [IDs dos frameworks/heuristicas usados]        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Passo 6: FORMATO FINAL NO CHAT

```
╔══════════════════════════════════════════════════════════╗
║  TEAM DIAGNOSTIC: [NOME DA EQUIPE]                      ║
║  [N] agents  ·  [M] frameworks aplicados                ║
╚══════════════════════════════════════════════════════════╝

  [ICONE] @agent-1 ([Nome]):
  "[Diagnostico...]"

  [ICONE] @agent-2 ([Nome]):
  "[Diagnostico...]"

  [ICONE] @agent-3 ([Nome]):
  "[Diagnostico...]"

  [ICONE] @agent-4 ([Nome]):
  "[Diagnostico...]"

┌─────────────────────────────────────────────────────────┐
│  PLANO DE ACAO CONSOLIDADO                              │
│  ...                                                    │
└─────────────────────────────────────────────────────────┘

[N] agents. [N] diagnosticos. 1 plano de acao.
```

---

## ICONES POR CARGO

| Cargo | Icone | Archetype |
|-------|-------|-----------|
| CRO | 📈 | Revenue Strategist |
| CFO | 💵 | Financial Guardian |
| CMO | 📣 | Marketing Strategist |
| COO | ⚙️ | Operations Chief |
| Closer | 🤝 | Deal Closer |
| SDR | 📞 | Prospector |
| Sales Manager | 🎯 | Pipeline Manager |
| Media Buyer | 💰 | Ad Operator |
| Paid Media Specialist | 🎬 | Creative Strategist |
| Copywriter | ✍️ | Word Architect |

---

## NOTAS

- Usa Agent tool para disparar consultas em PARALELO (nao sequencial)
- Se agent nao tem DNA-CONFIG.yaml, usar apenas AGG do dominio
- Se agent scaffold (status SCAFFOLD), avisar que precisa enriquecimento
- Maximo 6 agents por diagnostic (se equipe tem mais, priorizar top 6)
- Se pergunta cruza 2 equipes, incluir agents de ambas (max 6 total)
