# Detailed Targeting — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting/
**Fetched:** 2026-03-28

---

## Overview

The Detailed Targeting API enables searching multiple targeting types simultaneously with a single request.

## Response Fields

All endpoints return standardized targeting data:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Target audience identifier |
| `name` | string | Audience name |
| `audience_size_lower_bound` | integer | Minimum estimated audience size |
| `audience_size_upper_bound` | integer | Maximum estimated audience size |
| `path` | string array | Category hierarchy including parent categories |
| `description` | string | Brief audience description |

**Note:** Results with fewer than 2,000 people are filtered by default across: `work_employers`, `work_positions`, `education_majors`, `education_schools`.

## Search Endpoint

```bash
curl -G \
-d "q=harvard" \
-d "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<API_VERSION>/act_<AD_ACCOUNT_ID>/targetingsearch
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `q` | string | Yes | Search query string |
| `limit` | integer | No | Number of results to return |
| `limit_type` | string | No | Filter by type: `interests`, `education_schools`, `education_majors`, `work_positions`, `work_employers`, `relationship_statuses`, `college_years`, `education_statuses`, `family_statuses`, `industries`, `life_events`, `behaviors`, `income` |
| `locale` | string | No | Locale for names/descriptions |

## Suggestions Endpoint

```bash
curl -G \
-d "targeting_list=[{'type':'interests','id':6003263791114}]" \
-d "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<API_VERSION>/act_<AD_ACCOUNT_ID>/targetingsuggestions
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `targeting_list` | array | Yes | Array of `{'type':'{TYPE}', 'id':{ID}}` pairs |
| `limit` | integer | No | Number of results (default: 30, max: 45) |

## Browse Endpoint

```bash
curl -G \
-d "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<API_VERSION>/act_<AD_ACCOUNT_ID>/targetingbrowse
```

## Validation Endpoint

```bash
curl -G \
-d "targeting_list=[{'type':'interests','id':6003283735711}]" \
-d "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<API_VERSION>/act_<AD_ACCOUNT_ID>/targetingvalidation
```

Additional response field: `valid` (boolean) — indicates whether the audience is valid for targeting.

Input (provide at least one):
- `targeting_list` — Array of type/id pairs (preferred)
- `id_list` — Array of IDs
- `name_list` — Array of strings (interests only, case-insensitive)
