# SOURCE: Meta Marketing API Documentation v25.0

> **Source ID:** META-ADS-API
> **Version:** v1.0.0
> **Date Fetched:** 2026-03-28
> **API Version:** v25.0 (current)
> **Base URL:** `https://graph.facebook.com/v25.0/`
> **Files:** 29 markdown documents
> **Total Size:** ~143KB
> **Origin:** Official Meta for Developers documentation (developers.facebook.com)

---

## Overview

Complete technical documentation of the Meta Marketing API v25.0, covering the full lifecycle of programmatic advertising across Facebook, Instagram, Messenger, and WhatsApp. This source provides the API reference, best practices, and implementation guides needed to build automated ad management systems.

---

## Topics Covered

### 1. Campaign Hierarchy & CRUD Operations
- **Object model:** Ad Account > Campaign > Ad Set > Ad Creative > Ad
- **6 campaign objectives:** OUTCOME_AWARENESS, OUTCOME_TRAFFIC, OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_APP_PROMOTION, OUTCOME_SALES
- **Full CRUD:** Create, Read, Update, Delete for all objects
- **Special ad categories:** HOUSING, EMPLOYMENT, CREDIT, ISSUES_ELECTIONS_POLITICS
- **Ad Creatives are immutable** after creation (must create new)

### 2. Conversions API (CAPI)
- **Server-side event tracking** complementing browser-side Pixel
- **Endpoint:** `POST /{PIXEL_ID}/events`
- **7 action sources:** website, app, physical_store, phone_call, chat, email, business_messaging
- **SHA-256 hashing** for all PII (email, phone, name, etc.)
- **Deduplication:** Match by `event_name` + `event_id` within 48-hour window
- **Event Match Quality (EMQ):** Score 1-10 based on user data completeness
- **CAPI Gateway (CAPIG):** Auto-converts Pixel events to server-side ($10-100/mo)
- **Business SDKs:** PHP >=7.2, Node.js >=7.6, Java >=8, Python >=2.7, Ruby >=2

### 3. Custom & Lookalike Audiences
- **Custom Audiences:** Upload hashed user data (14+ schema fields)
- **Lookalike Audiences:** Expand from seed audience (min 100 members, 200+ recommended)
- **Lookalike ratio:** 0.01 to 0.20 (1% to 20% of country population)
- **Reach Estimate API** for audience sizing before launch

### 4. Insights API & Breakdowns
- **4 levels:** Account, Campaign, Ad Set, Ad
- **30+ metrics:** impressions, reach, spend, actions, cost_per_action_type, cpm, frequency, etc.
- **Breakdown categories:** Demographic (age, gender), Platform, Geographic, Creative Assets, Action, Product, Temporal
- **Attribution windows:** 1d_click, 1d_view, 7d_click (default), 28d_click, 28d_view
- **Async reports** for large volumes (up to 1 hour processing)
- **Data refresh:** Every 15 minutes; frozen after 28 days

### 5. Rate Limiting (BUC Scoring)
- **Point system:** Read = 1 point, Write = 3 points
- **Development tier:** 60 points max, 300s lockout
- **Standard tier:** 9,000 points max, 60s lockout
- **QPS mutation limit:** 100 requests/second per app-account
- **BUC hourly quotas** per use case (Ads Management, Custom Audiences, Insights, Catalog)
- **HTTP headers** for real-time monitoring (X-Ad-Account-Usage, X-Business-Use-Case)

### 6. Authorization & Access Tiers
- **Token types:** User (~1h), Long-lived (~60 days), System User (never expires), Page
- **OAuth 2.0 flow** with scopes: ads_read, ads_management, business_management
- **Standard tier:** Automatic approval, limited volumes, 1 system user
- **Advanced tier:** Requires App Review, min 1,500 successful calls in 15 days, <15% error rate

### 7. Lead Ads
- Form-based lead capture within Facebook/Instagram
- Webhook integration for real-time lead retrieval
- CRM integration patterns

### 8. Dynamic Product Ads (Advantage+ Catalog Ads)
- Product catalog integration
- Automated creative generation from feed
- Retargeting and prospecting modes

### 9. Error Handling
- **Structured errors:** code, subcode, message, fbtrace_id, blame_field_specs
- **Key codes:** 1 (unknown), 2 (service unavailable), 4 (insights throttle), 17 (user limit), 100 (invalid param), 190 (OAuth invalid), 200/294 (permissions), 613 (account throttle), 80000-80014 (BUC limit)

### 10. API Versioning
- **Current:** v25.0
- **Release cycle:** Every ~3-4 months
- **Deprecation:** ~2 years after launch
- **Best practice:** Always specify version in URL

---

## Key Numerical Thresholds

| Threshold | Value | Context |
|-----------|-------|---------|
| Budget values | In centavos (R$50 = 5000) | Ad Set budget field |
| Custom Audience upload batch | Max 10,000 users per request | `/users` endpoint |
| File audiences per account | 500 max | Custom Audiences |
| Website custom audiences | 10,000 max | Per account |
| Lookalike audiences | 500 max | Per account |
| Mobile app audiences | 200 max | Per account |
| Lookalike seed minimum | 100 members (200+ recommended) | Seed audience |
| Lookalike ratio range | 0.01 - 0.20 (1%-20%) | `lookalike_spec.ratio` |
| Audience retention | Deleted after 2 years unused | Auto-cleanup |
| CAPI batch limit | Max 1,000 events per request | Events endpoint |
| CAPI event_time window | Up to 7 days retroactive (62 for physical_store) | Timestamp validity |
| CAPI deduplication window | 48 hours | Pixel + CAPI match |
| CAPI EMQ target | 8-10/10 (email + phone + name) | Event Match Quality |
| Events Manager visibility | Up to 20 minutes after send | CAPI events |
| Rate limit (Development) | 60 points, 300s lockout | BUC scoring |
| Rate limit (Standard) | 9,000 points, 60s lockout | BUC scoring |
| QPS mutation limit | 100 req/s per app-account | Create/edit operations |
| Budget changes | Max 4/hour per ad set | 1-hour lockout if exceeded |
| Spending limit changes | Max 10/day | Account-level |
| Advanced Access maintenance | 1,500+ calls / 15 days, <15% errors | Tier retention |
| Insights data refresh | Every 15 minutes | Real-time reporting |
| Insights data frozen | After 28 days | Historical data |
| Async report expiry | 30 days | `report_run_id` |
| Reach with breakdowns | 13 months max (unless async, 10 requests/day) | June 2025 change |
| User token lifespan | ~1 hour | Short-lived |
| Long-lived token lifespan | ~60 days | Extended |
| System User token | Never expires | Server-to-server |
| API version lifecycle | ~2 years before deprecation | Versioning |

---

## Key Frameworks & Implementation Patterns

### CAPI Implementation Framework
1. Set up Pixel for browser events
2. Implement server-side CAPI endpoint
3. Generate shared `event_id` (nonce) for deduplication
4. Hash all PII with SHA-256 (lowercase, trimmed)
5. Send both Pixel + CAPI events within 48h window
6. Monitor EMQ score (target 8+)
7. Use `test_event_code` for validation before production

### Audience Building Architecture
1. **Seed:** Upload hashed customer list (Custom Audience)
2. **Expand:** Create Lookalike (1-3% for quality, 5-10% for reach)
3. **Layer:** Combine with detailed targeting (interests, behaviors)
4. **Validate:** Use Reach Estimate API before launch
5. **Refresh:** Update audiences regularly; unused = deleted after 2 years

### Targeting Architecture (3 Layers)
1. **Basic Targeting:** geo_locations, age_min/max, genders, locales
2. **Detailed Targeting:** interests, behaviors, demographics (flexible_spec)
3. **Custom/Lookalike:** First-party data and algorithmic expansion

### Insights Extraction Pattern
1. Start with sync calls for small queries
2. Switch to async for large date ranges or high-cardinality breakdowns
3. Use `filtering` to query only active objects
4. Fragment by date range when timeouts occur
5. Monitor `x-fb-ads-insights-throttle` header
6. Implement exponential backoff on throttling

### Rate Limit Management
1. Monitor X-Ad-Account-Usage and X-Business-Use-Case headers
2. Implement exponential backoff on error codes 4, 17, 613, 80000+
3. Batch requests to reduce point consumption
4. Distribute requests uniformly (avoid bursts)
5. Use async for Insights (decoupled from real-time limits)
6. Cache data that doesn't change (frozen after 28 days)

---

## File Manifest

| # | File | Size | Topic |
|---|------|------|-------|
| 1 | 02-research-report.md | 22.5KB | Complete technical report (all topics) |
| 2 | reference-all-core.md | 25.5KB | Full documentation extract (multi-page) |
| 3 | reference-ad.md | 13.4KB | Ad (Adgroup) API reference |
| 4 | conversions-api-using.md | 6.9KB | CAPI implementation guide |
| 5 | insights-best-practices.md | 5.1KB | Insights limits and async jobs |
| 6 | custom-audiences.md | 5.1KB | Custom Audience creation and management |
| 7 | insights-api.md | 4.4KB | Insights API endpoints and metrics |
| 8 | lookalike-audiences.md | 4.4KB | Lookalike Audience configuration |
| 9 | reference-ad-image.md | 4.3KB | Ad Image upload and reference |
| 10 | insights-breakdowns.md | 4.1KB | Breakdown dimensions and compatibility |
| 11 | conversions-api-best-practices.md | 3.7KB | CAPI best practices and EMQ |
| 12 | conversions-api-parameters.md | 3.7KB | CAPI event and user_data parameters |
| 13 | versioning.md | 3.7KB | API versioning and deprecation |
| 14 | rate-limiting.md | 3.6KB | BUC scoring and throttling |
| 15 | authorization.md | 3.3KB | OAuth, tokens, access tiers |
| 16 | detailed-targeting.md | 2.9KB | Interest/behavior targeting search |
| 17 | basic-targeting.md | 2.8KB | Geographic, age, gender targeting |
| 18 | ads-action-stats.md | 2.6KB | Action stats field reference |
| 19 | best-practices.md | 2.5KB | General API best practices |
| 20 | conversions-api-overview.md | 2.4KB | CAPI overview and architecture |
| 21 | error-reference.md | 2.4KB | Error codes and handling |
| 22 | conversions-api-deduplication.md | 2.4KB | Pixel + CAPI deduplication |
| 23 | lead-ads.md | 2.3KB | Lead form ads and webhooks |
| 24 | getting-started.md | 1.8KB | API setup and first call |
| 25 | catalog.md | 1.5KB | Product catalog management |
| 26 | business-asset-management.md | 1.5KB | Business Manager assets |
| 27 | dynamic-product-ads.md | 1.5KB | Advantage+ Catalog Ads |
| 28 | audiences-overview.md | 1.4KB | Audience types overview |
| 29 | reach-estimate.md | 1.1KB | Reach estimation API |

---

## Raw Files Location

```
knowledge/external/sources/meta-ads/raw/meta-ads-docs-v25/
```

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-03-28 | Initial creation: 29 files from Meta Marketing API v25.0 docs |
