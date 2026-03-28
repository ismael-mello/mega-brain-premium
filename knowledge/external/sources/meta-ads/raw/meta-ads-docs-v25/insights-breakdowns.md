# Insights Breakdowns — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/insights/breakdowns/
**Fetched:** 2026-03-28

---

## Overview

The Marketing API Insights feature allows you to group results using various breakdown parameters. "Insight values are estimated, with support for estimated and in-development metrics."

## Field Limitations

Several fields cannot be requested with breakdowns:
- `app_store_clicks`
- `newsfeed_avg_position`
- `newsfeed_clicks`
- `relevance_score`
- `newsfeed_impressions`

## Off-Meta Action Metrics Restrictions

**Type 1 Restricted Breakdowns:**
- `region`
- `dma`
- `hourly_stats_aggregated_by_audience_time_zone`
- `hourly_stats_aggregated_by_advertiser_time_zone`

**Type 2 Restricted Breakdowns:**
- `action_device`
- `action_destination`
- `action_target_id`
- `product_id`
- `action_carousel_card_id/action_carousel_card_name`
- `action_canvas_component_name`

Type 1 breakdowns prevent incompatible metrics from returning. Type 2 breakdowns may return web metrics without values or exclude mobile metrics entirely.

## Generic Breakdowns

| Breakdown | Description |
|-----------|-------------|
| `action_device` | Device where conversion occurred |
| `action_canvas_component_name` | Canvas ad component name |
| `action_carousel_card_id` | Specific carousel card ID engaged |
| `action_carousel_card_name` | Carousel card header identifier |
| `action_destination` | Where users land after clicking |
| `action_reaction` | Reaction counts to ads/posts |
| `action_target_id` | Target destination identifier |
| `action_type` | Type of action taken |
| `action_video_sound` | Video sound status (on/off) |
| `action_video_type` | Video metric details |
| `age` | User age ranges |
| `country` | Geographic location |
| `device_platform` | Mobile or desktop |
| `dma` | Designated Marketing Areas (US) |
| `frequency_value` | Ad exposure frequency |
| `gender` | User gender |
| `impression_device` | Device where ad displayed |
| `platform_position` | Ad placement position |
| `publisher_platform` | Facebook, Instagram, Audience Network |
| `region` | Geographic regions |

## Hourly Breakdowns

Two hourly breakdown options are available:
- `hourly_stats_aggregated_by_advertiser_time_zone`
- `hourly_stats_aggregated_by_audience_time_zone`

"Hourly breakdowns are not compatible with fields having prefixes `unique_*`, `reach` or `frequency`."

## Action Breakdowns

When grouping action results, these breakdowns apply:
- `action_device`
- `conversion_destination`
- `matched_persona_id`
- `matched_persona_name`
- `signal_source_bucket`
- `standard_event_content_type`
- `action_type`
- `action_destination`
- `action_reaction`
- `is_business_ai_assisted`

`action_type` adds implicitly if not specified.

## Combining Breakdowns

Due to storage constraints, only specific combinations are permitted (marked with asterisk can group with `action_type`, `action_target_id`, and `action_destination`):

- `action_type *`
- `action_device *`
- `action_device, impression_device *`
- `age, gender *`
- `country *`
- `region *`
- `publisher_platform *`
- `publisher_platform, impression_device *`
- `publisher_platform, platform_position *`
- `hourly_stats_aggregated_by_advertiser_time_zone *`
- `hourly_stats_aggregated_by_audience_time_zone *`
- `action_carousel_card_id/action_carousel_card_name` (various combinations)

## Combination Limitations

- Video fields cannot be requested with hourly breakdowns
- `video_avg_time_watched_actions` incompatible with region breakdowns
- Video actions like `video_p25_watched_actions` unsupported with region

## Dynamic Creative Asset Breakdowns

Creative asset breakdowns support limited metrics:
- `impressions`
- `clicks`
- `spend`
- `reach`
- `actions`
- `action_values`

## Example Request

```bash
curl -G \
  -d "breakdowns=age,gender" \
  -d "fields=impressions" \
  -d "access_token=<ACCESS_TOKEN>" \
  "https://graph.facebook.com/<API_VERSION>/<AD_CAMPAIGN_ID>/insights"
```
