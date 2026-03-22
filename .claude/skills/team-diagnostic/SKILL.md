# TEAM DIAGNOSTIC - Multi-Agent por Equipe

> **Auto-Trigger:** Quando usuario faz pergunta operacional que envolve diagnostico, problema, ou decisao que beneficia de multiplas perspectivas de cargo
> **Keywords:** "campanha caiu", "o que fazer", "meu closer", "como resolver", "diagnostico", "equipe", "team", "minha taxa", "meu custo", "nao ta convertendo", "como melhorar", "ta dando errado", "problema com"
> **Prioridade:** MEDIA
> **Tools:** Agent, Read, Glob, Grep

## Quando Ativar

- Usuario descreve um PROBLEMA operacional (campanha caindo, closer nao fechando, etc.)
- Usuario pede diagnostico de MULTIPLAS perspectivas
- Usuario usa `/team` explicitamente
- Pergunta envolve metricas + decisao (pausar/escalar/mudar)

## Quando NAO Ativar

- Pergunta simples que 1 agent resolve (usar `/ask` em vez)
- Perguntas sobre o sistema Mega Brain (usar `/jarvis`)
- Debate filosofico entre experts (usar `/conclave`)
- Criacao de conteudo (usar `/ask copywriter`)

## Execucao

O comando `/team` tem instrucoes detalhadas em `.claude/commands/team.md`.

Resumo do fluxo:

1. Detectar dominio da pergunta (traffic, vendas, copywriting, etc.)
2. Mapear equipe: quais cargo agents participam
3. Carregar DNA de cada agent em PARALELO (usar Agent tool)
4. Cada agent responde da sua perspectiva com framework/heuristica citada
5. Consolidar plano de acao com consensos e divergencias

### Diferenca vs /conclave

| Aspecto | /team | /conclave |
|---------|-------|-----------|
| Participantes | Cargo agents (CRO, Closer, SDR) | Person agents (Hormozi, Cole) + Council |
| Perspectiva | Funcional (cada cargo) | Expert (cada mentor) |
| Fases | 1 rodada + consolidacao | 3 fases formais + sintese |
| Velocidade | Rapido (paralelo) | Completo (sequencial) |
| Uso ideal | Problemas operacionais do dia-a-dia | Decisoes estrategicas grandes |

### Diferenca vs /ask

| Aspecto | /team | /ask |
|---------|-------|------|
| Agents | Todos da equipe (3-6) | 1 agent especifico |
| Output | Diagnostico multi-perspectiva | Resposta unica |
| Quando | Problema complexo, precisa visao 360 | Pergunta pontual |
