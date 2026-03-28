# Conversions API Best Practices — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/conversions-api/best-practices
**Fetched:** 2026-03-28

---

## Implementation

### Account Configuration

When establishing campaigns, simplify account structure:
- Implement learning phase best practices
- Avoid significant campaign edits
- Reduce auction overlap
- Select automatic placements and budget optimization
- Choose appropriate bid strategy for business objectives

### Configure Redundant Events

Use Conversions API as complement to Meta Pixel, sharing the same events through both channels. This allows events potentially lost by Pixel due to connectivity or page load issues to be captured via server.

### Event Deduplication

To avoid duplicate reporting when sending redundant events:
- Both events must have the same `event_name`
- Include `event_id` or combination of `external_id` and `fbp`
- Include all these parameters for appropriate deduplication

### Required Parameters

| Parameter | Type | Requirement |
|-----------|------|------------|
| `action_source` | Server event | All events |
| `event_source_url` | Server event | All website events |
| `client_user_agent` | Client info | All website events |

**Note on `action_source`**: Must be accurate. Should not be `website` for offline events.

Recommended to include `external_id` and `event_id` in all events.

### Client Information Parameters

Send additional parameters to improve event match quality. High-quality parameters include:
- Email address (`em`)
- IP address (`client_ip_address`)
- Name (`fn` and `ln`)
- Phone (`ph`)

### Minimum Matching Requirements

From Graph API v13.0, an event will be considered invalid if it contains ONLY one of these parameter sets:
- `ct` + `country` + `st` + `zp` + `ge` + `client_user_agent`
- `db` + `client_user_agent`
- `fn` + `ge`
- `ln` + `ge`

### fbp and fbc Parameters

These browser cookie values are subject to change. If implemented as user parameters, must be updated regularly. Meta Pixel sets them automatically as first-party cookies.

### Real-Time Sharing

"Sharing events in real time can help your campaigns achieve better results." Consider batch requests for near-real-time sharing.

### Test Events

Use the Test Events tool to:
- Verify server events are configured and received correctly
- Check appropriate deduplication by analyzing processed events
- Debug unusual activity

### Business SDK

Meta Business SDK offers code examples in Python, Java, Ruby, PHP, and Node, reducing required development. Includes automatic parameter hashing.

### Offline Events

Conversions API is the container for all offline events (store sales, phone calls, smart TV actions, offline subscriptions).

**Requirement**: Include appropriate `action_source` parameter (not `website`).

## Partner Best Practices

### Agencies

Partners/agencies sharing events on behalf of advertisers must send a unique `partner_agent` string documenting the platform.

### Website Platforms

Offer Conversions API selectively or via opt-in. Obtain client authorization for sharing data via API when configuring Pixel.

## Post-Implementation

### Verify Event Match Quality (EMQ)

View EMQ score (1-10) for each server event in Events Manager. Indicates efficiency of event matching between client info and Facebook/Meta accounts.

**Availability**: Currently for web events only.

### Run Tests

Recommended testing and optimization:
- **Conversion Lift Study**: Understand incremental impact of server events
- **A/B Test**: Compare campaign strategies for better results
