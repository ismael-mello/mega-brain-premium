# Rate Limiting — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/overview/rate-limiting/
**Fetched:** 2026-03-28

---

## Overview

The Marketing API operates with its own rate limiting system independent of the Graph API. "A API de Marketing tem a propria logica de limitacao de volume e esta excluida de todos os limites de volume da Graph API."

## Access Tiers

**Development Access**: Default tier with limited quotas
- Max score: 60 points
- Decay rate: 300 seconds
- Lockout duration: 300 seconds when exceeded

**Standard Access**: Enhanced tier with higher quotas
- Max score: 9,000 points
- Decay rate: 300 seconds
- Lockout duration: 60 seconds when exceeded

## Rate Limiting Categories

### Ad Account Level Limits

Standard scoring applies across most operations:
- Read API calls: 1 point each
- Write API calls: 3 points each

Limits are evaluated in real-time within specified time intervals.

### QPS (Queries Per Second) Mutation Limits

Mutation endpoints (create/edit operations) face stricter controls:
- Limit: 100 requests per second per app-account combination
- Applies to: campaign, ad set, and ad creation/modification endpoints
- Purpose: Prevents traffic spikes from overwhelming systems

### Business Use Case (BUC) Quotas

Hourly quotas vary by use case and access tier:

**Ads Management**: 100,000 (Standard) or 300 (Development) + 40 x active ads

**Custom Audiences**: Up to 700,000 (Standard) or 5,000 (Development) + 40 x active audiences

**Ads Insights**: 190,000 (Standard) or 600 (Development) + 400 x active ads - 0.001 x user errors

**Catalog Management**: 20,000 + 20,000 x log2(unique users)

### Specialized Limits

**Spending Changes**: Maximum 10 modifications per day on account spending caps

**Ad Set Budget**: 4 budget modifications per hour per ad set

**App-Level**: Aggregate restrictions based on total app user volume

## Error Handling

Common error codes and responses:

| Error Code | Subcode | Meaning | Typical Cause |
|-----------|---------|---------|---------------|
| 17 | 2446079 | User request limit | Development tier threshold exceeded |
| 613 | 1487742 | Too many calls | Ad account rate exceeded |
| 613 | 5044001 | Mutation rate exceeded | 100 QPS limit breached |
| 4 | 1504022 | App-level throttling | Ads Insights platform limits |

## Mitigation Strategies

**Recommended approaches include**:

- Distributing requests uniformly over time instead of burst patterns
- Consolidating multiple small requests into batch operations
- Implementing exponential backoff when encountering throttling
- Using asynchronous requests for Insights API queries
- Checking HTTP headers for reset timing information

## HTTP Headers

Key response headers provide diagnostic data:

### X-Ad-Account-Usage
Contains account utilization percentage and access tier.

### X-Business-Use-Case
Shows specific BUC limits and CPU/time consumption.

### X-FB-Ads-Insights-Throttle
Insights-specific throttling information:

```json
{
  "app_id_util_pct": 100,
  "acc_id_util_pct": 10,
  "ads_api_access_tier": "standard_access"
}
```

**Fields:**
- `app_id_util_pct`: Percentage of capacity consumed by application
- `acc_id_util_pct`: Percentage of capacity consumed by ad account
- `ads_api_access_tier`: Access level (`standard_access` or `development_access`)

## Upgrade Path

Applications can request Standard tier access to unlock higher quotas and improved lockout behavior through the app dashboard's Advanced Access section.
