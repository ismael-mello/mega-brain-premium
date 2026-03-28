# Ads Action Stats Reference — Meta Graph API v25.0

**Source:** https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats/
**Fetched:** 2026-03-28

---

## Overview

This endpoint provides statistics for advertising actions tracked through Meta's Graph API. It represents a single action within a Statistics result, with certain fields returned conditionally based on specified breakdowns.

## Important Limitations

"Metrics will not be available" in these scenarios:
- Attempted aggregation across multiple attribution settings
- Requests with impacted breakdowns like age, gender, etc. (applies to off-Facebook and action types only)

**Exception:** Metrics are available when querying with `action_attribution_windows=1d_click,7d_click,1d_view,incrementality` (excluding default windows). Only conversion-type metrics support attribution windows beyond one day.

## Available Fields

### Attribution Window Metrics

The endpoint tracks conversions across multiple time windows:

- **1-day windows:** `1d_click`, `1d_view`, `1d_ev` (engaged view)
- **7-day windows:** `7d_click`, `7d_view`
- **28-day windows:** `28d_click`, `28d_view`

Each window supports variants: standard, `_all_conversions`, and `_first_conversion`.

### Conversion Type Metrics

- `dda` - Data-driven attribution
- `incrementality` - Incremental attribution (supports conversion variants)
- `inline` - On-ad conversions
- `value` - Default attribution window

### Action Breakdown Fields

- `action_type` - Categorizes user interactions (page likes, app installs, purchases, etc.)
- `action_device` - Device where conversion occurred (Desktop, iPhone, Android, etc.)
- `action_destination` - Where users navigate after clicking
- `action_carousel_card_name` - Specific carousel card engaged with
- `action_canvas_component_name` - Component within Canvas ads
- `action_video_type` - Video-specific metrics breakdown
- `action_video_sound` - Audio status during video playback
- `action_reaction` - Emoji reactions on ads/posts
- `action_target_id` - Destination identifier

## Supported Action Types

Includes mobile app events, pixel conversions, and on-Facebook actions such as:
"Mobile App Purchases," "Completed Registration," "Website Adds To Cart," "On-Facebook Purchases," and grouped types like "Omni Purchase" and "All Offsite Leads."

## Operations

- **Reading:** Supported with field specifications
- **Creating:** Not available
- **Updating:** Not available
- **Deleting:** Not available
