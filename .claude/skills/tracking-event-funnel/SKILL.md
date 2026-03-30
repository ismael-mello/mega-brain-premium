> **Auto-Trigger:** Quando usuário perguntar sobre tracking, pixel, API de conversão, funil de eventos, atribuição, Advanced Matching, configuração de eventos do Facebook/Meta, otimização de pixel, qualidade de eventos, nota do pixel, campanha de controle, campanha extendida, funil invertido, diagnóstico de relevância, server-side tracking, connect rate, otimização de campanhas Meta
> **Keywords:** "tracking", "pixel", "api de conversão", "funil de eventos", "event funnel", "atribuição", "advanced matching", "qualidade de eventos", "nota do pixel", "configurar eventos", "page view", "initiate checkout", "purchase event", "subscribe event", "CAPI", "conversion API", "server-side tracking", "connect rate", "80-10-10", "campanha de controle", "campanha extendida", "funil invertido", "diagnóstico de relevância", "otimização relâmpago", "GTM server", "traqueamento", "ACTWACLIB", "WhatsApp tracking"
> **Prioridade:** ALTA
> **Tools:** Read, Grep, Glob

## Quando NÃO Ativar
- Quando a pergunta for sobre criativos ou copy de anúncios
- Quando for sobre criação de BM (ver skill bm-shield)
- Quando for sobre Google Ads (esta skill é focada em Meta/Facebook)
- Quando for sobre oferta/produto (sem relação com tracking ou campanha)

---

# SKILL: Meta Ads — Tracking, Campanhas & Otimização

## Propósito

Guia completo para tracking avançado, campanha de controle, extensão de campanhas e otimização no Meta/Facebook Ads. Baseado na metodologia de **Lúcio Artes** (13 cursos, 501 elementos DNA) complementada por Cat Howell, Frank Kern e Jeremy Haynes.

## Conceito Central

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║  "Qualidade do evento é mais importante que quantidade."                     ║
║                                     — Lúcio Artes                            ║
║                                                                              ║
║  O PIXEL SOZINHO = 40-60% de atribuição (pode cair para 15%)                ║
║  PIXEL + API DE CONVERSÃO + ADVANCED MATCH = 90% de atribuição              ║
║  NOTA MÁXIMA WEB = 9.3/10 (10 só com SDK de app)                            ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Analogia da Ferrari (Framework Mestre)

A plataforma de anúncios é uma Ferrari. Para performar precisa de 3 elementos:

| Elemento | Significado | O Que Fazer |
|----------|-------------|-------------|
| **COMBUSTÍVEL** | Qualidade dos eventos/dados | API de conversão, Advanced Match, funil completo |
| **ESTRADA** | Infraestrutura de conversão | Site rápido (PageSpeed > 90), checkout otimizado |
| **PILOTO** | Estratégia do anunciante | Bid strategy correta, paciência, conhecimento |

**Se faltar qualquer um dos 3, não escala.**

## Hierarquia Completa de Eventos (Meta/Facebook)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  HIERARQUIA DE EVENTOS — DO MENOR PARA O MAIOR VALOR                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. PageView          → Visitou a página (automático)                       │
│  2. Search / Scroll   → Interagiu com a página (scroll 50%+)               │
│  3. ViewContent       → Viu a oferta / conteúdo principal                   │
│  4. AddToWishlist     → Clicou no botão de interesse / CTA                  │
│  5. Contact           → Iniciou contato (WhatsApp, formulário)              │
│  6. Lead              → Preencheu formulário / captura de dados              │
│  7. AddToCart         → Visitou o checkout                                   │
│  8. InitiateCheckout  → Preencheu dados pessoais no checkout                │
│  9. AddPaymentInfo    → Selecionou forma de pagamento                       │
│  10. Purchase         → Pagou (cartão, PIX confirmado)                      │
│  11. Subscribe        → Assinou (com predicted_ltv)                         │
│                                                                             │
│  ⚠️ REGRA: Quanto mais eventos intermediários, MAIS RÁPIDO o sistema        │
│     calibra. É como dar mais referências ao sniper para acertar o alvo.     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Funil Duplo: Página + Checkout

Todo funil online tem **dois funis encadeados**:

### Funil 1: Página de Vendas
```
PageView → Scroll 50% → ViewContent (viu oferta) → AddToWishlist (clicou CTA)
```

### Funil 2: Checkout
```
AddToCart (visitou checkout) → InitiateCheckout (preencheu dados) → AddPaymentInfo → Purchase
```

**IMPORTANTE:** Disparar `InitiateCheckout` SOMENTE quando o lead **preenche os dados**, não quando visita o checkout. Isso aumenta a nota de atribuição.

## Configuração da API de Conversão

### Por que API + Pixel (e não só Pixel)

| Cenário | Atribuição |
|---------|------------|
| Só Pixel (browser-side) | 40-60% (caindo para 15% com iOS14+) |
| Pixel + API de Conversão | ~85% |
| Pixel + API + Advanced Match Manual | ~90% |
| App com SDK nativo | Até 100% (nota 10) |

### Advanced Match — Campos Obrigatórios

| Campo | Prioridade | O Que Envia |
|-------|-----------|-------------|
| Email | ALTA | email do lead/comprador |
| Telefone | ALTA | com código do país (+55) |
| Nome | MÉDIA | primeiro nome |
| Sobrenome | MÉDIA | último nome |
| Cidade | BAIXA | cidade do lead |
| Estado | BAIXA | UF |
| CEP | BAIXA | código postal |
| Data Nascimento | BAIXA | se disponível |

**Enviar MANUALMENTE** via código, não confiar no Auto Advanced Match do Facebook.

## Princípio 80-10-10 (Validação de Funil)

Antes de escalar, validar:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  MÉTRICAS MÍNIMAS PARA ESCALAR                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Connect Rate (cliques → visitas):      ≥ 80%                              │
│  Conversão LP (visitas → checkout):     ≥ 10%                              │
│  Conversão Checkout (checkout → compra): ≥ 10%                              │
│  Conversão Global (visitas → compra):   ≥ 1%                               │
│                                                                             │
│  SE QUALQUER MÉTRICA ABAIXO DO MÍNIMO → NÃO ESCALE → RESOLVA PRIMEIRO     │
│                                                                             │
│  DIAGNÓSTICO:                                                               │
│  • Connect Rate < 80% → Problema de INFRAESTRUTURA (site lento, servidor)  │
│  • Conv LP < 10% → Problema de PÁGINA (copy, oferta, design)               │
│  • Conv Checkout < 10% → Problema de CHECKOUT (UX, preço, confiança)       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Métricas Customizadas (Criar no Gerenciador)

O Facebook NÃO fornece essas métricas nativamente. Criar manualmente:

| Métrica | Fórmula | Tipo |
|---------|---------|------|
| Connect Rate | Visualização Página Destino / Cliques no Link | Percentual |
| Conversão LP | Finalizações Iniciadas / Visualização Página Destino | Percentual |
| Conversão Checkout | Compras / Finalizações Iniciadas | Percentual |
| Lucro R$ | Valor Conversão Compra - Valor Usado | Moeda |
| Lucro % | (Valor Conversão - Usado) / Usado | Percentual |
| Conversão Global | Compras / Visualização Página Destino | Percentual |

## Otimização de PIX (Específico Brasil)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  REGRA DO PIX OTIMIZADO                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Cartão de crédito → Enviar evento Purchase com VALOR CHEIO (100%)         │
│  PIX pago → Enviar evento Purchase com VALOR PROPORCIONAL                   │
│                                                                             │
│  Exemplo: Produto R$100, taxa de conversão PIX = 60%                        │
│  • Cartão: Purchase value = R$100                                           │
│  • PIX: Purchase value = R$100 × 0.60 = R$60                               │
│                                                                             │
│  POR QUÊ: O Facebook prioriza público que gera MAIS VALOR.                 │
│  Com valor proporcional, o algoritmo busca:                                 │
│  1. Compradores de cartão (valor cheio = mais valioso)                      │
│  2. Pagadores de PIX (valor proporcional = segundo mais valioso)            │
│  3. Ignora geradores de PIX que não pagam                                   │
│                                                                             │
│  CONFIGURAÇÃO: Na plataforma de pagamento → Configuração do pixel →         │
│  "Enviar todos os métodos de pagamento" → Definir valor por método          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Subscribe vs Purchase (Recorrência)

Para produtos de **assinatura/recorrência**, usar `Subscribe` em vez de `Purchase`:

| Aspecto | Purchase | Subscribe |
|---------|----------|-----------|
| Valor enviado | Valor da primeira compra | predicted_ltv (valor total estimado) |
| Otimização | Busca quem compra | Busca quem compra E fica |
| Exemplo | R$100 (1ª mensalidade) | R$600 (R$100 × 6 meses estimados) |
| Resultado | Mais compradores, mais churn | Menos compradores, mais retenção |

## Heurísticas Numéricas de Tracking

| Heurística | Valor | Fonte |
|-----------|-------|-------|
| Pixel sozinho (atribuição) | 40-60% | FIL-LA-006 |
| Pixel + API + AM (atribuição) | ~90% | FIL-LA-006 |
| Nota máxima web | 9.3/10 | HEUR-LA-210 |
| Nota máxima app | 10/10 | HEUR-LA-210 |
| Redução de CPL com API (caso real) | R$12 → R$1,80 (-85%) | HEUR-LA-207 |
| Tempo para performance máxima da API | 21 dias (3 janelas de 7d) | HEUR-LA-208 |
| Variação aceitável gerenciador vs CRM | ≤ 20% | HEUR-LA-217 |
| Conversões para desbloquear Valor | 30 + 2 valores distintos | HEUR-LA-023 |

## Fontes do Mega Brain

| Expert | Contribuição para Tracking | DNA Path |
|--------|---------------------------|----------|
| **Lúcio Artes** (PRIMARY) | Funil de eventos completo, API de conversão, 80-10-10, PIX otimizado, métricas customizadas | knowledge/external/dna/persons/lucio-artes/ |
| Cat Howell | Attribution Window Analysis, OCPM/CPM Selection Matrix | knowledge/external/dna/persons/cat-howell/ |
| Frank Kern | Hyros integration, multi-platform attribution, automation rules | knowledge/external/dna/persons/frank-kern/ |
| Jeremy Haynes | ConnectIO Suite, Facebook Rules Automation | knowledge/external/dna/persons/jeremy-haynes/ |

## Checklist de Implementação de Tracking

```
□ 1. Instalar pixel do Facebook na página
□ 2. Configurar API de Conversão (server-side)
□ 3. Implementar Advanced Match MANUAL (email, telefone, nome)
□ 4. Criar funil de eventos completo na página (PV → Scroll → VC → AW)
□ 5. Criar funil de eventos no checkout (ATC → IC após dados → API → Purchase)
□ 6. Configurar evento Subscribe para assinaturas (com predicted_ltv)
□ 7. Configurar PIX otimizado (valor proporcional à taxa de conversão)
□ 8. Desabilitar pixel da plataforma de pagamento (usar apenas o seu)
□ 9. Testar TODOS os eventos no Event Test do Facebook
□ 10. Criar métricas customizadas no gerenciador
□ 11. Validar com Princípio 80-10-10 após 300-500 visitas
□ 12. Aguardar 21 dias para performance máxima da API
```

---

## CAMPANHA DE CONTROLE (Método Lúcio Artes)

### O Que É

Campanha de Controle é um conceito estatístico. O objetivo NÃO é testar (A vs B). É **validar uma hipótese** ("esse produto vai vender para esse público"). Somente após ter parâmetros de controle é que se fazem testes.

### Estrutura Exata — Configurações no Gerenciador

**Nível Campanha:**
- Objetivo: **Vendas** (manual, NÃO Advantage+)
- Orçamento Advantage: **DESLIGADO** (usar ABO, orçamento no conjunto)
- Estratégia de lance: **Maximizar Conversões** (produzir números, não controlar CPA)

**Nível Conjunto (3 conjuntos, nunca mais que 5):**
- Orçamento: **TOTAL** (NÃO diário)
- Prazo: **7 dias** (início imediato, término em 7 dias)
- Cálculo: R$6/anúncio/dia × qtd anúncios × 7 dias
  - Ex: 3 anúncios × R$6 × 7 = R$126/conjunto → 3 conjuntos = **R$378 total**

**Nível Anúncio (3 por conjunto, nunca mais que 5):**
- NÃO misturar imagem e vídeo no mesmo conjunto
- Conjunto de imagem separado do conjunto de vídeo

### Variação de Segmentação (3 Conjuntos)

| Conjunto | Segmentação | Quando Usar |
|----------|-------------|-------------|
| **1** | Aberto + Advantage | Deixar Meta decidir |
| **2** | Segmentado (empilhamento de interesses) | Testar hipótese de público |
| **3** | Interesse + Advantage OU Público Personalizado | Combinar |

### Por Que Orçamento TOTAL (Não Diário)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ORÇAMENTO DIÁRIO (RUIM):                                                   │
│  • Obriga o Facebook a gastar TODO o orçamento todo dia                    │
│  • Desde abril/2024, pode ultrapassar em ATÉ 75% o orçamento diário       │
│  • Diário + Maximizar Conversões = gastar sem controle                     │
│                                                                             │
│  ORÇAMENTO TOTAL (CORRETO):                                                │
│  • Facebook gasta MAIS nos dias bons, MENOS nos ruins                      │
│  • Respeita sazonalidade de cada dia da semana                             │
│  • Permite aprender qual dia/horário converte melhor                       │
│  • NÃO ultrapassa o total definido                                         │
│                                                                             │
│  Fonte: Documentação oficial Meta                                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Sistema de Otimização D-Menos

| Dia | O que acontece | Ação |
|-----|---------------|------|
| D1 (D0) | ZERO otimização. Pura entrega baseada em segmentação | NÃO FAÇA NADA |
| D2 | Pega dados D1. Leve variação | Observe |
| D3 | Convergência começa | Observe |
| **D4** | **DIA CHAVE.** Metade da janela. Dados suficientes | **DECISÃO: continuar ou parar** |
| D5-7 | Estabilização | Avaliar 80-10-10 |
| Semana 2 | Oscila menos | Maturação |
| **Semana 3** | **Geralmente MELHOR resultado** | Considerar extensão |
| Semana 4 | Campanha madura | Estável |

**Caso real:** Lead de R$12 → R$3,42 (sem1) → R$1,82 (sem3) → R$2,80 estável após 7 meses com R$500K+ investidos.

### Dicas de Otimização de Connect Rate

Se Connect Rate < 80%, ANTES de gastar mais:

1. **Somente Wi-Fi:** Conjunto → Posicionamento → Somente Wi-Fi (operadoras BR dão pacote grátis de redes sociais mas sem dados web)
2. **Android 11/12+:** Filtrar versões mais recentes (melhor poder aquisitivo)
3. **Remover Tablet:** Desmarcar (maioria é criança)
4. **Remover posicionamentos:** Tirar Messenger, Audience Network, coluna Desktop

### UTMs Dinâmicos nos Anúncios

Na configuração do anúncio, seção de parâmetros de URL (NÃO na URL principal):

```
utm_source = meta
utm_medium = {{adset.name}}
utm_campaign = {{campaign.name}}
utm_content = {{ad.name}}
src = {{placement}}
sck = {{site_source_name}}
```

### O Que NÃO Fazer

- ❌ 20 criativos e 40 conjuntos no primeiro teste
- ❌ CPM como KPI para fundo de funil
- ❌ Parar campanha no dia 3 por oscilação
- ❌ Escalar com Maximizar Conversões (doc Meta: "No cost control")
- ❌ Clonar campanhas de R$10/dia infinitamente
- ❌ Se preocupar com horário de subir (Facebook calcula proporcional)
- ❌ Conjuntos com tamanhos de público muito diferentes em CBO (máx 15-20% diferença)

---

## CAMPANHA EXTENDIDA (Como Estender Sem Resetar)

### Quando Aplicar

No **4º dia** da campanha de controle, avaliar 80-10-10. Se métricas boas → estender.

### Passo a Passo

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  COMO ESTENDER SEM VOLTAR AO APRENDIZADO                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. Calcular média diária: Orçamento Total / Dias                          │
│     Ex: R$2.100 / 7 = R$300/dia                                            │
│                                                                             │
│  2. Definir novo prazo (ex: 90 dias a partir do início)                    │
│                                                                             │
│  3. Calcular novo orçamento: Novo prazo × média diária                     │
│     Ex: 90 × R$300 = R$27.000                                              │
│                                                                             │
│  4. Alterar SIMULTANEAMENTE prazo E orçamento → Publicar                   │
│     (se fizer separado, volta ao aprendizado!)                             │
│                                                                             │
│  5. Verificar: status deve continuar "Ativo" (não "Aprendizado")           │
│                                                                             │
│  ⚠️ REGRA: Isso NÃO é escalar — é manter o investimento diário            │
│     constante por mais tempo. A plataforma continua aprendendo             │
│     sazonalidade dos dias, semanas e meses.                                │
│                                                                             │
│  "Quanto mais tempo roda, mais inteligente fica."                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## FUNIL INVERTIDO (Método Original Lúcio Artes)

### Conceito

```
CRIAR campanha = de cima para baixo (Objetivo → Segmentação → Criativo)
ANALISAR campanha = de BAIXO para cima (Anúncio → Sinais → Diagnóstico → Decisão)
```

### Diagnóstico de Relevância (3 Classificações)

Após 500 impressões, o Facebook ativa 3 métricas no nível de ANÚNCIO:

| Classificação | O que mede | Ação se "Abaixo da Média" |
|---------------|-----------|---------------------------|
| **Qualidade** | Atributos do anúncio vs políticas | Refazer criativo, remover clickbait |
| **Engajamento** | Reação do público (curtidas, cliques) | Mudar copy/visual para gerar reação |
| **Conversão** | Resultado para o anunciante | Rever oferta, LP, checkout |

### Tabela de Decisão

| Diagnóstico | Ação |
|-------------|------|
| Na média ou acima (3/3) | ✅ ESCALAR — custo CAI ao aumentar budget |
| Na média ou acima (2/3) | ⚠️ Otimizar o pilar fraco, depois escalar |
| Abaixo da média (bottom 35%) | 🔴 PAUSAR — corrigir antes de gastar mais |
| Abaixo da média (bottom 10%) | ⛔ PARAR IMEDIATO — refazer tudo |

### 50 Conversões = Saída do Aprendizado

O Meta precisa de ~50 conversões em 7 dias para sair do aprendizado. Quando isso acontece E os diagnósticos estão na média ou acima, o sistema otimiza de verdade e custos caem.

**Caso documentado:** CPA de R$7,50 → R$1,69 (redução de 77%) com diagnóstico correto. Lead de R$112 → R$7 em escala de R$900/dia para R$5.000/dia.

### 7 Atributos de Baixa Qualidade (Evitar)

1. Retenção de informação (clickbait)
2. Linguagem sensacionalista
3. Engagement bait ("curte se...")
4. Blank pages / destino sem conteúdo
5. Pop-ups intersticiais
6. Volume desproporcional de anúncios
7. Experiência inesperada de conteúdo

---

## TRACKING AVANÇADO 2025

### Traqueamento vs Rastreamento

```
RASTREAMENTO (antigo): Saber DE ONDE veio o clique (UTM, last-click)
TRAQUEAMENTO (moderno): Coletar COMPORTAMENTO para alimentar IA preditiva

O dinheiro está na camada 3: IA de otimização, não no dashboard.
```

### Stack de Server-Side Tracking

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  BROWSER → GTM Web → GTM Server (VPS) → Meta CAPI + Google                │
│                                                                             │
│  Vantagem: dados não passam pelo navegador do usuário                      │
│  Resultado: mais confiável, mais rápido, ignora ad blockers               │
│                                                                             │
│  STACK RECOMENDADA:                                                         │
│  VPS (AWS/GCP) + GTM Server + N8N para automação + Graph API v23.0        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Excesso de Scripts = Connect Rate Baixo

- Cada script no header é um mini-programa que atrasa carregamento
- Caso real: Connect rate de 44% → 78% após consolidar/reduzir scripts
- **Insight:** Consolidar scripts de tracking em menos chamadas melhora performance drasticamente
- Remover scripts duplicados, plugins inativos, e tags desnecessárias do GTM

### Tracking WhatsApp (CAPI)

Para campanhas de mensagens no WhatsApp:
1. Meta gera **ACTWACLIB** (equivalente ao FBCLID para WhatsApp)
2. Salvar ACTWACLIB no banco de dados ao receber mensagem
3. Quando converter, enviar evento via API com ACTWACLIB
4. Meta atribui conversão à campanha

### Pré-Checkout Para Hotmart (Tracking Confiável)

1. Criar formulário na página de vendas (captar nome + telefone)
2. Enviar dados para banco de dados/N8N
3. Redirecionar para checkout Hotmart
4. Webhook de compra → cruzar com dados do formulário → API Meta

### Memória de 7 Dias do Meta

- Meta só aprende com os últimos 7 dias
- 7 dias de pausa = volta ao aprendizado ZERO
- Se tem 50+ conversões/dia, testar janela de 1 dia (ao invés de 7)

### 3 Segundos de Loading = 70% Abandono

Google benchmark. Meta pune com atribuição de baixa qualidade. Soluções:
- Remover scripts desnecessários do header
- Consolidar/reduzir scripts de tracking
- Remover plugins WordPress inativos
- CDN + hospedagem otimizada

---

## Checklist Completo (Tracking + Campanha)

```
TRACKING:
□ 1. Pixel instalado na página
□ 2. API de Conversão configurada (server-side)
□ 3. Advanced Match MANUAL (email, telefone, nome)
□ 4. Funil de eventos na página (PV → Scroll → VC → AW)
□ 5. Funil de eventos no checkout (ATC → IC após dados → API → Purchase)
□ 6. Subscribe para assinaturas (com predicted_ltv)
□ 7. PIX otimizado (valor proporcional)
□ 8. Pixel da plataforma desabilitado (usar apenas o seu)
□ 9. Eventos testados no Event Test
□ 10. Métricas 80-10-10 criadas no gerenciador

CAMPANHA DE CONTROLE:
□ 11. Objetivo: Vendas (manual)
□ 12. ABO com orçamento TOTAL por 7 dias
□ 13. 3 conjuntos × 3 anúncios (imagem e vídeo separados)
□ 14. Segmentações diferentes por conjunto
□ 15. UTMs dinâmicos configurados
□ 16. Avaliar no DIA 4 (80-10-10)
□ 17. Se bom → Estender (prazo + orçamento simultâneo)

DIAGNÓSTICO (após 500 impressões):
□ 18. Verificar 3 classificações no nível de anúncio
□ 19. Na média ou acima → pode escalar
□ 20. Abaixo → pausar e corrigir antes de gastar mais
```

## Fontes do Mega Brain

| Expert | Contribuição | DNA Path |
|--------|-------------|----------|
| **Lúcio Artes** (PRIMARY — 501 elementos, 13 cursos) | Funil de eventos, API, 80-10-10, Campanha de Controle, Extendida, Funil Invertido, Diagnóstico de Relevância, Server-Side | knowledge/external/dna/persons/lucio-artes/ |
| Cat Howell | Attribution Window Analysis, OCPM/CPM Selection Matrix | knowledge/external/dna/persons/cat-howell/ |
| Frank Kern | Hyros integration, multi-platform attribution | knowledge/external/dna/persons/frank-kern/ |
| Jeremy Haynes | ConnectIO Suite, Facebook Rules Automation | knowledge/external/dna/persons/jeremy-haynes/ |

## Quando Consultar Esta Skill

- "Como configurar tracking para minha página?"
- "Como criar campanha de controle?"
- "Como estender campanha sem resetar aprendizado?"
- "Meu connect rate está baixo"
- "Como funciona o funil invertido?"
- "Diagnóstico de relevância — como analisar?"
- "Como implementar API de conversão / server-side?"
- "Como trackear WhatsApp no Meta?"
- "Qual a diferença entre pixel e CAPI?"
- "Princípio 80-10-10 — como validar funil?"
- "Como configurar PIX no pixel?"
- "500 impressões — e agora?"
