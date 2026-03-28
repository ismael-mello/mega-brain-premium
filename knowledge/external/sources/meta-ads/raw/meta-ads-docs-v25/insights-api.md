# Insights API — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/insights/
**Fetched:** 2026-03-28

---

## Overview

The Insights API offers a unified interface for retrieving ad performance statistics across Meta's advertising ecosystem.

## Prerequisites

Required before beginning:
- `ads_read` permission
- A registered Meta app

## Core Functionality

### Campaign Statistics

Retrieve performance metrics from the last 7 days:

```bash
curl -G \
  -d "date_preset=last_7d" \
  -d "access_token=ACCESS_TOKEN" \
  "https://graph.facebook.com/API_VERSION/AD_CAMPAIGN_ID/insights"
```

### Available API Endpoints

| Endpoint | Purpose |
|----------|---------|
| `act_<AD_ACCOUNT_ID>/insights` | Account-level data |
| `<CAMPAIGN_ID>/insights` | Campaign metrics |
| `<ADSET_ID>/insights` | Ad set performance |
| `<AD_ID>/insights` | Individual ad data |

## Request Parameters

### Field Selection

Specify desired fields using comma-separated values:

```bash
curl -G \
-d "fields=impressions" \
-d "access_token=ACCESS_TOKEN" \
"https://graph.facebook.com/v25.0/<AD_ID>/insights"
```

### Level Aggregation

Group results at specific object levels to eliminate duplication:

```bash
curl -G \
-d "level=ad" \
-d "fields=impressions,ad_id" \
-d "access_token=ACCESS_TOKEN" \
"https://graph.facebook.com/v25.0/CAMPAIGN_ID/insights"
```

## Advanced Features

### Attribution Windows

The API supports multiple attribution windows for conversion tracking:
- `1d_click`: 1-day click window
- `1d_view`: 1-day view window
- `7d_click`: 7-day click window (default)

When unspecified, the system defaults to `7d_click`.

### Sorting Results

```bash
curl -G \
-d "sort=reach_descending" \
-d "level=ad" \
-d "fields=reach" \
-d "access_token=ACCESS_TOKEN" \
"https://graph.facebook.com/v25.0/AD_SET_ID/insights"
```

### Field Expansion

Request nested fields using expansion syntax:

```bash
curl -G \
-d "fields=insights{impressions}" \
-d "access_token=ACCESS_TOKEN" \
"https://graph.facebook.com/v25.0/AD_ID"
```

## Archived and Deleted Objects

Statistics for deleted or archived ads appear when querying parent objects. Default filtering excludes inactive items. To retrieve archived ad statistics:

```bash
curl -G \
  -d "level=ad" \
  -d "filtering=[{'field':'ad.effective_status','operator':'IN','value':['ARCHIVED']}]" \
  -d "access_token=<ACCESS_TOKEN>" \
  "https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/insights/"
```

## Click Metrics Definitions

**Link Clicks** (`actions:link_click`): Clicks directing users to destinations within or outside Meta properties.

**All Clicks** (`clicks`): Encompasses various interaction types including container interactions and expanded ad experiences.

## Ad Labels

Query statistics for ads matching specific label criteria:

```bash
curl -G \
  -d "fields=id,name,insights{unique_clicks,cpm,total_actions}" \
  -d "level=ad" \
  -d 'filtering=[{"field":"ad.adlabels","operator":"ANY", "value":["Label Name"]}]' \
  -d 'time_range={"since":"2015-03-01","until":"2015-03-31"}' \
  -d "access_token=ACCESS_TOKEN" \
  "https://graph.facebook.com/v25.0/AD_OBJECT_ID/insights"
```

## Troubleshooting

### Timeout Issues

Common causes include:
- Excessive request volume
- Memory constraints during processing
- Large data volume extraction

**Recommendations:**
- Break queries into smaller segments using date filters
- Query unique metrics separately for improved performance
- Avoid requesting all metrics simultaneously

### Volume Throttling

Meta applies rate limiting to ensure equitable access.

### Discrepancies with Ads Manager

As of June 10, 2025, changes reduce reporting differences:
- Attributed values follow ad set-level attribution settings
- Inline/in-ad actions included in `1d_click` or `1d_view` windows
- Mixed action report time applied (impressions for Meta actions, conversions for off-platform actions)

## Important Notes

- No explicit query failure threshold exists; timeouts occur when limits are exceeded
- Unique metric calculations are computationally expensive
- Permissions restrict access to specific ad object levels
- The `use_unified_attribution_setting` parameter will be deprecated
