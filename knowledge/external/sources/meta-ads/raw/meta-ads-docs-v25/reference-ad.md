# Ad (Adgroup) Reference — Meta Graph API v25.0

**Source:** https://developers.facebook.com/docs/marketing-api/reference/adgroup
**Fetched:** 2026-03-28

---

## Overview

The Ad object contains data necessary to visually display an ad and associate it with a corresponding ad set. Each ad is associated with an ad set, and all ads in a set share the same daily or lifetime budget, schedule, and targeting.

**Important Note:** Results from `synchronous_ad_review` do not represent the final decision made during full ad review.

## Political Content Requirements

Advertisers running ads with political content must:
- Complete authorization through a Page admin
- Indicate the ad has political content
- Provide the funding source name
- Have the ad account authorized on the "Issue, Electoral or Political Ads" tab under Page Settings

## Page Mentions

Facebook's ads tools support Page Mentions, but the Marketing API does not provide this functionality. Ads created via API with Page Mentions will succeed but deliver without the mention.

## DSA Compliance (European Union)

For ads targeting EU Digital Services Act regulated locations, set payor/beneficiary information first. Default values (`default_dsa_payor`, `default_dsa_beneficiary`) set in ad accounts auto-fill during copying.

## Youth Targeting Restrictions

Meta stopped showing ads to youth in the EU, EEA, and Switzerland as of November 6, 2023. Existing ad sets targeting youth in these regions pause delivery automatically.

---

## Reading Ads

### By Ad ID

```bash
curl -X GET \
  -d 'fields="id,name"' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_ID>/
```

### By Ad Account

**PHP SDK:**
```php
use FacebookAds\Object\AdAccount;
use FacebookAds\Object\Fields\AdFields;

$account = new AdAccount($account_id);
$ads = $account->getAds(array(AdFields::NAME));

foreach ($ads as $ad) {
  echo $ad->name;
}
```

**Python SDK:**
```python
from facebookads.objects import AdAccount, Ad

account_id = 'act_<AD_ACCOUNT_ID>'
ad_account = AdAccount(account_id)
ad_iter = ad_account.get_ads(fields=[Ad.Field.name])
for ad in ad_iter:
    print ad[Ad.Field.name]
```

**cURL:**
```bash
curl -G \
-d "fields=name" \
-d "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/<API_VERSION>/act_<AD_ACCOUNT_ID>/ads"
```

### By Ad Campaign

```bash
curl -X GET \
  -d 'fields="name"' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_CAMPAIGN_ID>/ads
```

### By Ad Set

**PHP SDK:**
```php
use FacebookAds\Object\AdSet;
use FacebookAds\Object\Fields\AdSetFields;

$adset = new AdSet($adset_id);
$ads = $adset->getAds(array(AdFields::NAME));

foreach ($ads as $ad) {
  echo $ad->name;
}
```

**Python SDK:**
```python
from facebookads.objects import AdSet, Ad

adset_id = <AD_SET_ID>
ad_set = AdSet(adset_id)
ad_iter = ad_set.get_ads(fields=[Ad.Field.name])
for ad in ad_iter:
    print ad[Ad.Field.name]
```

**cURL:**
```bash
curl \
-F "fields=name" \
-F "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/<API_VERSION>/<AD_SET_ID>/ads"
```

---

## Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `date_preset` | enum | today, yesterday, this_month, last_month, this_quarter, maximum, data_maximum, last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, last_week_mon_sun, last_week_sun_sat, last_quarter, last_year, this_week_mon_today, this_week_sun_today, this_year |
| `review_feedback_breakdown` | boolean | Default: false |
| `time_range` | object | Format: {'since':'YYYY-MM-DD','until':'YYYY-MM-DD'} |
| `since` | datetime | Beginning of specified day |
| `until` | datetime | Beginning of following day |

---

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | numeric string | Ad identifier (default field) |
| `account_id` | numeric string | Associated account |
| `ad_active_time` | numeric string | When ad became active |
| `ad_review_feedback` | AdgroupReviewFeedback | Review feedback details |
| `ad_schedule_end_time` | datetime | Ad schedule end |
| `ad_schedule_start_time` | datetime | Ad schedule start |
| `adlabels` | list<AdLabel> | Associated labels |
| `adset` | AdSet | Parent ad set |
| `adset_id` | numeric string | Parent ad set ID |
| `bid_amount` | int32 | Bid amount (deprecated) |
| `bid_info` | map<string, unsigned int32> | Bidding information |
| `bid_type` | enum | CPC, CPM, MULTI_PREMIUM, ABSOLUTE_OCPM, CPA |
| `campaign` | Campaign | Parent campaign |
| `campaign_id` | numeric string | Campaign identifier |
| `configured_status` | enum | ACTIVE, PAUSED, DELETED, ARCHIVED |
| `conversion_domain` | string | Domain where conversions occur |
| `conversion_specs` | list<ConversionActionQuery> | Conversion specifications |
| `created_time` | datetime | Creation timestamp |
| `creative` | AdCreative | Associated creative |
| `creative_asset_groups_spec` | AdCreativeAssetGroupsSpec | Asset group specifications |
| `demolink_hash` | string | Demo link identifier |
| `display_sequence` | int32 | Display order |
| `effective_status` | enum | ACTIVE, PAUSED, DELETED, PENDING_REVIEW, DISAPPROVED, PREAPPROVED, PENDING_BILLING_INFO, CAMPAIGN_PAUSED, ARCHIVED, ADSET_PAUSED, IN_PROCESS, WITH_ISSUES |
| `engagement_audience` | bool | Audience based on engagement |
| `failed_delivery_checks` | list<DeliveryCheck> | Failed delivery validations |
| `issues_info` | list<AdgroupIssuesInfo> | Issue information |
| `last_updated_by_app_id` | id | Last updating application |
| `name` | string | Ad name |
| `preview_shareable_link` | string | Preview link |
| `priority` | unsigned int32 | Display priority |
| `recommendations` | list<AdRecommendation> | Optimization recommendations |
| `source_ad` | Ad | Original ad (if copied) |
| `source_ad_id` | numeric string | Original ad ID |
| `special_ad_categories` | list<enum> | Special category flags |
| `status` | enum | ACTIVE, PAUSED, DELETED, ARCHIVED |
| `targeting` | Targeting | Audience targeting details |
| `tracking_and_conversion_with_defaults` | TrackingAndConversionWithDefaults | Tracking configuration |
| `tracking_specs` | list<ConversionActionQuery> | Tracking specifications |
| `updated_time` | datetime | Last update timestamp |

---

## Edges

| Edge | Type | Description |
|------|------|-------------|
| `adcreatives` | Edge<AdCreative> | Associated creatives |
| `adrules_governed` | Edge<AdRule> | Governing ad rules |
| `copies` | Edge<Adgroup> | Copied ads |
| `insights` | Edge<AdsInsights> | Performance insights |
| `leads` | Edge<UserLeadGenInfo> | Generated leads |
| `previews` | Edge<AdPreview> | Ad previews |
| `targetingsentencelines` | Edge<TargetingSentenceLine> | Targeting descriptions |

---

## Creating Ads

Before creating an ad, ensure you have:
- An existing ad set
- An existing ad creative

**New ads enter pending state and do not run until Facebook approves or rejects them.** After approval, ads run automatically unless the ad set is paused.

### Synchronous Creation

```bash
curl -X POST \
  -F 'name="My Ad"' \
  -F 'adset_id="<AD_SET_ID>"' \
  -F 'creative={"creative_id": "<CREATIVE_ID>"}' \
  -F 'status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```

### Creating Political Ads

```bash
curl -X POST \
  -F 'name="My AdGroup"' \
  -F 'adset_id="<AD_SET_ID>"' \
  -F 'creative={"creative_id": "<CREATIVE_ID>"}' \
  -F 'status="PAUSED"' \
  -F 'authorization_category="POLITICAL"' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```

### Asynchronous Creation

Make an HTTP POST to: `https://graph.facebook.com/{API_VERSION}/act_{AD_ACCOUNT_ID}/asyncadrequestsets`

| Field | Description |
|-------|-------------|
| `name` | Name of ad set for newly created ads (required) |
| `ad_specs` | Array of ad specifications (required) |
| `notification_uri` | URI for async completion notification (optional) |
| `notification_mode` | OFF or ON_COMPLETE (optional) |

For images in ad creative, provide `image_hash` after uploading to: `https://graph.facebook.com/{API_VERSION}/act_{AD_ACCOUNT_ID}/adimages`

### Ad Limits

| Limit | Value |
|-------|-------|
| Ads in regular ad account | 5000 non-deleted ads |
| Ads in bulk ad account | 50000 non-deleted ads |
| Ads in an ad set | 50 non-deleted ads |
| Archived ads in ad account | 100,000 archived ads |

### Creating with Redownload

```bash
curl -X POST \
  -F 'name="My AdGroup with Redownload"' \
  -F 'adset_id="<AD_SET_ID>"' \
  -F 'creative={"creative_id": "<CREATIVE_ID>"}' \
  -F 'redownload=1' \
  -F 'status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```

---

## Copying Ads

**POST Endpoints:**
- `/{ad_id}/copies`
- `/act_{ad_account_id}/ads`

### Copy Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `adset_id` | numeric string or integer | Target ad set ID (optional) |
| `creative_parameters` | AdCreative | Creative overrides (optional) |
| `rename_options` | JSON or object-like arrays | Rename configuration |
| `rename_strategy` | enum | DEEP_RENAME, ONLY_TOP_LEVEL_RENAME, NO_RENAME (default: ONLY_TOP_LEVEL_RENAME) |
| `rename_prefix` | string | Prefix for copied names |
| `rename_suffix` | string | Suffix for copied names |
| `status_option` | enum | ACTIVE, PAUSED, INHERITED_FROM_SOURCE (default: PAUSED) |

### Copy Return Type

```json
{
  "copied_ad_id": "numeric string",
  "success": true
}
```

---

## Creation Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `ad_schedule_end_time` | datetime | Optional end time for individual ad (sales/app promotion campaigns only) |
| `ad_schedule_start_time` | datetime | Optional start time for individual ad (sales/app promotion campaigns only) |
| `adlabels` | list<Object> | Associated ad labels |
| `adset_id` | int64 | Ad set ID (required on creation) |
| `adset_spec` | Ad set spec | Ad set specification (alternative to adset_id) |
| `audience_id` | string | Audience identifier |
| `bid_amount` | integer | Deprecated - use ad set bid_amount |
| `conversion_domain` | string | Domain for conversions (required for pixel-sharing campaigns) |
| `creative` | AdCreative | Creative ID or spec (required) |
| `creative_asset_groups_spec` | string (CreativeAssetGroupsSpec) | Asset groups specification |
| `date_format` | string | Date format specification |
| `display_sequence` | int64 | Display order within campaign |
| `engagement_audience` | boolean | Create audience from engagement |
| `execution_options` | list<enum> | validate_only, synchronous_ad_review, include_recommendations |
| `include_demolink_hashes` | boolean | Include demolink hashes |
| `name` | string | Ad name (required) |
| `priority` | int64 | Display priority |
| `source_ad_id` | numeric string or integer | Original ad ID if copying |
| `status` | enum | ACTIVE or PAUSED during creation only |
| `tracking_specs` | Object | See Tracking and Conversion Specs |

### Execution Options

- `validate_only`: Perform validation without mutation
- `synchronous_ad_review`: Run Ads Integrity validations (must use with validate_only)
- `include_recommendations`: Include optimization recommendations in response

---

## Updating Ads

Update certain fields after creation:

```bash
curl -X POST \
  -F 'name="My New Ad"' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_ID>/
```

### Update Limitations

- Only fields used during creation can be updated
- `adset_id` and `social_prefs` cannot be updated
- Archived ads: only `name` and `status` (to DELETED) are mutable
- Deleted ads: only `name` is mutable
- Ads in ad sets with `creative_sequence` cannot change to PAUSED, ARCHIVED, or DELETED
- Duplicating to new campaign objectives may throw errors

### Status Update Example

```bash
curl -X POST \
  -F 'adgroup_status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_ID>/
```

---

## Deleting Ads

Remove optional field values by updating to empty. Cannot delete ads in ad sets with `creative_sequence` settings.

```bash
curl -X DELETE \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_ID>/
```

### DELETE Return Type

```json
{
  "success": true
}
```

---

## Error Codes

| Code | Description |
|------|-------------|
| 100 | Invalid parameter |
| 104 | Incorrect signature |
| 105 | Number of parameters exceeded maximum |
| 190 | Invalid OAuth 2.0 Access Token |
| 194 | Missing required parameter |
| 200 | Permissions error |
| 270 | Development access level insufficient |
| 368 | Action deemed abusive or disallowed |
| 500 | Message contains banned content |
| 613 | Rate limit exceeded |
| 2500 | Error parsing graph query |
| 2635 | Using deprecated API version |
| 3018 | Start date beyond 37 months from current |
| 80004 | Too many calls to ad-account - retry later |
