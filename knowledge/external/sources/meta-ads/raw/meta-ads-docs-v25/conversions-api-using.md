# Using the Conversions API — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/conversions-api/using-the-api/
**Fetched:** 2026-03-28

---

## Overview

The Conversions API builds on Facebook's Marketing API, which extends the Graph API. Version compatibility is maintained for at least two years, with special exceptions for the Conversions API aligning to Graph API release schedules.

## Sending Requests

### Basic POST Request

Send a POST request to the `/events` endpoint using this path:
```
https://graph.facebook.com/{API_VERSION}/{PIXEL_ID}/events?access_token={TOKEN}
```

### cURL Example

```bash
curl -X POST \
  -F 'data=[{
    "event_name": "Purchase",
    "event_time": 1762902353,
    "user_data": {
      "em": ["309a0a5c3e211326ae75ca18196d301a9bdbd1a882a4d2569511033da23f0abd"],
      "ph": ["254aa248acb47dd654ca3ea53f48c2c26d641d23d7e2e93a1ec56258df7674c4"],
      "client_ip_address": "123.123.123.123",
      "client_user_agent": "$CLIENT_USER_AGENT",
      "fbc": "fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz1234567890",
      "fbp": "fb.1.1558571054389.1098115397"
    },
    "custom_data": {
      "currency": "usd",
      "value": 123.45,
      "contents": [{
        "id": "product123",
        "quantity": 1,
        "delivery_category": "home_delivery"
      }]
    },
    "event_source_url": "http://jaspers-market.com/product/123",
    "action_source": "website"
  }]' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<PIXEL_ID>/events
```

### Request Body Example

```json
{
  "data": [
    {
      "event_name": "Purchase",
      "event_time": 1633552688,
      "event_id": "event.id.123",
      "event_source_url": "http://jaspers-market.com/product/123",
      "action_source": "website",
      "user_data": {
        "client_ip_address": "192.19.9.9",
        "client_user_agent": "test ua",
        "em": ["309a0a5c3e211326ae75ca18196d301a9bdbd1a882a4d2569511033da23f0abd"],
        "ph": [
          "254aa248acb47dd654ca3ea53f48c2c26d641d23d7e2e93a1ec56258df7674c4",
          "6f4fcb9deaeadc8f9746ae76d97ce1239e98b404efe5da3ee0b7149740f89ad6"
        ],
        "fbc": "fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz1234567890",
        "fbp": "fb.1.1558571054389.1098115397"
      },
      "custom_data": {
        "value": 100.2,
        "currency": "USD",
        "content_ids": ["product.id.123"],
        "content_type": "product"
      },
      "opt_out": false
    }
  ]
}
```

## Event Time vs. Load Time

The `event_time` parameter represents when the transaction occurred, sent as a Unix timestamp in seconds. This can be backdated to enable batch processing and server performance optimization.

**Key constraints:**
- The event_time can be up to 7 days before submission to Meta
- Backdated events exceeding 7 days result in rejection of the entire batch
- Physical store events allow backdating up to 62 days after conversion

## Batch Requests

You can send up to 1,000 events in the data parameter. However, Meta recommends sending events immediately after occurrence, preferably within one hour.

**Critical limitation:** If there is one invalid event in the submitted batch, the entire batch will be rejected.

## Hashing Requirements

Review the user data parameters documentation to determine which fields require hashing before transmission. Business SDK implementations handle hashing automatically.

## Event Verification

After sending events, verify receipt in Events Manager:

1. Navigate to **Data Sources** and select your pixel
2. Click **Overview** to see raw, matched, and attributed event counts
3. View connection method in the interface
4. Access specific event details by clicking individual events
5. Allow up to 20 minutes for event visibility

## Test Events Tool

Use the **Test Events** feature in Events Manager to validate server event reception.

```json
{
  "data": [
    {
      "event_name": "ViewContent",
      "event_time": 1764975551,
      "event_id": "event.id.123",
      "event_source_url": "http://jaspers-market.com",
      "user_data": {
        "client_ip_address": "1.2.3.4",
        "client_user_agent": "test user agent"
      }
    }
  ],
  "test_event_code": "TEST123"
}
```

**Important:** The `test_event_code` field should only be used for testing. It must be removed when sending your production payload. Events sent with `test_event_code` are not discarded — they go to Events Manager and are used for ad targeting and measurement.

## Data Processing Options for US Users

### No Explicit LDU Enabling

```json
{
  "data_processing_options": []
}
```

### Enabling Limited Data Use with Meta Geolocation

```json
{
  "data_processing_options": ["LDU"],
  "data_processing_options_country": 0,
  "data_processing_options_state": 0
}
```

### Enabling Limited Data Use with Manual Location (California)

```json
{
  "data_processing_options": ["LDU"],
  "data_processing_options_country": 1,
  "data_processing_options_state": 1000
}
```

## API Rate Limits

The Marketing API has its own throttling logic and is excluded from all Graph API rate limits. No specific rate limit applies to Conversions API calls. The only constraint is the 1,000 event maximum per submission.

## Business SDK Features

### Supported Languages and Versions

- PHP >= 7.2
- Node.js >= 7.6.0
- Java >= 8
- Python >= 2.7
- Ruby >= 2

### Features
- Asynchronous Requests
- Concurrent Batching
- HTTP Service Interface

## Conversions API Gateway Integration

### CAPIGatewayIngressRequest Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `endpointUrl` | String | Gateway endpoint receiving events. Valid URL format required |
| `accessKey` | String | Required access key for the gateway endpoint |

### Available Setters

| Setter | Type | Description |
|--------|------|-------------|
| `setSendToDestinationOnly` | Boolean | If true, events send only to the gateway endpoint. Default: false |
| `setFilter` | CustomEndpointRequest.Filter() | Implements event filtering logic. Default: null |

### PHP Implementation

```php
$event_request = new EventRequest($this->pixel_id);
$capiIngressRequest = new CAPIGatewayIngressRequest($this->cb_url, $this->access_key);
$event_request->setCustomEndpoint($capiIngressRequest);
$event_request->setEvents($events);
$event_request->execute();
```

### Java Implementation

```java
EventRequest eventRequest = new EventRequest(PIXEL_ID, context);
CAPIGatewayIngressRequest capiSyncRequest = new CAPIGatewayIngressRequest(CB_URL, CAPIG_ACCESS_KEY);
eventRequest.setCustomEndpoint(capiSyncRequest);
eventRequest.addDataItem(testEvent);
eventRequest.execute();
```
