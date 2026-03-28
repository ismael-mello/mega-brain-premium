# Conversions API Parameters — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/
**Fetched:** 2026-03-28

---

## Overview

All required and optional parameters for Meta's Conversions API, which supports web, app, offline, and business messaging events.

## Key Requirements

**Web Events** require three parameters:
- `client_user_agent`
- `action_source`
- `event_source_url`

**Non-Web Events** require only:
- `action_source`

Users must ensure the `action_source` parameter accurately reflects the event's true origin.

## Main Body Parameters

### `data`
Container for event information being transmitted to Meta.

### `test_event_code`
Identifier for testing event configurations without affecting live campaign metrics.

## Customer Information Parameters

### Hashed Parameters (SHA-256 required)

| Parameter | Description |
|-----------|-------------|
| `em` | Email |
| `ph` | Phone number |
| `fn` | First name |
| `ln` | Last name |
| `ge` | Gender |
| `db` | Birth date |
| `ct` | City |
| `st` | State |
| `zp` | Postal code |
| `country` | Country |
| `external_id` | External ID (recommended hashing) |

### Non-Hashed Parameters

| Parameter | Description |
|-----------|-------------|
| `client_ip_address` | Client IP address |
| `client_user_agent` | Client user agent |
| `fbc` | Click identifier |
| `fbp` | Browser identifier |
| `subscription_id` | Subscription ID |
| `fb_login_id` | Facebook Login ID |
| `lead_id` | Lead ID |
| `page_id` | Page ID |
| `page_scoped_user_id` | Page-scoped user ID |
| `ctwa_clid` | WhatsApp click ID |
| `ig_account_id` | Instagram account ID |
| `ig_sid` | Instagram click ID |

### App-Only Parameters

| Parameter | Description |
|-----------|-------------|
| `anon_id` | Installation ID |
| `madid` | Mobile advertising identifier |

## Server Event Parameters

### Core Event Fields

| Field | Description |
|-------|-------------|
| `event_name` | The action being tracked |
| `event_time` | Unix timestamp of occurrence |
| `user_data` | Customer information object |
| `custom_data` | Additional business metrics |
| `event_source_url` | Page URL generating the event |
| `event_id` | Unique event identifier for deduplication |
| `action_source` | Origin classification (website, app, offline, etc.) |

### Privacy & Compliance

| Field | Description |
|-------|-------------|
| `opt_out` | User opt-out signal |
| `data_processing_options` | Array for limited data processing |
| `data_processing_options_country` | Geographic restriction |
| `data_processing_options_state` | State-level restrictions |

### Additional Fields

| Field | Description |
|-------|-------------|
| `referrer_url` | Previous page URL |
| `customer_segmentation` | User classification data |

## App-Specific Parameters

| Parameter | Description |
|-----------|-------------|
| `advertiser_tracking_enabled` | User tracking consent |
| `application_tracking_enabled` | App-level tracking status |
| `extinfo` | Extended information array |
| `campaign_ids` | Marketing campaign identifiers |
| `install_referrer` | App installation source |
| `installer_package` | Distribution channel |
| `url_schemes` | App deep linking information |
| `windows_attribution_id` | Windows device identifier |
| `vendor_id` | iOS identifier |

## Original Event Data Parameters

For tracking original conversion events:

| Field | Description |
|-------|-------------|
| `event_name` | Original event name |
| `event_time` | Original event time |
| `order_id` | Order identifier |
| `event_id` | Original event ID |
