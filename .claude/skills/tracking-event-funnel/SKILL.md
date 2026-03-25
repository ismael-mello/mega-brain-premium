> **Auto-Trigger:** Quando usuário perguntar sobre tracking, pixel, API de conversão, funil de eventos, atribuição, Advanced Matching, configuração de eventos do Facebook/Meta, otimização de pixel, qualidade de eventos, nota do pixel
> **Keywords:** "tracking", "pixel", "api de conversão", "funil de eventos", "event funnel", "atribuição", "advanced matching", "qualidade de eventos", "nota do pixel", "configurar eventos", "page view", "initiate checkout", "purchase event", "subscribe event", "CAPI", "conversion API", "server-side tracking", "connect rate", "80-10-10"
> **Prioridade:** ALTA
> **Tools:** Read, Grep, Glob

## Quando NÃO Ativar
- Quando a pergunta for sobre tráfego em geral (sem foco em tracking/eventos)
- Quando for sobre criativos ou copy de anúncios
- Quando for sobre estratégias de lance ou orçamento (sem relação com eventos)
- Quando for sobre Google Ads (esta skill é focada em Meta/Facebook)

---

# SKILL: Tracking & Event Funnel Architecture

## Propósito

Guia completo para implementação de tracking avançado e funil de eventos no Meta/Facebook Ads, baseado na metodologia de **Lúcio Artes** (Formação Tráfego de Escala) complementada por outros experts do Mega Brain (Cat Howell, Frank Kern, Jeremy Haynes).

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

## Checklist de Implementação

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

## Quando Consultar Esta Skill

- "Como configurar tracking para minha página?"
- "Meu pixel está com nota baixa, o que fazer?"
- "Como implementar API de conversão?"
- "Qual a diferença entre pixel e CAPI?"
- "Como otimizar a nota do pixel?"
- "Meu connect rate está baixo"
- "Como configurar eventos do Facebook?"
- "Quero melhorar a atribuição das minhas campanhas"
- "Como funciona o funil de eventos?"
- "Devo usar Purchase ou Subscribe?"
- "Como configurar PIX no pixel do Facebook?"
