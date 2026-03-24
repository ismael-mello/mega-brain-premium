> **Auto-Trigger:** When user asks to create a video, VSL, creative, ad, or presentation from agent output
> **Keywords:** "video", "vsl", "creative", "ad", "apresentação", "renderizar", "gerar video", "fazer video", "criar video", "video sales letter", "anúncio"
> **Prioridade:** ALTA
> **Tools:** Write, Bash, Read

# SKILL: Video Generator (Remotion)

Gera vídeos (VSL, Criativos, Apresentações) a partir de outputs de agentes do Mega Brain.

## Quando Ativar

- Usuário pede para criar um vídeo/VSL/creative
- Conclave ou agente produz output que deve virar vídeo
- Usuário quer transformar conhecimento do DNA em formato visual

## Quando NÃO Ativar

- Usuário quer apenas texto/copy (usar agente Copywriter)
- Discussão sobre estratégia de vídeo sem intenção de gerar
- Edição de vídeo existente (Remotion gera, não edita)

## Tipos de Vídeo Disponíveis

| Tipo | Composição | Dimensão | Uso |
|------|-----------|----------|-----|
| **VSL** | `VSL` | 1920x1080 | Video Sales Letter — hook, problem, solution, CTA |
| **Creative** | `Creative` | 1080x1080 | Ad criativo para redes sociais |
| **Presentation** | `Presentation` | 1920x1080 | Apresentação com slides (resumos, treinamentos) |

## Fluxo de Execução

### Passo 1: Coletar Conteúdo

Se o conteúdo vem de um agente/conclave, extrair:
- **Hook:** A frase de abertura que prende atenção
- **Problem:** O problema que o público enfrenta
- **Solution:** A solução proposta
- **Offer:** O que está sendo oferecido
- **CTA:** Call to action

Se o usuário pede diretamente, perguntar o tema e gerar o script.

### Passo 2: Criar JSON de Input

Criar arquivo JSON em `video/output/` com a estrutura:

```json
{
  "headline": "Título Principal",
  "subheadline": "Subtítulo opcional",
  "scenes": [
    { "type": "hook", "text": "E se você pudesse...", "duration": 120 },
    { "type": "problem", "text": "O problema é que...", "duration": 150 },
    { "type": "solution", "text": "A solução é...", "duration": 150 },
    { "type": "cta", "text": "Clique no botão abaixo", "duration": 90 }
  ],
  "brandColor": "#FF6B00",
  "backgroundColor": "#0A0A0A",
  "fontFamily": "Inter"
}
```

### Passo 3: Renderizar

```bash
cd video && node render.mjs --input output/scene-data.json --composition VSL --output output/meu-video.mp4
```

### Passo 4: Reportar

Mostrar ao usuário:
- Path do vídeo gerado
- Duração em segundos
- Composição usada

## Estrutura de Input por Tipo

### VSL (Video Sales Letter)

```json
{
  "headline": "Headline",
  "subheadline": "Sub",
  "scenes": [
    { "type": "hook", "text": "...", "duration": 120 },
    { "type": "problem", "text": "...", "duration": 150 },
    { "type": "agitate", "text": "...", "duration": 120 },
    { "type": "solution", "text": "...", "duration": 150 },
    { "type": "proof", "text": "...", "duration": 120 },
    { "type": "offer", "text": "...", "duration": 150 },
    { "type": "cta", "text": "...", "duration": 90 }
  ],
  "brandColor": "#FF6B00",
  "backgroundColor": "#0A0A0A"
}
```

Scene types: `hook`, `problem`, `agitate`, `solution`, `proof`, `offer`, `cta`, `custom`

### Creative (Ad Social)

```json
{
  "headline": "Headline do Ad",
  "body": "Corpo do texto",
  "ctaText": "Saiba Mais",
  "brandColor": "#FF6B00",
  "backgroundColor": "#0A0A0A",
  "style": "bold"
}
```

Styles: `bold`, `minimal`, `gradient`

### Presentation

```json
{
  "title": "Título da Apresentação",
  "subtitle": "Por Expert Name",
  "slides": [
    { "title": "Slide 1", "bullets": ["Ponto 1", "Ponto 2"], "duration": 150 },
    { "title": "Slide 2", "bullets": ["Ponto A", "Ponto B"], "duration": 150 }
  ],
  "brandColor": "#FF6B00",
  "closingText": "Obrigado!"
}
```

## Integração com Agentes

Quando um agente do conclave ou cargo produz output que deve virar vídeo:

1. Extrair conteúdo estruturado do output do agente
2. Mapear para o tipo de vídeo adequado (VSL se tem hook/problem/solution, Presentation se tem bullets/slides)
3. Usar `agent-to-video.ts` como referência para o mapeamento
4. Gerar JSON → Renderizar → Entregar

## Pré-requisitos

O módulo precisa de `npm install` na primeira vez:

```bash
cd video && npm install
```

Remotion inclui FFmpeg automaticamente — sem dependências externas.

## Development Studio

Para preview e edição visual dos templates:

```bash
cd video && npx remotion studio src/index.ts
```

Abre um browser com preview interativo de todas as composições.

## Output

Vídeos são salvos em `video/output/` (gitignored).
