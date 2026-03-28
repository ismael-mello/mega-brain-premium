# Ad Image Reference — Meta Graph API v25.0

**Source:** https://developers.facebook.com/docs/marketing-api/reference/ad-image
**Fetched:** 2026-03-28

---

## Overview

This documentation covers uploading and managing images for use in ad creatives through the Facebook Marketing API. Image formats, sizes, and design guidelines depend on your ad type.

## Reading Images

### Endpoint
No parameters required for reading.

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | token (ID) | The image's unique identifier |
| `account_id` | numeric string | Ad account that owns the image |
| `created_time` | datetime | Creation timestamp |
| `creatives` | list<numeric string> | Ad creative IDs using this image |
| `hash` | string | Unique identifier for the image |
| `height` | unsigned int32 | Image height in pixels |
| `is_associated_creatives_in_adgroups` | bool | Association status |
| `name` | string | Filename (max 100 characters) |
| `original_height` | unsigned int32 | Original upload height |
| `original_width` | unsigned int32 | Original upload width |
| `permalink_url` | string | Permanent URL for story creatives |
| `status` | enum | ACTIVE, INTERNAL, or DELETED |
| `updated_time` | datetime | Last update timestamp |
| `url` | string | Temporary retrieval URL (do not use in ad creation) |
| `url_128` | string | 128x128 pixel resized version |
| `width` | unsigned int32 | Image width in pixels |

### Error Codes

| Code | Description |
|------|-------------|
| 100 | Invalid parameter |

## Creating Images

### Upload Methods

**Base64 Bytes Upload:**
```bash
curl \
  -F 'bytes=iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAMAAAAMs7fI...' \
  -F 'access_token=<ACCESS_TOKEN>' \
"https://graph.facebook.com/<API_VERSION>/act_<ACCOUNT_ID>/adimages"
```

**Upload During Ad Creation:**
```bash
curl \
  -F 'campaign_id=<AD_SET_ID>' \
  -F 'creative={"title":"test title","body":"test","object_url":"http://www.test.com","image_file":"test.jpg"}' \
  -F 'test.jpg=@test.jpg' \
  -F 'name=My ad' \
  -F 'access_token=<ACCESS_TOKEN>' \
"https://graph.facebook.com/<API_VERSION>/act_<ACCOUNT_ID>/ads"
```

**Copy Images Between Accounts:**
```bash
curl \
  -F 'copy_from={"source_account_id":"<SOURCE_ACCOUNT_ID>", "hash":"02bee5277ec507b6fd0f9b9ff2f22d9c"}' \
  -F 'access_token=<ACCESS_TOKEN>' \
"https://graph.facebook.com/<API_VERSION>/act_<DESTINATION_ACCOUNT_ID>/adimages"
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `bytes` | Base64 UTF-8 string | Image file content |
| `copy_from` | JSON object | Source account ID and image hash for copying |
| `source_account_id` | numeric string | Source account ID |
| `hash` | string | Image hash identifier |

**Requirements:**
- Include filename extension (e.g., `sample.jpg`, not `sample` or `sample.tmp`)
- User must have read access to source account for copying

### Return Type

```
Map {
  string: Map {
    string: Struct {
      hash: string
      url: string
      url_128: string
      url_256: string
      url_256_height: string
      url_256_width: string
      height: int32
      width: int32
      name: string
    }
  }
}
```

Supports read-after-write functionality.

### Creation Error Codes

| Code | Description |
|------|-------------|
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |
| 200 | Permissions error |
| 368 | Action deemed abusive or disallowed |
| 613 | Rate limit exceeded |
| 80004 | Too many calls to ad account; retry later |

## Updating Images

This operation is not supported on this endpoint.

## Deleting Images

Images must not be actively used in ad creatives for deletion.

### Endpoint
`DELETE /act_{ad_account_id}/adimages`

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `hash` | string | Yes | Image hash to delete |
| `image_id` | string | No | Image ID to delete |

### Return Type

```json
{
  "success": true
}
```

### Deletion Error Codes

| Code | Description |
|------|-------------|
| 100 | Invalid parameter |
| 80004 | Too many calls; retry later |
