"""Phase 7: Append DK Referral Machine enrichment to 4 cargo agent MEMORY.md files."""

import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- CLOSER ----
closer_block = """

---

## DK REFERRAL MACHINE ENRICHMENT (2026-03-16)

> **Fonte:** Dan Kennedy — The Ultimate No BS Referral Machine (Source #10)
> **Versão:** +6 insights adicionados → v2.23.0
> **Relevância:** Referral selling dynamics, testimonials, pricing psychology

### Insights RM para CLOSER

| Data | Insight | ID | PATH_RAIZ | Confiança |
|------|---------|-----|-----------|-----------|
| 2026-03-16 | **Referred Customer: Less Resistance**: Leads por referral têm menos resistência de preço e vendas — fecha mais rápido, com menos objeções. | HEUR-DK-729 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Satisfaction ≠ Referral**: Cliente satisfeito não refere em abundância. Satisfação é passiva — não gera venda ativa. Exige sistema, não esperança. | FIL-DK-572 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Testimonials = Prova Mais Crível**: Testemunhos são o tipo de prova mais acreditável. Usar em toda apresentação de vendas. | FIL-DK-576 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Write Testimonial Yourself**: Escreva o testemunho pelo cliente e peça aprovação — raramente mudam uma palavra. Elimina friction, gera prova usável. | HEUR-DK-743 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Great Testimonial Framework**: 5 elementos — before/after drama + detalhes específicos + erasure de objeção + multimídia + credibilidade do autor. | FW-DK-737 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Information Easier to Refer**: Referir informação (relatório, guia) é dramaticamente mais fácil que referir um prestador. Usar reports como entrada. | FIL-DK-571 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |

### Padrões Decisórios RM Adicionados

| ID | Situação | Decisão Padrão | Ref | Confiança |
|----|----------|----------------|-----|-----------|
| PD-RM-CLOSER-001 | Prospect referenciado vs cold | Tratar diferente — menos qualifying friction, fechar mais direto | HEUR-DK-729 | ALTA |
| PD-RM-CLOSER-002 | Precisa de prova social rápida | Usar testemunho com 5 elementos DK — escrever você mesmo, pedir aprovação | FW-DK-737 + HEUR-DK-743 | ALTA |
| PD-RM-CLOSER-003 | Pedir referral após fechamento | Nunca pedir diretamente ao cliente — educar sobre sistema, apresentar Special Report | FIL-DK-571 | ALTA |

*Atualização: 2026-03-16 — DK Referral Machine Source #10 Enrichment*
*MEMORY.md v2.23.0*
"""

# ---- CMO ----
cmo_block = """

---

## DK REFERRAL MACHINE ENRICHMENT (2026-03-16)

> **Fonte:** Dan Kennedy — The Ultimate No BS Referral Machine (Source #10)
> **Versão:** +18 insights adicionados → v2.4.0
> **Relevância:** Referral marketing strategy, internal marketing, newsletters, events, gifting

### Insights RM para CMO — Estratégia de Referral

| Data | Insight | ID | PATH_RAIZ | Confiança |
|------|---------|-----|-----------|-----------|
| 2026-03-16 | **Referral Machine — 3 I's**: Intentional + Invested + Integrated. Sem esses três, não é sistema, é esperança. | MM-DK-560 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Foundation Before Machine**: Quatro camadas antes do sistema de referral: WOW service + WOW package + gifting + internal culture. | MM-DK-563 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Referral Budget = Math First**: Budget começa pelo CAC cold. Se cold custa $6k, pagar $5k por referral ainda é lucro. Criatividade depois, math primeiro. | MM-DK-564 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Status-by-Doing**: Pessoas referem quando isso lhes dá STATUS — 3 formas: status perante o indicado, perante o grupo, perante si mesmo. | MM-DK-565 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Permanent Visible Space Principle**: Presentes que ficam em espaço permanente e visível forçam conversas — melhor que consumíveis digitais. | MM-DK-566 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Omnipresence Model**: Cliente não consegue dar 360 graus sem te ver. 280+ comunicações/ano não-vendas (GKIC benchmark). | MM-DK-567 + HEUR-DK-737 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Upstream via Centers of Influence**: Pescar onde os peixes andam — endorsed mailing via COIs direciona para informação, não para o prestador diretamente. | MM-DK-568 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **ABC Segmentation for Referrals**: Investimento diferenciado por segmento. A-clientes recebem mais gifting/atenção — produzem mais referrals. | MM-DK-569 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **5 Razões que Clientes Não Referem**: Não sabem que você quer / não sabem como / medo de errar / não pensaram / nunca foram ativados. | MM-DK-570 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Digital Gifts = Zero WOW**: Presentes digitais não têm permanência, WOW nem pass-along. Misturar com itens físicos permanentes. | FIL-DK-568 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **WOW Box Benchmark**: Burleson Ortho — WOW box de $170 para cliente de $6-7K. Resultado: referrals 15% → 60%. ROI absurdo. | HEUR-DK-739 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Newsletter Failure**: Maioria das newsletters falha por ser 100% conteúdo core-deliverable — chato. Deve ter entretenimento + reconhecimento + promoção. | HEUR-DK-738 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |

### Frameworks RM para CMO

| Data | Framework | ID | PATH_RAIZ | Confiança |
|------|-----------|-----|-----------|-----------|
| 2026-03-16 | **Referral Machine Architecture**: Foundation > Tools > Training > Measurement. Sequência obrigatória. | FW-DK-729 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **WOW New Client Package**: educate + inform + cool/fun + permanence + pass-along. 5 componentes. | FW-DK-730 + MET-DK-613 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Special Report of Month System**: stealth referral via informação — pessoa indica o relatório, não você. | FW-DK-731 + MET-DK-615 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Referral Culture Building**: 6 componentes para prática visível referral-driven. | FW-DK-732 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Internal Marketing System**: 9 componentes de infraestrutura interna de marketing. | FW-DK-733 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Client Referral Event**: evento anual de apreciação com cultura bring-a-buddy. Blueprint de 100 a milhares. | FW-DK-736 + MET-DK-619 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |

### Metodologias RM para CMO

| ID | Metodologia | PATH_RAIZ |
|----|-------------|-----------|
| MET-DK-614 | Gift of Month System: gifting agendado que aparece randômico (a cada 6 semanas, skip julho) | knowledge/external/sources/dan-kennedy/raw/referral-machine/ |
| MET-DK-620 | Endorsed Mailing Execution: duas cartas dirigindo para report, não para o prestador | knowledge/external/sources/dan-kennedy/raw/referral-machine/ |
| MET-DK-622 | Disney D23 Model: caixa de boas-vindas + gifting físico recorrente | knowledge/external/sources/dan-kennedy/raw/referral-machine/ |

### Padrões Decisórios RM Adicionados

| ID | Situação | Decisão Padrão | Ref | Confiança |
|----|----------|----------------|-----|-----------|
| PD-RM-CMO-001 | Estruturar sistema de referral | Começar pelo math (CAC cold) → WOW Package → Newsletter → Events | MM-DK-564 + FW-DK-729 | ALTA |
| PD-RM-CMO-002 | Escolher tipo de presente para cliente | Permanente e visível > consumível > digital. Mix físico+food. | MM-DK-566 + FIL-DK-568 | ALTA |
| PD-RM-CMO-003 | Segmentar investimento de referral | ABC segmentation — A-clientes recebem gifting premium | MM-DK-569 | ALTA |
| PD-RM-CMO-004 | Newsletter não está performando | Adicionar entretenimento + reconhecimento de clientes + promoção ao conteúdo | HEUR-DK-738 | ALTA |
| PD-RM-CMO-005 | Aumentar referrals sem pedir diretamente | Special Report of Month como stealth referral | FW-DK-731 | ALTA |

*Atualização: 2026-03-16 — DK Referral Machine Source #10 Enrichment*
*MEMORY.md v2.4.0*
"""

# ---- CRO ----
cro_block = """

---

## DK REFERRAL MACHINE ENRICHMENT (2026-03-16)

> **Fonte:** Dan Kennedy — The Ultimate No BS Referral Machine (Source #10)
> **Versão:** +9 insights adicionados → v3.3.0
> **Relevância:** Referral ROI math, customer retention, churn economics, reactivation

### Insights RM para CRO — Revenue e Retenção

| Data | Insight | ID | PATH_RAIZ | Confiança |
|------|---------|-----|-----------|-----------|
| 2026-03-16 | **Customer Replacement Costs Double**: Perder 1 cliente exige 2 novos para compensar (LTV + aquisição). Retenção é o ROI mais alto. | FIL-DK-575 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Single-Digit Referral Rate Default**: Maioria das empresas que afirma ter bons referrals mede <5%. Sistema intencional chega a 15-60%. | HEUR-DK-730 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Referral ROI Math**: Cold CAC = $6k → pagar $5k por referral ainda economiza $1k + mais qualidade + velocidade de fechamento. | HEUR-DK-731 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Referral Budget = Math First**: Budget de referral começa no CAC cold. Decisão financeira, não criativa. | MM-DK-564 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Indifference = 68% Churn**: Preço é razão #6 de perda de cliente — indiferença é 68%. Omnipresence é anti-churn. | HEUR-DK-742 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Closed Loop Retention**: Quem refere fica. Ato de referir cria compromisso psicológico (Cialdini) — referrer é mais difícil de perder. | MM-DK-561 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **6-Month Non-Referral Trigger**: Cliente que não referiu em 6 meses precisa de conversa direta — proativo, não passivo. | HEUR-DK-740 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **WOW Box ROI**: Burleson: $170 no WOW box em cliente de $6-7K → referrals 15% → 60%. Math claro. | HEUR-DK-739 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Lost Customer Reactivation**: 6 razões de saída endereçadas com campanha multi-step. Mais barato que cold acquisition. | MET-DK-621 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |

### Padrões Decisórios RM Adicionados

| ID | Situação | Decisão Padrão | Ref | Confiança |
|----|----------|----------------|-----|-----------|
| PD-RM-CRO-001 | Calcular budget de referral | CAC cold é o teto — referral < CAC cold = ROI positivo garantido | MM-DK-564 + HEUR-DK-731 | ALTA |
| PD-RM-CRO-002 | Cliente não referiu em 6+ meses | Trigger: conversa direta. Identificar razão (5 motivos DK) e remover barreira. | HEUR-DK-740 + MM-DK-570 | ALTA |
| PD-RM-CRO-003 | Avaliar custo de churn | Cada cliente perdido = 2 novos para compensar. Calcular antes de ignorar retenção. | FIL-DK-575 | ALTA |
| PD-RM-CRO-004 | Reativar clientes perdidos | Campanha multi-step endereçando 6 razões de saída. Mais barato que cold. | MET-DK-621 | ALTA |
| PD-RM-CRO-005 | Medir taxa de referral | Baseline: <5% sem sistema. Meta com sistema: 15-60%. Benchmark Burleson: $170 → 60%. | HEUR-DK-730 + HEUR-DK-739 | ALTA |

*Atualização: 2026-03-16 — DK Referral Machine Source #10 Enrichment*
*MEMORY.md v3.3.0*
"""

# ---- SALES MANAGER ----
sm_block = """

---

## DK REFERRAL MACHINE ENRICHMENT (2026-03-16)

> **Fonte:** Dan Kennedy — The Ultimate No BS Referral Machine (Source #10)
> **Versão:** +8 insights adicionados → v2.14.0
> **Relevância:** Staff training, referral culture, compliance system, internal marketing

### Insights RM para SALES MANAGER — Staff e Cultura de Referral

| Data | Insight | ID | PATH_RAIZ | Confiança |
|------|---------|-----|-----------|-----------|
| 2026-03-16 | **Staff Hostage Mode**: Staff em modo de refém perpetuo é a maior ameaça interna à implementação de referral. Resolver antes de treinar. | FIL-DK-573 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Staff Refers First**: Staff deve referir da própria rede primeiro — só assim motiva clientes. Quem não pratica não prega. | HEUR-DK-741 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Recognize & Reward = Mais Comportamento**: Reconhecer e recompensar gera mais do comportamento. Ignorar elimina. | FIL-DK-565 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Foundation Before Machine**: 4 camadas antes do sistema de referral — WOW service, WOW package, gifting, cultura interna. | MM-DK-563 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Referral Culture Building**: 6 componentes para cultura visível de referrals — leaderboard, tiers, símbolos, reconhecimento público. | FW-DK-732 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Staff Referral Training Cycle**: Teach → Coach → Monitor → Enforce → Reward → Punish. Ciclo completo, não treinamento único. | MET-DK-617 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Referral Toolkit Deployment**: Tools + Training + Monthly Restocking. Sistema físico que staff usa no ponto de contato. | MET-DK-616 + FW-DK-729 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |
| 2026-03-16 | **Mindset de Implementação**: "Como posso fazer isso funcionar?" vs "não vai funcionar para mim". Aplicar ao onboarding. | FIL-DK-567 | knowledge/external/sources/dan-kennedy/raw/referral-machine/ | ALTA |

### Padrões Decisórios RM Adicionados

| ID | Situação | Decisão Padrão | Ref | Confiança |
|----|----------|----------------|-----|-----------|
| PD-RM-SM-001 | Implementar sistema de referral com equipe | Verificar se staff está em hostage mode antes de treinar. Resolver primeiro. | FIL-DK-573 | ALTA |
| PD-RM-SM-002 | Treinar staff para referrals | Ciclo completo: Teach → Coach → Monitor → Enforce → Reward → Punish | MET-DK-617 | ALTA |
| PD-RM-SM-003 | Staff não está motivando clientes a referir | Staff deve referir da própria rede primeiro — credibilidade vem do exemplo | HEUR-DK-741 | ALTA |
| PD-RM-SM-004 | Medir performance de referrals do time | Criar leaderboard visível + reconhecimento público + tiers | FIL-DK-565 + FW-DK-732 | ALTA |
| PD-RM-SM-005 | Onboarding de novo membro do time | Apresentar mindset DK: "Como faço isso funcionar?" não "por que não vai funcionar" | FIL-DK-567 | ALTA |

*Atualização: 2026-03-16 — DK Referral Machine Source #10 Enrichment*
*MEMORY.md v2.14.0*
"""

files_and_blocks = [
    ("agents/cargo/sales/closer/MEMORY.md", closer_block),
    ("agents/cargo/c-level/cmo/MEMORY.md", cmo_block),
    ("agents/cargo/c-level/cro/MEMORY.md", cro_block),
    ("agents/cargo/sales/sales-manager/MEMORY.md", sm_block),
]

for filepath, block in files_and_blocks:
    full_path = os.path.join(BASE, filepath)
    with open(full_path, "a", encoding="utf-8") as f:
        f.write(block)
    print(f"APPENDED: {filepath}")

print("\nPhase 7 COMPLETE — 4 cargo agents enriched with RM elements")
