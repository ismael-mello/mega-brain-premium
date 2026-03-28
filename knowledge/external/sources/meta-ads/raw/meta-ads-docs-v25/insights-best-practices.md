# Insights Best Practices & Limits — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/insights/best-practices/
**Fetched:** 2026-03-28

---

## Recent Changes (June 2025)

Starting June 10, 2025, the `reach` field will not be returned in standard queries when breakdowns are applied with `start_date` older than 13 months. This improves API performance.

**Alternative:** Async jobs allow up to 10 daily requests per ad account for reach metrics with breakdowns and extended periods.

## Timeouts

### Common Issues
- Synchronous/GET requests may return memory or timeout errors
- POST/async requests can take up to one hour including retries

### Recommendations
- No explicit limit exists; when timeout occurs, fragment queries using filters and date ranges
- Query unique metrics in separate calls for better performance

## Data Limits Per Call

Two types of limits:
1. **By number of rows** in response
2. **By number of data points** needed to calculate totals

Both apply to sync and async calls, returning: `error_code = 100, CodeException (error subcode: 1487534)`

### Best Practices

- Restrict date range or number of ad IDs
- Limit to necessary metrics or split into multiple queries
- Avoid account-level queries with high-cardinality breakdowns (`action_target_id`, `product_id`) over long periods
- Use `/insights` edge directly on lower-level objects
- Use `filtering` parameter to query only objects with data
- Prefer `date_preset` over custom ranges
- Implement batch requests for multiple calls
- Test with sync calls first; use async if needed
- Data refreshes every 15 minutes and doesn't change after 28 days

## Call Load Limits

The system measures call volume based on required resources, applying a fixed load limit per app per second.

### HTTP Header: x-fb-ads-insights-throttle

```json
{
  "app_id_util_pct": 100,
  "acc_id_util_pct": 10,
  "ads_api_access_tier": "standard_access"
}
```

**Fields:**
- `app_id_util_pct`: Percentage of capacity consumed by application
- `acc_id_util_pct`: Percentage of capacity consumed by ad account
- `ads_api_access_tier`: Access level (`standard_access` or `development_access`)

When limit is reached: `error_code = 4, CodedException`

### Global Volume Limits

In high-load periods, the system may limit requests with: `error_code = 4, error_subcode: 1504022, error_title: Too many API requests`

**Recommendation:** Reduce calls, wait minutes and retry.

### Volume Best Practices

- Distribute `/insights` queries with intervals instead of sending multiple simultaneously
- Monitor response header to moderate calls
- Implement backoff mechanism when reaching ~100% utilization
- Consider ad account timezone when scheduling daily queries
- Check `ads_api_access_tier` (request "advanced access" for higher limits)

## Async Jobs

Three-step process:

### 1. Submit POST Request

```bash
POST /v25.0/<AD_OBJECT>/insights
```

Returns:
```json
{
  "report_run_id": 6023920149050
}
```

**Note:** `report_run_id` expires after 30 days.

### 2. Check Status

Query `async_status` until `Job Completed` and `async_percent_completion` is `100`:

```json
{
  "id": "6044775548468",
  "account_id": "1010035716096012",
  "async_status": "Job Completed",
  "async_percent_completion": 100
}
```

**From v25.0:** If report fails, `error_code`, `error_message`, `error_subcode`, `error_user_title` and `error_user_msg` are returned by default.

### 3. Retrieve Results

```bash
GET /v25.0/<AD_REPORT_RUN_ID>/insights
```

Returns:
```json
{
  "data": [
    {
      "impressions": "9708",
      "date_start": "2009-03-28",
      "date_stop": "2016-04-04"
    }
  ],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MQZDZD"
    }
  }
}
```

### Async Job Status

| Status | Description |
|--------|-----------|
| Job Not Started | Not initiated |
| Job Started | Initiated, not running |
| Job Running | In execution |
| Job Completed | Completed successfully |
| Job Failed | Failed; review and retry |
| Job Skipped | Expired; resubmit |

## Export Reports

Endpoint to export `<AD_REPORT_RUN_ID>` in localized format:

```bash
curl -G \
  -d 'report_run_id=<AD_REPORT_RUN_ID>' \
  -d 'name=myreport' \
  -d 'format=xls' \
  'https://www.facebook.com/ads/ads_insights/export_report/'
```

**Parameters:**
- `name` (string): File name
- `format` (enum): csv or xls
- `report_run_id` (integer): Report ID
- `access_token` (string): Access token

**Warning:** Endpoint is not versioned and may change without notice.

## Discrepancy with Ads Manager

Starting June 10, 2025:
- `use_unified_attribution_setting` and `action_report_time` will be disregarded
- API will match Ads Manager settings:
  - Attributed values based on ad set level settings
  - Inline/in-ad actions included in `1d_click` or `1d_view` window
  - Actions recorded as `action_report_time=mixed`
