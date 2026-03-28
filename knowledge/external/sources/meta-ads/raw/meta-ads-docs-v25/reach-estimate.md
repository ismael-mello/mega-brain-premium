# Reach Estimate API — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/audiences/guides/reach-estimate/
**Fetched:** 2026-03-28

---

## Overview

The Reach Estimate API enables advertisers to obtain audience size estimates for targeting specifications and understand bidding strategies needed to reach specific target groups.

## Basic Usage

```bash
curl -G \
  --data-urlencode 'targeting_spec={
    "geo_locations": {"countries":["US","GB"]},
    "publisher_platforms": ["instagram"],
    "user_os": ["iOS"]
  }' \
  -d 'optimize_for=IMPRESSIONS' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/reachestimate
```

## Key Parameters

- **targeting_spec**: Defines audience targeting criteria including geographic locations, platforms, and device operating systems
- **optimize_for**: Specifies optimization objective (e.g., IMPRESSIONS)
- **access_token**: Required authentication credential

## Endpoints

- `act_{AD_ACCOUNT_ID}/reachestimate` — Reach estimate
- `act_{AD_ACCOUNT_ID}/delivery_estimate` — Delivery estimate
