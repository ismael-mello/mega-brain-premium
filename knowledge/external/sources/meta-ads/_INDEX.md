# Meta Ads — Source Index

> **Source:** Meta Marketing API Documentation v25.0
> **Date Fetched:** 2026-03-28
> **Total Files:** 29
> **Total Size:** ~143KB
> **Raw Location:** `knowledge/external/sources/meta-ads/raw/meta-ads-docs-v25/`

---

## Source Documents

### Comprehensive References

| # | File | Description |
|---|------|-------------|
| 1 | `02-research-report.md` | Complete technical report covering all API topics — campaign hierarchy, CAPI, audiences, insights, rate limiting, auth, errors, versioning |
| 2 | `reference-all-core.md` | Full multi-page documentation extract from Meta for Developers portal |

### Campaign Structure & Ad Objects

| # | File | Description |
|---|------|-------------|
| 3 | `getting-started.md` | API setup, first call, prerequisites |
| 4 | `reference-ad.md` | Ad (Adgroup) object — all fields, edges, CRUD operations, status values |
| 5 | `reference-ad-image.md` | Ad Image upload, hashing, read operations |

### Audiences & Targeting

| # | File | Description |
|---|------|-------------|
| 6 | `audiences-overview.md` | Overview of audience types (Custom, Lookalike, Saved) |
| 7 | `custom-audiences.md` | Custom Audience creation from CRM data — upload schema, hashing, limits (500/account) |
| 8 | `lookalike-audiences.md` | Lookalike Audience configuration — seed requirements (100+ members), ratio (1-20%), type (similarity/reach) |
| 9 | `basic-targeting.md` | Geographic, age, gender, locale targeting parameters |
| 10 | `detailed-targeting.md` | Interest/behavior targeting — search, suggestions, browse, validation endpoints |
| 11 | `reach-estimate.md` | Reach estimation and delivery estimate APIs |

### Insights & Reporting

| # | File | Description |
|---|------|-------------|
| 12 | `insights-api.md` | Insights API — endpoints, metrics (30+), date presets, attribution windows, filtering, sorting |
| 13 | `insights-breakdowns.md` | Breakdown dimensions — demographic, platform, geographic, creative, action, product, temporal |
| 14 | `insights-best-practices.md` | Insights limits, async jobs (3-step process), data refresh timing, discrepancy with Ads Manager |
| 15 | `ads-action-stats.md` | Action stats reference — action_type field values and structure |

### Conversions API (CAPI)

| # | File | Description |
|---|------|-------------|
| 16 | `conversions-api-overview.md` | CAPI overview — server-side tracking, architecture, benefits vs Pixel |
| 17 | `conversions-api-using.md` | CAPI implementation — payload structure, event creation, test events, batch sending |
| 18 | `conversions-api-parameters.md` | Event and user_data parameters — SHA-256 hashing rules, action_source values |
| 19 | `conversions-api-deduplication.md` | Pixel + CAPI event deduplication — event_id matching, 48-hour window |
| 20 | `conversions-api-best-practices.md` | CAPI best practices — EMQ scoring (1-10), data quality, CAPIG gateway, compliance (LGPD/CCPA) |

### Product Catalog & Dynamic Ads

| # | File | Description |
|---|------|-------------|
| 21 | `catalog.md` | Product catalog management — feed setup, product sets |
| 22 | `dynamic-product-ads.md` | Advantage+ Catalog Ads (DPA) — retargeting and prospecting with product feeds |

### Lead Generation

| # | File | Description |
|---|------|-------------|
| 23 | `lead-ads.md` | Lead Ads — form creation, webhook integration, CRM retrieval |

### Platform & Infrastructure

| # | File | Description |
|---|------|-------------|
| 24 | `authorization.md` | OAuth 2.0 flow, token types (User/System/Page), permissions, access tiers (Standard/Advanced) |
| 25 | `rate-limiting.md` | BUC scoring system — point values, tier limits, QPS mutations, hourly quotas, HTTP headers |
| 26 | `error-reference.md` | Error codes — structured errors, blame_field_specs, common codes (1, 2, 4, 17, 100, 190, 200, 613) |
| 27 | `versioning.md` | API versioning — v25.0 current, release cycle (~3-4 months), deprecation (~2 years) |
| 28 | `business-asset-management.md` | Business Manager — asset management, account sharing, permissions |
| 29 | `best-practices.md` | General API best practices — batching, error handling, pagination |

---

## Processing Status

| Stage | Status | Date |
|-------|--------|------|
| Raw files fetched | COMPLETE | 2026-03-28 |
| Raw copied to sources | COMPLETE | 2026-03-28 |
| SOURCE document created | COMPLETE | 2026-03-28 |
| DNA extraction | PENDING | — |
