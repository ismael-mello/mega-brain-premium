# Basic Targeting — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting/
**Fetched:** 2026-03-28

---

## Demographics and Life Events

### Available Fields

| Field | Type | Description |
|-------|------|-------------|
| `genders` | array | Target by gender: `1` (male), `2` (female), or all (default) |
| `age_min` | integer | Minimum age (default: 18, minimum allowed: 13) |
| `age_max` | integer | Maximum age (maximum allowed: 65) |
| `user_age_unknown` | boolean | Include WhatsApp users with unknown age (WhatsApp Status only) |
| `life_events` | array | Target based on life milestones (e.g., Recently Moved) |
| `industries` | array | Target by industry categories |
| `relationship_statuses` | array | Numeric codes for relationship status targeting |

## Geographic Targeting

### Location Parameters

| Parameter | Details |
|-----------|---------|
| `countries` | ISO country codes (e.g., `['US']`) |
| `regions` | State/province targeting with key codes (limit: 200) |
| `cities` | Target with radius (10-50 miles or 17-80 km) |
| `zips` | Postal codes (limit: 50,000; creates `location_cluster` if exceeds 2,500) |
| `places` | Specific venues/locations (limit: 200) |
| `custom_locations` | Address or lat/long with radius (0.63-50 miles or 1-80 km) |
| `geo_markets` | DMA and Comscore market codes (limit: 2,500) |
| `electoral_districts` | Geographic electoral areas |
| `location_types` | `['home', 'recent']` - defaults to both |
| `country_groups` | Regional groupings like 'asia', 'europe', 'mercosur' |

**Important:** You must specify at least one country in targeting, unless using a custom audience.

## Interest-Based Targeting

Users can target based on timeline activity, page likes, or associated keywords.

```json
"interests": [
  {"id": "6003139266461", "name": "Movies"},
  {"id": "6003397425735", "name": "Tennis"}
]
```

## Behavioral Targeting

Based on digital activities, devices used, purchase intent or previous purchases, and travel.

```json
"behaviors": [
  {"id": "6002714895372", "name": "All frequent travelers"},
  {"id": "6004386044572", "name": "Android Owners (All)"}
]
```

## Special Considerations

- Distinct restrictions apply for housing, employment, credit, social issues, elections, or political ads (US-based)
- `flexible_spec` allows OR logic between criteria groups
- Multi-city targeting available via `custom_type: "multi_city"` with population filters

## API Endpoints

```bash
# Create ad set with targeting
POST /v25.0/act_<AD_ACCOUNT_ID>/adsets

# Targeting search
GET /v25.0/search?type=adinterest|adTargetingCategory|adgeolocation
```
