# MEMÓRIA: Media Buyer

> **Agente:** `/agents/cargo/marketing/media-buyer/AGENT.md`
> **Criada:** 2026-03-22
> **Última atualização:** 2026-03-22
> **Total de registros:** 1 (Molly Pittman enrichment)
> **Versão:** 2.0.0

---

## METADADOS DE CONTEXTO

### Projeto Atual
| Campo | Valor |
|-------|-------|
| **Domínio primário** | traffic |
| **Status** | ENRICHED — Molly Pittman (PRIMARY, 397 elements) |

---

## PADRÕES DECISÓRIOS

| ID | Situação | Decisão Padrão | chunk_id | PATH_RAIZ | Confiança |
|----|----------|---|---|---|---|
| PD-001 | Campaign strategy | Use Traffic Plays (12 plays) to select campaign type | MP-TP | /knowledge/external/sources/molly-pittman/raw/ | ALTA |
| PD-002 | Audience segmentation | Apply Traffic Temperature (cold/warm/hot) | MP-TT | /knowledge/external/sources/molly-pittman/raw/ | ALTA |
| PD-003 | Campaign diagnosis | Check 5 Elements of High Converting Campaign | MP-5E | /knowledge/external/sources/molly-pittman/raw/ | ALTA |
| PD-004 | Creative testing | Use Ad Grid for systematic creative testing | MP-AG | /knowledge/external/sources/molly-pittman/raw/ | ALTA |
| PD-005 | Scaling | Apply CBO Scaling methodology | MP-CBO | /knowledge/external/sources/molly-pittman/raw/ | ALTA |
| PD-006 | Retargeting | Use Retargeting Layers (multi-tier architecture) | MP-RL | /knowledge/external/sources/molly-pittman/raw/ | ALTA |

### 2026-03-26 — Molly Pittman Enrichment (397 elements, PRIMARY source)
- **Source:** Molly Pittman Traffic Training
- **Key frameworks:** Traffic Plays (12 plays), Traffic Temperature, 5 Elements of High Converting Campaign, CBO Scaling, Retargeting Layers, Ad Grid, Traffic Engine 9-Step, 11 Ad Copy Chunks, Before/After Grid, Customer Avatar Canvas
- **Impact:** Molly Pittman is now the PRIMARY source for this cargo agent (peso 0.95) — the foundational traffic education framework

---

## HABILIDADES DISTRIBUÍDAS

> Habilidades extraídas automaticamente pelo Skill Distribution Engine.

| ID | Habilidade | Domínios | Fonte | Relevância |
|----|-----------|---------|-------|------------|

*Pendente — será populado pelo skill_distribution.py.*

---

### 2026-03-28 — Meta Ads API v25.0 Integration
**Fonte:** Meta Marketing API Documentation (29 files, 212KB)
**Insight:** Official API documentation provides 84 DNA elements covering campaign hierarchy, CAPI implementation, audience management, rate limiting, and insights reporting. Critical operational thresholds: $0.50 min daily budget (impressions), max 200 ad sets per CBO campaign, max 50 ads per ad set, CAPI batch max 1,000 events, 48h deduplication window.
**Contexto de uso:** Reference for all API-level campaign operations, troubleshooting rate limits, implementing CAPI, audience creation limits.
**Confiança:** ALTA — official Meta documentation
