# Best Practices — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/best-practices
**Fetched:** 2026-03-28

---

## Ad Review and Analysis Triggers

Changes triggering ad review include:
- Creative modifications (images, text, links, videos)
- Targeting adjustments
- Optimization goal or billing event changes

**Note:** Bid, budget, and ad set value modifications do not affect review status. Ads paused before review remain paused after review completion; otherwise they activate upon approval.

## Pagination

For obtaining paginated response data, consult the Pagination of Graph API documentation.

## User Information Storage

Organizations should retain user IDs, session keys, and ad account identifiers for programmatic access. Data handling must comply with Facebook Platform Terms and Developer Policies.

## Suggested Bids

Execute frequent campaign reports, as suggested bids adjust dynamically responding to competing bids using similar targeting.

## Batch Requests

Multiple API calls can be consolidated into single requests using:
- Multiple requests documentation
- Batch requests reference
- ID-based queries: `https://graph.facebook.com/<API_VERSION>?ids=[id1,id2]`
- Field-specific queries: `https://graph.facebook.com/<API_VERSION>?ids=[id1,id2]&fields=field1,field2`

## ETags for Change Detection

Implement ETags to quickly verify response modifications since previous requests.

## Object Archival and Deletion States

Ads have two deletion states: archived and deleted. Archived objects remain queryable by ID; deleted objects don't return through edge queries. Archive up to 5,000 objects simultaneously, then transition to deletion status when no longer needed.

## Testing Environment

The sandbox mode enables read/write API testing without ad delivery. Use Graph API Explorer for experimentation with appropriate permissions (`ads_management` or `ads_read`).

**Limitation:** Sandbox cannot create ads or creatives; use hardcoded IDs for demonstration.

## App Approval Criteria

- Demonstrate value beyond core Facebook solutions (Ads Manager)
- Align with business objectives (sales growth, etc.)

## Policy Compliance

Understand and maintain compliance with:
- Facebook Platform Terms
- Developer Policies
- Promotion Guidelines
- Data Use Policy
- Rights and Responsibilities Statement
- Advertising Guidelines

Most changes feature versioning, with 90-day continuous change windows.
