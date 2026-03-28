# Event Deduplication — Conversions API + Pixel

**Source:** https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events
**Fetched:** 2026-03-28

---

## Overview

Strategies for eliminating duplicates when implementing the Conversions API alongside Meta Pixel — a "redundant configuration" approach.

## Deduplication Options

### 1. Event ID + Event Name (Recommended)

**Required parameter:** `event_id`

Deduplication works by comparing:
- `eventID` from Meta Pixel with `event_id` from Conversions API
- `event` from Meta Pixel with `event_name` from Conversions API

**Implementation Examples:**

Track method:
```javascript
fbq('track', 'Purchase', {value: 12, currency: 'USD'}, {eventID: 'EVENT_ID'});
```

TrackSingle method:
```javascript
fbq('trackSingle', 'SPECIFIC_PIXEL_ID', 'Purchase', {value: 12, currency: 'USD'}, {eventID: 'EVENT_ID'});
```

Image pixel:
```html
<img src="https://www.facebook.com/tr?id=PIXEL_ID&ev=Purchase&eid=EVENT_ID"/>
```

Event without parameters:
```javascript
fbq('track', 'Lead', {}, {eventID: 'EVENT_ID'});
```

### 2. FBP or External ID

**Required parameters:** `event_name`, `fbp` and/or `external_id`

The system automatically removes duplicates when these parameters are consistent between browser and server.

**Process:**
1. Browser event with `event_name`, `fbp` and/or `external_id`
2. Server event with the same parameters
3. Automatic comparison
4. Duplicate removal (preference to first received event)

**Limitations:**
- Deduplication primarily for events sent first by browser, then by server
- 48-hour window for browser to receive events before server
- Does not deduplicate events from the same source (only browser or only server)

## Verification and Validation

"If we find the same combinations of server key (`event_id` and `event_name`) **and** browser key (`eventID` and `event`) sent to the same pixel ID within 48 hours, we will discard subsequent events."

Events are deduplicated only if received within 48 hours after the first event with that `event_id`.

## Technical Requirements

- The `eventID` must be a unique value
- Exact match between identifiers required
- Consistent implementation between browser and server
- Monitoring within the 48-hour period
