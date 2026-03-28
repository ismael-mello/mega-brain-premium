# Error Codes Reference — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/error-reference/
**Fetched:** 2026-03-28

---

## Overview

Comprehensive error code reference for the Meta Marketing API, listing error codes returned by API calls with descriptions and remediation steps.

## Error Code Reference Table

| Code | Description | Notes |
|------|-------------|-------|
| `-` | Internal Facebook errors with negative values | Check `error_subcode` for actual failure code |
| `1` | Unknown error occurred | Can occur when `level` incorrectly set to `adset` instead of `campaign` |
| `4` | App request limit reached | Rate limiting issue |
| `10` | App lacks permission for action | Authorization problem |
| `17` | User request limit reached | Rate limiting issue |
| `100` | Invalid parameter | Multiple subcodes with specific causes |
| `102` | Invalid or expired session key | Authentication issue |
| `104` | Incorrect signature | Validation failure |
| `190` | Invalid OAuth 2.0 access token | Authentication problem |
| `200` | Permission error | Multiple subcodes available |
| `294` | Missing `ads_management` extended permission | Authorization requirement |

## Notable Error Subcodes

**Error 100, subcode 33**: Incompatible POST request — requires system user with proper permissions added to ad account.

**Error 100, subcode 1487694**: Targeting category obsolete — behavioral targeting categories unavailable.

**Error 2708008**: User unauthorized for social/political advertising — identity verification required.

**Error 3858082**: Creative needs enrollment decision — standard enhancements require explicit status declaration.

## blame_field_specs Property

All validation errors include a `blame_field_specs` property indicating which API fields caused failure. Structure example:

```json
"blame_field_specs": [["daily_budget"]]
```

Multiple failing fields indicated as nested arrays showing field path within API specification. For example, nested targeting errors:

```json
"blame_field_specs": [["targeting_spec", "interested_in"]]
```

## Key Implementation Notes

Error handling must use error codes only; description strings may change without notice. The `error_data` blob contains context-specific information for proper error recovery and user feedback.
