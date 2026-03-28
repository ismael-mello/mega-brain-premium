# MEMORY: Meta Ads API

> **Versao:** 1.0.0
> **Tipo:** SOLO (Technical Source)
> **Ultima atualizacao:** 2026-03-28
> **Fontes processadas:** 1

---

## FONTES PROCESSADAS

| # | Source ID | Nome | Arquivos | Status |
|---|----------|------|----------|--------|
| 1 | META-API-v25 | Meta Marketing API Documentation v25.0 | 29 | COMPLETE |

---

## INSIGHTS-CHAVE

| # | Insight | Dominio | Source |
|---|---------|---------|--------|
| 1 | Campaign hierarchy (Campaign > Ad Set > Ad) e a estrutura atomica de tudo na API | campaign-management | META-API-v25 |
| 2 | Learning phase requer 50 optimization events/week por ad set; editar reseta o contador | campaign-management | META-API-v25 |
| 3 | CAPI deduplication via event_id — mesmo event_id de Pixel e CAPI = conta 1x | conversions-api | META-API-v25 |
| 4 | SHA-256 hashing obrigatorio para todos os campos PII (em, ph, fn, ln, ct, st, zp, country, db, ge) | conversions-api | META-API-v25 |
| 5 | Rate limiting usa BUC scoring — default 200 calls/hour/token, throttling progressivo acima disso | rate-limiting | META-API-v25 |
| 6 | Lookalike Audiences requerem seed audience minimo de 100 pessoas no mesmo pais | audience-targeting | META-API-v25 |
| 7 | Custom Audiences de customer list exigem pelo menos 2 identificadores para match rate otimo | audience-targeting | META-API-v25 |
| 8 | Insights API suporta breakdowns por age, gender, placement, device, country e combinacoes | insights-reporting | META-API-v25 |
| 9 | Async reports via report_run_id para queries grandes — poll ate async_status = "Job Completed" | insights-reporting | META-API-v25 |
| 10 | Lead Ads instant forms retornam dados via Webhooks ou polling de /leadgen_forms/{form-id}/leads | lead-generation | META-API-v25 |
| 11 | Dynamic Product Ads requerem Product Catalog vinculado + Product Feed atualizado | dynamic-product-ads | META-API-v25 |
| 12 | Error code 17 = rate limit exceeded, code 100 = invalid parameter, code 190 = access token expired | rate-limiting | META-API-v25 |
| 13 | Reach Estimate endpoint permite estimar tamanho de audiencia antes de gastar budget | audience-targeting | META-API-v25 |
| 14 | Business Manager controla acesso a ad accounts, pages, pixels via asset permissions | business-asset-management | META-API-v25 |
| 15 | API versioning tem lifecycle definido: cada versao dura ~2 anos antes de deprecation | versioning | META-API-v25 |

---

## THRESHOLDS CRITICOS

| Metrica | Valor | Contexto | Source |
|---------|-------|----------|--------|
| Learning phase events | 50/week per ad set | Minimo para sair do learning phase | META-API-v25 |
| Rate limit default | 200 calls/hour/token | BUC scoring base; pode variar com app quality | META-API-v25 |
| Lookalike seed minimum | 100 pessoas | Mesmo pais; recomendado 1,000-50,000 | META-API-v25 |
| Custom Audience match | 2+ identificadores | Minimo para match rate aceitavel | META-API-v25 |
| API version lifecycle | ~2 anos | Da lancamento ate deprecation | META-API-v25 |
| CAPI event delay max | 72 horas | Eventos apos 72h sao descartados | META-API-v25 |
| Async report timeout | 1 hora | Poll interval recomendado: 30-60 segundos | META-API-v25 |

---

## DOMINIOS COBERTOS

| Dominio | Arquivos Fonte | Profundidade |
|---------|---------------|-------------|
| campaign-management | reference-all-core.md, reference-ad.md, reference-ad-image.md, getting-started.md | Alta |
| audience-targeting | audiences-overview.md, custom-audiences.md, lookalike-audiences.md, detailed-targeting.md, basic-targeting.md, reach-estimate.md | Alta |
| conversions-api | conversions-api-overview.md, conversions-api-using.md, conversions-api-parameters.md, conversions-api-deduplication.md, conversions-api-best-practices.md | Muito Alta |
| insights-reporting | insights-api.md, insights-best-practices.md, insights-breakdowns.md, ads-action-stats.md | Alta |
| rate-limiting | rate-limiting.md, error-reference.md | Media |
| lead-generation | lead-ads.md | Media |
| dynamic-product-ads | dynamic-product-ads.md, catalog.md | Media |
| business-asset-management | business-asset-management.md, authorization.md | Media |
| versioning | versioning.md, best-practices.md | Baixa |

---

## PADROES IDENTIFICADOS

1. **Tudo e hierarquico** — Campaign > Ad Set > Ad > Creative. Business Manager > Ad Account > Campaign.
2. **Dual signal e o padrao** — Pixel (browser) + CAPI (server) com deduplication via event_id.
3. **Rate limits sao progressivos** — nao binarios. BUC scoring aumenta/diminui acesso gradualmente.
4. **Privacy e layer zero** — hashing, consent, data processing options permeiam todos os endpoints.
5. **Async para escala** — reports grandes, batch requests, webhooks — a API empurra para async.
