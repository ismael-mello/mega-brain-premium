# MEMORY: Capital Upgrade — Paulo Vito Porto / PWR Gestão

> **Versao:** 1.0.0
> **Criado:** 2026-03-11
> **Ultima atualizacao:** 2026-03-11
> **Tipo:** SOLO (fonte unica: FLGF Turma 07)

---

## SOBRE ESTE ARQUIVO

MEMORY.md e a experiencia acumulada do agente — insights extraidos das fontes processadas, padroes de pensamento identificados, e decisoes-padrao que guiam respostas.

**REGRA:** MEMORY = experiencia pratica. DNA = conhecimento estruturado. Nao duplicar.

---

## FONTES PROCESSADAS

| Fonte | Tipo | Modulos | Elementos | Data |
|-------|------|---------|-----------|------|
| FLGF - Formacao de Lideres e Gestores Financeiros (Turma 07) | Programa completo | M00-M10 + Bonus | 257 | 2026-03-11 |

**Agentes enriquecidos:**
- CFO cargo agent (peso 0.85) — ^[agents/cargo/c-level/cfo/DNA-CONFIG.yaml]
- COO cargo agent (peso 0.40) — ^[agents/cargo/c-level/coo/DNA-CONFIG.yaml]

**AGG criado:**
- AGG-GESTAO-FINANCEIRA.yaml (70 elementos selecionados) — ^[knowledge/external/dna/AGGREGATED/AGG-GESTAO-FINANCEIRA.yaml]

---

## APRENDIZADOS E INSIGHTS

### DRE e Demonstrativos

| Insight | ID | Fonte |
|---------|----|-------|
| DRE usa regime de competencia; fluxo de caixa usa regime de caixa. Confundir os dois e erro de iniciante com consequencias de especialista. | PHI-CU-101 | M04 |
| Analise vertical = raio-X (percentual sobre receita liquida). Analise horizontal = filme (evolucao temporal). Usar os dois juntos. | MM-CU-103, MM-CU-104 | M04 |
| EBITDA = gerador de caixa operacional puro. Remover juros, impostos, depreciacao e amortizacao para comparar empresas de forma justa. | HEUR-CU-103 | M04 |
| CMV (comercio) = CPV (industria) = CSP (servico). O nome muda, o conceito e o mesmo: custo direto da atividade fim. | HEUR-CU-101 | M04 |
| Custo = ligado a atividade fim. Despesa = ligado a estrutura. A separacao define onde aparece na DRE e como analisar margem. | PHI-CU-102 | M04 |

### Indicadores Financeiros

| Insight | ID | Fonte |
|---------|----|-------|
| Tres utilidades de um indicador: tomar decisao, acompanhar execucao, medir performance. Se nao faz nenhuma das tres, descarta. | MM-CU-107 | M05 |
| Classificacao R1/R2/R3: R1 semanal (cruciais), R2 mensal (importantes), R3 trimestral (complementares). | MM-CU-108 | M05 |
| 42 indicadores financeiros em 4 grupos: resultado economico, fluxo de caixa, estrutura patrimonial, atividade operacional. | MM-CU-109 | M05 |
| Analogia do painel do carro: voce pode dirigir sem ele, mas so descobre o problema quando quebrar. Mesmo logica dos indicadores. | MM-CU-110 | M05 |
| Fatores criticos de sucesso = variaveis que, se nao bem gerenciadas, comprometem o resultado mesmo com tudo mais perfeito. | MM-CU-111 | M05 |

### Gestao de Resultado e ARM

| Insight | ID | Fonte |
|---------|----|-------|
| ARM (Analise de Resultado Mensal) e o modulo mais importante — nao traz conteudo novo, traz a pratica de analisar resultado sistematicamente. | PHI-CU-111 | M07 |
| CMV ideal vs CMV real: a distancia entre os dois e o diagnostico. Desperdicio, extravio, erro de input ficam visiveis aqui. | MM-CU-116 | M07 |
| Efeito espantalho: as vezes nao precisa encontrar a fraude — so espalhar que esta olhando. O numero melhora sozinho. | MM-CU-117 | M07 |
| Progressao: disciplina → habito → cultura → gestao de resultado. Sem disciplina inicial, nao ha gestao sustentavel. | MM-CU-115 | M07 |
| ARM vai do macro pro micro: foto dos indicadores → DRE detalhada → curvas mensais. Cada nivel revela o que o anterior escondeu. | MM-CU-118 | M07 |

### Gestao de Caixa e Inadimplencia

| Insight | ID | Fonte |
|---------|----|-------|
| Conciliacao bancaria diaria e inegociavel. Passar de um dia ja abre brecha pra problemas. | PHI-CU-110 | M06 |
| Inadimplencia tem envelhecimento: 1-30 dias (curtissimo), 30-60 (curto), 60-90 (medio), 90+ (longo). Cada faixa = tratamento diferente. | MM-CU-112 | M06 |
| Prevenir inadimplencia e mais barato e eficaz que cobrar. A regua de cobranca comeca antes do vencimento. | PHI-CU-109 | M06 |
| PCLD (Provisao de Credito de Liquidacao Duvidosa) = conta na DRE que registra creditos provavelmente irrecuperaveis. | MM-CU-114 | M06 |

### Endividamento e Emprestimos

| Insight | ID | Fonte |
|---------|----|-------|
| Divida nao e problema — divida mal gerenciada e problema. Emprestimo e ferramenta estrategica quando o ROI supera o CET. | PHI-CU-200, MM-CU-200 | M08 |
| CET (Custo Efetivo Total) e a unica metrica honesta para comparar emprestimos. Taxa nominal anunciada engana. | PHI-CU-203, MM-CU-201 | M08 |
| Indice de endividamento geral (Passivo/Ativo) acima de 70% = sinal de alerta. Monitorar mensalmente. | MM-CU-210 | M08 |
| SAC vs PRICE: SAC tem parcelas decrescentes (mais amortizacao no inicio); PRICE tem parcelas fixas (mais juros no inicio). | MM-CU-203 | M08 |
| Cenario macroeconomico nao e assunto so de economista. SELIC e IPCA afetam diretamente custo e capacidade de pagamento. | PHI-CU-211 | M08 |

### Orcamento Empresarial

| Insight | ID | Fonte |
|---------|----|-------|
| OBZ (Orcamento Base Zero) = antidoto contra piloto automatico. Cada centavo precisa justificar sua existencia. | PHI-CU-205 | M09 |
| Orcamento como contrato: o orcamento aprovado e compromisso entre gestores e direcao. Desvio exige justificativa formal. | MM-CU-204 | M09 |
| Top-down = velocidade mas pouca adesao. Bottom-up = adesao mas demora. Ideal e combinar os dois. | MM-CU-205 | M09 |
| GMD (Gestao Matricial de Despesas) transforma orcamento de exercicio teorico em ferramenta de accountability real. | PHI-CU-212 | M09 |
| Variancia orcamentaria nao e busca de culpados — e entender causas estruturais vs pontuais para calibrar o proximo ciclo. | MM-CU-206 | M09 |

### Precificacao e Pro-Labore

| Insight | ID | Fonte |
|---------|----|-------|
| Preco de venda deve ser calculado, nunca chutado. Precificacao errada mata mais empresas que falta de clientes. | PHI-CU-209 | Bonus |
| Margem de contribuicao = o que realmente sobra para pagar a estrutura. Numero mais importante para o empresario. | PHI-CU-210 | Bonus |
| Pro-labore nao e lucro. Misturar remuneracao do socio com resultado distorce toda a gestao financeira. | PHI-CU-208 | Bonus |
| Precificacao por margem de contribuicao: preco = custos variaveis + MC desejada. Nunca so markup sobre custo. | MM-CU-208 | Bonus |

---

## PADROES DE PENSAMENTO

| Padrao | Descricao | Expressao tipica |
|--------|-----------|------------------|
| Dado antes de opiniao | Toda afirmacao precisa de numero ou fonte | "Confia na tua opiniao mas traz dado." |
| Pratica sobre teoria | Implementacao real diverge do que foi ensinado | "Na pratica a teoria e outra." |
| Ritmo sobre volume | Consistencia diaria/mensal supera estudo intensivo pontual | "Trazer ritmo importa mais do que trazer conhecimento." |
| Diagnostico antes de solucao | Primeiro entender o numero, depois agir | "Empresa nao e so engenharia, e artesanato." |
| Simplicidade operacional | Ferramentas complexas nao substituem disciplina basica | "BI sem acao e decoracao." |

---

## DECISOES PADRAO

| Situacao | Decisao | Justificativa |
|----------|---------|---------------|
| Comparar emprestimos | Sempre usar CET, nunca taxa nominal | Taxa nominal esconde IOF, TAC e seguros |
| Inadimplencia detectada | Identificar faixa de envelhecimento e tratar por protocolo | Cada faixa tem abordagem diferente |
| Gestao de resultado | Implementar ARM mensal antes de qualquer ferramenta avancada | Sem ritmo, ferramentas nao funcionam |
| Endividamento > 70% | Acionar plano de reducao — nao e momento de novo emprestimo | Risco sistemico elevado |
| Orcamento novo | Avaliar se contexto pede OBZ ou orcamento incremental | OBZ para pilotos automaticos; incremental para estavel |
| Pro-labore undefined | Calcular com base em mercado + capacidade da empresa — formalizar | Mistura PF/PJ distorce tudo |

---

## HISTORICO DE SESSOES

| Sessao | Data | Acao Principal |
|--------|------|----------------|
| SESSION-2026-03-11 | 2026-03-11 | Extracao completa do DNA FLGF M00-M10+Bonus (257 elementos) |
| SESSION-2026-03-11 | 2026-03-11 | CFO/COO enrichment + AGG-GESTAO-FINANCEIRA criado |
| SESSION-2026-03-11 | 2026-03-11 | Person Agent criado: SOUL + MEMORY + DNA-CONFIG + AGENT |

---

*Todo ritmo comeca com disciplina. Toda gestao comeca com dado.*
