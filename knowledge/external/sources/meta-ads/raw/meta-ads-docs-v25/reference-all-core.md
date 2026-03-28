# Facebook Marketing API - Complete Documentation Extract

## PAGE 1: https://developers.facebook.com/docs/marketing-api

### Marketing API Documentation - Meta for Developers

#### Overview

The Marketing API represents a collection of Graph API endpoints and resources designed to facilitate advertising across Meta's platforms including Facebook, Instagram, Messenger, and WhatsApp.

#### Current Version

The latest API version is **v25.0**. Information about recent updates can be found in the changelog and out-of-cycle changes documentation.

#### Getting Started Resources

##### Basic Ad Creation
Comprehensive guidance covers campaign setup, ad set configuration, and creative development with implementation code examples demonstrating the process workflow.

##### Campaign Management
Documentation explains primary operations including modification, pause functionality, and deletion of active campaigns through the API.

##### Ad Optimization Fundamentals
Resources detail API endpoints serving as essential tools for developer management of audience segments and campaign performance analysis.

#### Related APIs

**Conversions API** - Connects server-side marketing data to Meta systems for targeting optimization, cost reduction, and result measurement.

**Catalog API** - Enables item catalog creation for promotional campaigns, Facebook storefront sales, and additional commerce activities.

**Business Management API** - Supports creation and maintenance of organic and paid presence across Meta platforms.

**Meta Business Extension** - Facilitates business profile connections to third-party platforms with simplified Pixel, Catalog, and storefront configuration.

**Commerce Platform** - Integrates business infrastructure with Meta's product sales tools across platforms and Marketplace features.

#### Available Tools

- Ads Manager portal
- Business Manager interface
- Commerce Manager dashboard
- App Dashboard
- Meta Business SDK
- Marketing API Status monitoring
- Meta Blueprint training
- Developer Community Forums

---

## PAGE 2: https://developers.facebook.com/docs/marketing-api/campaign-structure/

### Meta Marketing API Overview

#### Document Summary

This page introduces Meta's Marketing API, a business tool designed to help developers and marketing professionals automate advertising across Meta's platforms.

#### Core Purpose

The Marketing API enables programmatic management of advertising campaigns. Users can "automate the creation of ads. You can use programming" to generate campaigns, ad sets, and individual ads with real-time performance optimization.

#### Key Capabilities

According to the documentation, you can accomplish the following:

- Update, pause, or delete advertisements without complications
- Keep campaigns aligned with business objectives
- Access detailed performance analytics to guide data-driven improvement decisions

#### Campaign Structure

The API organizes advertising around a hierarchical framework:

**Campaigns** form the highest organizational tier and represent singular goals (example: boosting page post engagement). Setting campaign objectives enforces validation ensuring all contained advertisements align properly.

**Ad Sets** group advertisements together, controlling budget allocation and scheduling duration. All ads within a set must share identical targeting parameters, budget handling, optimization metrics, and durations.

**Ad Creatives** contain only visual advertisement elements and cannot be modified post-creation. Each ad account maintains a creative repository for reuse across multiple advertisements.

**Ads** represent complete advertisement objects with all required information for display across Facebook, Instagram, Messenger, and WhatsApp platforms, including the associated creative asset.

#### Component Alignment Table

The documentation provides a matrix showing which components apply at different hierarchy levels, with checkmarks indicating where objectives, schedules, budgets, bids, audiences, and creatives apply.

---

## PAGE 3: https://developers.facebook.com/docs/marketing-api/reference/

### Facebook Marketing API Reference - Portuguese Documentation

#### Overview

This page provides a comprehensive reference guide for Facebook's Marketing API (v25.0), accessible through Meta for Developers. The content is presented in Portuguese (pt_BR).

#### Root API Nodes

The Marketing API includes six primary root nodes:

| Node | Purpose |
|------|---------|
| `/{AD_ACCOUNT_USER_ID}` | Represents individuals who create advertisements; users can hold roles across multiple ad accounts |
| `/act_{AD_ACCOUNT_ID}` | The business entity managing advertisements |
| `/{AD_ID}` | Contains ad data including creative elements and measurement information |
| `/{AD_CREATIVE_ID}` | Encompasses image, carousel, collection, or video ad formats |
| `/{AD_SET_ID}` | Groups ads sharing identical budget, schedule, bidding, and targeting |
| `/{AD_CAMPAIGN_ID}` | Top-level organizational structure defining campaign objectives; contains one or more ad sets |

#### User Node

**Edges (connections):**
- `/adaccounts` - All associated advertising accounts
- `/accounts` - Pages and locations where the user has administrative access
- `/promotable_events` - Promotional events from managed pages

#### Ad Account Node

Primary edges include:

| Edge | Description |
|------|-------------|
| `/adcreatives` | Defines advertisement appearance and content |
| `/adimages` | Independent image library for creative assets |
| `/ads` | Advertisement data and measurements |
| `/adsets` | Groups with shared budget, schedule, and targeting |
| `/advideos` | Independent video library for creative assets |
| `/campaigns` | Campaign objectives containing ad sets |
| `/customaudiences` | Custom audience segments |
| `/insights` | Performance analytics and reporting |
| `/users` | Associated people with account access |

#### Advertisement Node

**Key edges:**
- `/adcreatives` - Creative specifications
- `/insights` - Performance metrics
- `/leads` - Associated lead data
- `/previews` - Preview generation based on existing ads

#### Ad Set Node

**Key edges:**
- `/activities` - Action history log
- `/adcreatives` - Creative content
- `/ads` - Component advertisements
- `/insights` - Performance analytics

#### Campaign Node

**Key edges:**
- `/ads` - Contained advertisements
- `/adsets` - Associated ad sets
- `/insights` - Campaign performance data

#### Ad Creative Node

**Key edges:**
- `/previews` - Generated ad previews

#### Technical Implementation Details

The page includes substantial JavaScript bootloader configuration, with references to session management, feature flags, and analytics tracking. Multiple resource maps define asset locations and loading strategies.

**Note:** Access to complete reference documentation requires Facebook authentication through the developers portal.

---

## PAGE 4: https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group

### Campaign Documentation - Meta for Developers

#### Overview

A campaign represents the highest organizational level within an ad account and should embody a single advertiser objective, such as driving page post engagement. The campaign objective enforces validation on associated ads to ensure alignment.

#### Key Limits

- **Maximum 200 ad sets per campaign**
- Campaigns with 70+ ad sets using Campaign Budget Optimization cannot modify bid strategy or disable CBO

#### Required Field: Special Ad Categories

All businesses using the Marketing API must identify campaign classification. The `special_ad_categories` parameter accepts an array and is mandatory. Categories include housing, employment, credit, or issues/elections/politics. Businesses without ads in these categories must indicate `NONE` or submit an empty array.

#### Reading Campaign Data

Campaigns support querying with date presets and time ranges. The parameter `date_preset = lifetime` was deprecated in Graph API v10.0, replaced by `date_preset = maximum`, which returns up to 37 months of data.

##### Query Parameters

- `date_preset`: Options include today, yesterday, this_month, last_month, maximum, and various date ranges
- `time_range`: Custom date ranges using {'since':'YYYY-MM-DD','until':'YYYY-MM-DD'}

#### Core Campaign Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | numeric string | Campaign identifier |
| `name` | string | Campaign name (supports emoji) |
| `objective` | string | Campaign goal (validates ad compatibility) |
| `status` | enum | ACTIVE, PAUSED, DELETED, ARCHIVED |
| `budget_remaining` | numeric string | Unspent budget |
| `daily_budget` | numeric string | Daily spending limit |
| `lifetime_budget` | numeric string | Total lifetime spending limit |
| `spend_cap` | numeric string | Maximum campaign spend |

#### Bid Strategy Options

**`LOWEST_COST_WITHOUT_CAP`**: Maximizes results without bid limits; best for cost efficiency but may cause variable average costs

**`LOWEST_COST_WITH_BID_CAP`**: Limits actual bids to specified amounts; provides cost control but may reduce delivery if caps are too restrictive

**`COST_CAP`**: Limits average cost per optimization event to a specified amount

#### Creating Campaigns

##### Required Parameters:
- `name`: Campaign identifier
- `objective`: Campaign goal
- `special_ad_categories`: Array indicating category classification
- `status`: ACTIVE or PAUSED during creation

##### Optional Creation Parameters:
- `daily_budget` or `lifetime_budget` (set one at campaign or ad set level, not both)
- `bid_strategy`: Defaults to LOWEST_COST_WITH_BID_CAP
- `buying_type`: AUCTION (default) or RESERVED
- `promoted_object`: Objects the campaign promotes

##### Example Creation Request

```
POST /v25.0/act_<AD_ACCOUNT_ID>/campaigns
name=My+campaign&objective=OUTCOME_TRAFFIC&status=PAUSED&special_ad_categories=%5B%5D
```

#### Updating Campaigns

Updates occur via POST requests to `/{campaign_id}`. Modifiable fields include:
- Budget (daily or lifetime)
- Status
- Name
- Bid strategy
- Optimization settings

**Budget Toggle Requirements**: When switching between autobid and manual bidding, provide `adset_bid_amounts` mapping.

#### Deleting Campaigns

DELETE requests to `/{campaign_id}` remove campaigns. Bulk deletion supports `delete_strategy` options:
- `DELETE_ANY`: Remove any campaigns
- `DELETE_OLDEST`: Remove oldest first
- `DELETE_ARCHIVED_BEFORE`: Remove archived campaigns before specified date

#### Campaign Objectives

##### Legacy Objectives (Deprecated with v17.0)

Traditional objectives remain supported but are transitioning to Outcome-Driven Ads Experiences (ODAX):
- APP_INSTALLS
- BRAND_AWARENESS
- CONVERSIONS
- EVENT_RESPONSES
- LEAD_GENERATION
- LINK_CLICKS
- MESSAGES
- PAGE_LIKES
- POST_ENGAGEMENT
- PRODUCT_CATALOG_SALES
- REACH
- STORE_VISITS
- VIDEO_VIEWS

##### Newer ODAX Objectives

- OUTCOME_APP_PROMOTION
- OUTCOME_AWARENESS
- OUTCOME_ENGAGEMENT
- OUTCOME_LEADS
- OUTCOME_SALES
- OUTCOME_TRAFFIC

#### Objective Mapping Reference

**BRAND_AWARENESS → OUTCOME_AWARENESS**
- Destination: None specified
- Optimization: AD_RECALL_LIFT or REACH
- Promoted Object: page_id

**LINK_CLICKS → OUTCOME_TRAFFIC**
- Destinations: MESSENGER, WHATSAPP, PHONE_CALL
- Multiple optimization goals available
- Varies by destination type

**POST_ENGAGEMENT → OUTCOME_ENGAGEMENT**
- Destination: ON_POST, ON_PAGE, ON_EVENT, ON_VIDEO
- Supports multiple optimization approaches

**CONVERSIONS → OUTCOME_ENGAGEMENT/OUTCOME_LEADS/OUTCOME_SALES**
- Flexible destination types
- Requires pixel_id and custom_event_type
- Supports messenger, phone call, and web conversions

#### Creative Compatibility

Each objective supports specific ad types:

**APP_INSTALLS**: Image, video, carousel, instant experience, app ads, dynamic creative

**BRAND_AWARENESS**: Image, video, carousel, instant experience, dynamic creative

**CONVERSIONS**: Image, video, carousel, instant experience, collection, app, messenger, offer, dynamic ads

**LEAD_GENERATION**: Image, video, carousel, lead ads, dynamic creative

**LINK_CLICKS**: Broad support including all standard formats plus dynamic ads

**VIDEO_VIEWS**: Video and carousel ads with specific placement restrictions

#### Attribution Specifications

Attribution windows determine conversion tracking methodology:

**CONVERSIONS & PRODUCT_CATALOG_SALES with OFFSITE_CONVERSIONS**:
- 1-day click
- 7-day click
- 1-day click + 1-day view
- 7-day click + 1-day view

**APP_INSTALLS with APP_INSTALLS optimization**:
- 1-day click
- 1-day click + 1-day engaged-view
- 1-day click + 1-day view
- All three combined

#### Placement Compatibility

Placement availability depends on objective-creative combinations:

- **CONVERSIONS**: Supports right_hand_column and story placements (varies by destination)
- **LEAD_GENERATION**: Desktop and mobile feed; story under limited availability
- **LINK_CLICKS**: Comprehensive placement support
- **REACH**: All except right_hand_column
- **POST_ENGAGEMENT/PAGE_LIKES**: No right_hand_column support (as of v3.0)

#### Error Codes

| Code | Meaning |
|------|---------|
| 100 | Invalid parameter |
| 190 | Invalid OAuth token |
| 200 | Permissions error |
| 613 | Rate limit exceeded |
| 2500 | Graph query parsing error |
| 3018 | Start date exceeds 37-month window |
| 80004 | Ad account call throttling |

#### Special Ad Category Details

When creating housing, employment, or credit campaigns, advertisers must comply with targeting restrictions. The `special_ad_category_country` parameter specifies geographic scope using ISO country codes (AC through ZW).

#### Additional Features

**Campaign Copying**: Use the `/copies` edge with options for deep copying child assets, renaming strategies, and status inheritance

**Ad Studies**: Brand lift studies available through the `brand_lift_studies` edge

**Rules Governance**: Ad rules applicable to campaigns accessible via `adrules_governed` edge

**Child Objects**: Access ads and ad sets through `ads` and `adsets` edges

---

## PAGE 5: https://developers.facebook.com/docs/marketing-api/reference/ad-campaign

### Facebook Graph API v25.0: Ad Set Reference Documentation

#### Overview

An ad set is a grouping mechanism for ads that share identical daily or lifetime budgets, scheduling, bidding strategies, and targeting parameters. Ad sets enable advertisers to organize campaigns by specified criteria and retrieve aggregated statistics across associated advertisements.

#### Key Constraints

The platform enforces these operational limits:

| Limit Type | Value |
|-----------|-------|
| Maximum ad sets (regular account) | 5,000 non-deleted sets |
| Maximum ad sets (bulk account) | 10,000 non-deleted sets |
| Maximum ads per ad set | 50 non-archived ads |

#### Recent Policy Updates

**Flagged Custom Audiences and Conversions** (effective September 2, 2025):
- Custom audiences and conversions suggesting health conditions or financial status will be blocked
- Flagged items populate the `issues_info` list with warning codes
- Campaign delivery and performance may suffer until flags are resolved

**EU Digital Services Act Compliance** (effective August 16, 2023):
- Ad sets targeting EU/associated territories require `dsa_payor` and `dsa_beneficiary` fields
- These fields identify who pays for and benefits from the advertisement
- Ads without this information will not publish

#### Core Parameters

##### Budget Configuration
- `daily_budget`: Numeric value in account currency for daily spending
- `lifetime_budget`: Total spending across campaign duration
- `daily_spend_cap` / `lifetime_spend_cap`: Maximum spending limits
- `recurring_budget_semantics`: Boolean determining if daily spend may exceed budget (weekly cap applies)

##### Bidding Strategy
The `bid_strategy` field accepts:
- `LOWEST_COST_WITHOUT_CAP`: Maximize results without bid limiting
- `LOWEST_COST_WITH_BID_CAP`: Cap actual bids at specified `bid_amount`
- `COST_CAP`: Maintain target cost (deprecated in v9+)
- `LOWEST_COST_WITH_MIN_ROAS`: Optimize for return on ad spend

##### Optimization Goals
Supported objectives include: `APP_INSTALLS`, `CONVERSIONS`, `LINK_CLICKS`, `REACH`, `VALUE`, `THRUPLAY`, `LEAD_GENERATION`, `MESSAGING_PURCHASE_CONVERSION`, and numerous others.

##### Billing Events
- `IMPRESSIONS`: Cost per thousand impressions
- `LINK_CLICKS`: Per-click pricing
- `APP_INSTALLS`: Installation-based billing
- `PURCHASE`: Conversion-based billing
- `THRUPLAY`: Video completion or 15-second minimum

#### Reading Ad Sets

**Basic retrieval:**
```
GET /v25.0/{AD_SET_ID}/?fields=name,status
```

**Date format options:**
Use `date_format="U"` parameter to return datetime fields as UNIX timestamps rather than formatted strings.

**Date range parameters:**
- `date_preset`: Predefined ranges (today, last_30d, last_90d, maximum, etc.)
- `time_range`: Custom ranges using `{since: YYYY-MM-DD, until: YYYY-MM-DD}` format
- `since`/`until`: Individual date parameters in YYYY-MM-DD format

#### Creating Ad Sets

##### Minimum Budget Requirements

For `LOWEST_COST_WITHOUT_CAP` strategy:

| Billing Event | Minimum Daily Budget |
|--------------|-------------------|
| Impressions | $0.50 |
| Clicks/Likes/Video Views | $2.50 |
| Low-frequency Actions | $40 (same globally) |

For `LOWEST_COST_WITH_BID_CAP` strategy:
- Impressions: At least the bid_amount value
- Clicks/Actions: 5x the bid_amount

**Geographic multiplier**: Advertisers in Australia, Austria, Belgium, Canada, Denmark, Finland, France, Germany, Greece, Hong Kong, Israel, Italy, Japan, Netherlands, New Zealand, Norway, Singapore, South Korea, Spain, Sweden, Switzerland, Taiwan, UK, and USA face 2x minimum budgets (exception: low-frequency actions without cap).

##### Targeting Considerations

**Locale-targeted page posts**: When promoting locale-targeted Facebook page content, the ad set targeting must match or be a subset of the post's locale targeting.

**Mobile app ads**: Must include `user_device` and `user_os` targeting fields plus `MOBILE_APP_*` campaign objectives.

**Desktop app ads**: Require either `page_types=['desktopfeed']`, `['rightcolumn']`, or `['desktop']` with `CANVAS_APP_*` objectives.

##### EU Targeting Requirements

Ad sets targeting EU locations must supply:
```
{
  "dsa_payor": "<PAYOR_NAME>",
  "dsa_beneficiary": "<BENEFICIARY_NAME>"
}
```

If defaults are configured in the ad account, missing values will auto-populate. Without configured defaults, both fields must be explicitly provided.

#### Regional Regulations

The `regional_regulated_categories` parameter supports region-specific declarations:
- `TAIWAN_FINSERV`: Financial services for Taiwan
- `AUSTRALIA_FINSERV`: Financial services for Australia
- `INDIA_FINSERV`: Securities/investments for India
- `TAIWAN_UNIVERSAL`: General Taiwan targeting
- `SINGAPORE_UNIVERSAL`: General Singapore targeting
- `THAILAND_UNIVERSAL`: General Thailand targeting

Corresponding `regional_regulation_identities` fields specify verified identity IDs for beneficiary/payer roles per category.

#### Housing, Employment, and Credit Ads

The `special_ad_category` field restricts targeting availability for ads in these sectors to prevent discrimination. Advertisers must specify this category, which disables certain demographic and behavioral targeting options.

#### API Limitations and Errors

Common error codes:
- **100**: Invalid parameter
- **190**: Invalid OAuth 2.0 access token
- **200**: Permissions error
- **2635**: Deprecated API version
- **80004**: Rate limiting (wait before retrying)

#### Advanced Features

##### Dynamic Creative Ads
Set `is_dynamic_creative=true` to enable dynamic creative ad creation within the ad set.

##### Learning Stage Information
The `learning_stage_info` field indicates whether ranking/delivery systems are still optimizing, which may affect performance stability.

##### Frequency Control
The `frequency_control_specs` array allows frequency capping for `REACH` and `THRUPLAY` optimization goals, specified with event type, interval days, and maximum frequency.

##### Lookalike Expansion
For ad sets optimizing for value, conversions, or app events, lookalike expansion enables by default (v13.0+) and returns a `lookalike` property within `targeting_optimization_types`.

#### Resolving Flagged Content

**Custom Audiences**: Review in Audience Manager, remove prohibited information, or select different audiences. Request review if flagged in error.

**Custom Conversions**: Choose different conversions not containing health or financial data, or request review through Events Manager.

**Lookalike Audiences**: Resolve underlying seed audience issues or create new lookalikes excluding restricted information.

---

## PAGE 6: https://developers.facebook.com/docs/marketing-api/reference/ad-creative

### Graph API Reference v25.0: Ad Creative Documentation

#### Overview

Ad Creative provides layout and content formatting for advertisements. This documentation covers the Facebook Marketing API's Ad Creative resource for campaign management.

#### Key Requirements

##### Political & Sensitive Ads
Advertisers creating ads about "social issues, elections, and politics must specify `special_ad_categories`" during campaign creation and set `authorization_category` at the creative level.

Beginning January 9, 2024, politically-themed content using digitally created or altered media requires the `POLITICAL_WITH_DIGITALLY_CREATED_MEDIA` authorization category.

#### Field-Level Constraints

| Limit | Value |
|-------|-------|
| Maximum title length | 25 characters (recommended) |
| Minimum title length | 1 character |
| Maximum body length | 90 characters (recommended) |
| Minimum body length | 1 character |
| Maximum URL length | 1000 characters |
| Maximum word length | 30 characters (recommended) |

#### Title & Body Restrictions

- Cannot begin with punctuation marks
- Cannot contain consecutive punctuation (except three periods)
- Only three single-character words permitted
- Disallowed characters include IPA symbols, standalone diacritical marks, superscript/subscript (except ™ and ℠), and: `^~_={}[]|<>`

**Exception:** Link ads cannot use special characters; page post ads allow symbols like ★.

#### Core Fields

##### Identifiers:
- `id`: Numeric string identifier
- `account_id`: Associated ad account
- `actor_id`: Page ID of the creative

##### Content Fields:
- `name`: Creative library name (max 100 characters)
- `body`: Ad text (not supported for video posts)
- `title`: For link ads without page association
- `call_to_action_type`: Button type (extensive enum with 90+ options)

##### Media & Links:
- `image_hash`: Library image reference
- `image_url`: Direct image URL for upload
- `video_id`: Facebook video object ID
- `instagram_permalink_url`: Instagram post URL
- `link_url`: Landing page destination

##### Advanced Options:
- `object_story_spec`: Create unpublished page posts inline
- `asset_feed_spec`: Dynamic creative with multiple variations
- `platform_customizations`: Media per placement (Instagram, Facebook, etc.)
- `degrees_of_freedom_spec`: Enabled transformation types

#### API Operations

##### Reading

Retrieve creative details via GET request:
```
GET /v25.0/<CREATIVE_ID>/?fields=asset_feed_spec
```

**Thumbnail Parameters:**
- `thumbnail_width`: Default 64 pixels
- `thumbnail_height`: Default 64 pixels

##### Creating

POST to `/act_<AD_ACCOUNT_ID>/adcreatives` with required fields. Example for link ads includes `name`, `object_story_spec` with `link_data`, `message`, and `page_id`.

Carousel ads use `child_attachments` within `link_data` for multiple products.

**Branded Content:** Include `sponsored_page_id` (Facebook) or `sponsor_id` (Instagram) for partnership ads.

##### Updating

POST to `/<CREATIVE_ID>` with editable fields:
- `name`: Creative name update
- `status`: Change to ACTIVE, IN_PROCESS, WITH_ISSUES, or DELETED
- `adlabels`: Associated organization labels

Returns success boolean.

##### Deleting

DELETE `/<CREATIVE_ID>` removes the creative. Returns success boolean.

#### Rate Limiting & Limits

- Maximum 50,000 creatives returnable; pagination beyond this unavailable
- Rate limits apply: Error code 80004 indicates temporary throttling
- Error code 613: API rate limit exceeded

#### Related Resources

- App Ads, Video & Carousel Ads, Dynamic Catalog Ads
- Instagram Ads, WhatsApp Click-to-Message, Lead Ads

#### Error Codes

| Code | Message |
|------|---------|
| 100 | Invalid parameter |
| 190 | Invalid OAuth token |
| 200 | Permissions error |
| 270 | Development access level insufficient |
| 613 | Rate limit exceeded |
| 2500 | Graph query parsing error |
| 2635 | Deprecated API version |
| 80004 | Account call limit exceeded |
