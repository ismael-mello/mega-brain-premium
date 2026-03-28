# Lookalike Audiences — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/audiences/guides/lookalike-audiences/
**Fetched:** 2026-03-28

---

## Overview

Lookalike audiences take 1-6 hours to fully populate. You can create and run ad sets targeting them immediately; Facebook will adjust delivery once population is complete.

**Endpoint:** `https://graph.facebook.com/{API_VERSION}/act_{AD_ACCOUNT_ID}/customaudiences`

## Creating from Custom Audience

**Requirements:** Seed audience must contain minimum 100 members.

```bash
curl \
  -F 'name=My lookalike audience' \
  -F 'subtype=LOOKALIKE' \
  -F 'origin_audience_id=<SEED_AUDIENCE_ID>' \
  -F 'lookalike_spec={"type":"similarity","country":"US"}' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```

### Key Parameters

| Parameter | Type | Required | Details |
|-----------|------|----------|---------|
| `name` | string | Yes | Audience name |
| `origin_audience_id` | long | Yes | Seed custom audience ID |
| `lookalike_spec.type` | string | Yes | `similarity` or `reach` |
| `lookalike_spec.ratio` | float | Yes | 0.01-0.20 in 0.01 increments |
| `lookalike_spec.country` | string | Yes | Target country code |
| `lookalike_spec.allow_international_seeds` | boolean | No | Default: false |
| `lookalike_spec.starting_ratio` | float | No | Initial percentage range |

### Lookalike Types

- **Similarity:** Top 1% most similar people; smaller reach, higher precision
- **Reach:** Top 5% most similar people; larger reach, lower precision
- **Custom Ratio:** 1-20% in 1% increments

## Creating from Campaign Conversions

**Requirements:** Minimum 100 unique conversions (200+ recommended). Uses up to 180 days of conversion data.

```bash
curl \
  -F 'subtype=LOOKALIKE' \
  -F 'lookalike_spec={"origin_ids":"<CAMPAIGN_ID>","starting_ratio":0.03,"ratio":0.05,"conversion_type":"campaign_conversions","country":"US"}' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```

**Qualified Conversion Types:** Link clicks, Offer claims, Page likes, Canvas app installs, Event responses, Post engagement, Website conversions, Mobile app installs, Mobile app engagement, Video views, Local awareness

## Creating from Page Fans

```bash
curl \
  -F 'subtype=LOOKALIKE' \
  -F 'lookalike_spec={"ratio":0.01,"country":"US","page_id":"<PAGE_ID>","conversion_type":"page_like"}' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```

## Targeting with Lookalikes

```bash
curl \
  -F 'name=My AdSet' \
  -F 'optimization_goal=REACH' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={"custom_audiences":[{"id":"<LOOKALIKE_AUDIENCE_ID>"}],"geo_locations":{"countries":["US"]}}' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```

## Delivery Status

```bash
GET /{lookalike_audience_ID}?fields=delivery_status
```

Ready response:
```json
{
  "delivery_status": {
    "code": 200,
    "description": "This audience is ready for use."
  }
}
```

## Inactive Audiences

Lookalikes unused in active ads for 90 days become inactive:

| Field | Behavior |
|-------|----------|
| `approximate_count` | Returns `-1` |
| `operation_status` | Code `450` (inactive), `100` (expiring), or `471` (flagged) |
| `delivery_estimate` | Returns `-1` |
| `delete_time` | Shows Unix timestamp when audience expires if code `100` |

After 2+ years of non-use: "expiring" status applied automatically. 90 days after expiration flagging: audience deleted.

## Flagged Audiences

If seed audience has `operation_status` of `471`, lookalike creation fails:
```json
{
  "error": {
    "message": "Invalid parameter",
    "code": 100,
    "error_subcode": 1713232,
    "error_user_title": "Seed audience restricted"
  }
}
```

## Future Changes

Meta will eventually remove `location_spec` and `country` from lookalike creation. Location will be defined in campaign targeting specs instead. This change will not affect existing campaigns.
