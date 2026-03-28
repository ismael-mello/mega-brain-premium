# Custom Audiences — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/audiences/guides/custom-audiences/
**Fetched:** 2026-03-28

---

## Overview

Meta's Marketing API enables creation of custom audiences based on customer information.

## Upcoming Changes (September 2, 2025)

Meta will implement proactive restrictions on custom audiences suggesting impermissible information:
- **Flagged Content Examples**: Specific health conditions (arthritis, diabetes) or financial status (credit scores, high income)
- **Impact**: Flagged audiences cannot be used for new campaigns
- **API Signal**: `operation_status` will return `471` for flagged audiences

## Supported Data Types

- Email addresses
- Phone numbers
- Names and dates of birth
- Gender and location
- App user IDs (Apple IDFA, Android Advertising ID)
- CRM system identifiers

## Core Process

### Step 1: Create Empty Audience

```bash
curl -X POST \
  -F 'name="My Custom Audience"' \
  -F 'subtype="CUSTOM"' \
  -F 'description="Purchase history"' \
  -F 'customer_file_source="USER_PROVIDED_ONLY"' \
  -F 'access_token=<TOKEN>' \
  https://graph.facebook.com/v25.0/act_<ACCOUNT_ID>/customaudiences
```

**Customer File Source Options:**
- `USER_PROVIDED_ONLY`: Data collected directly from customers
- `PARTNER_PROVIDED_ONLY`: Data from external partners
- `BOTH_USER_AND_PARTNER_PROVIDED`: Mixed sources

### Step 2: Add Users

POST to `/{audience_id}/users` endpoint with hashed data (max 10,000 per request):

```json
{
  "session": {
    "session_id": 123456,
    "batch_seq": 1,
    "last_batch_flag": true,
    "estimated_num_total": 5000
  },
  "payload": {
    "schema": ["EMAIL", "FN", "LN"],
    "data": [
      ["<SHA256_EMAIL>", "<SHA256_FN>", "<SHA256_LN>"]
    ]
  }
}
```

## Data Hashing Requirements

All PII must use SHA256 hashing in lowercase hexadecimal format.

### Normalization Guidelines

| Field | Rules |
|-------|-------|
| EMAIL | Trim whitespace, lowercase |
| PHONE | Remove symbols/letters/leading zeros; add country code prefix |
| GEN | Use `m` (male) or `f` (female) |
| DOBY | Format YYYY (1900-current year) |
| DOBM | Format MM (01-12) |
| DOBD | Format DD (01-31) |
| FN/LN | Lowercase a-z only, no punctuation |
| ST | ANSI two-character code, lowercase |
| CT | Lowercase, no punctuation/spaces |
| ZIP | Lowercase, no spaces; US=5 digits only |
| COUNTRY | ISO 3166-1 alpha-2 codes |

**EXTERN_ID:** Do not require hashing but must maintain consistent formatting.
**MADID:** Do not hash; use lowercase with hyphens intact.

## Limited Data Use (LDU)

```json
{
  "payload": {
    "schema": ["EMAIL", "DATA_PROCESSING_OPTIONS"],
    "data": [
      ["<HASHED_EMAIL>", ["LDU"]]
    ]
  }
}
```

With manual location:
```json
{
  "payload": {
    "schema": ["EMAIL", "DATA_PROCESSING_OPTIONS", "DATA_PROCESSING_OPTIONS_COUNTRY", "DATA_PROCESSING_OPTIONS_STATE"],
    "data": [["<HASHED_EMAIL>", ["LDU"], 1, 1000]]
  }
}
```

## Multi-Key Matching

```bash
curl \
  -F 'payload={
    "schema": ["FN", "LN", "EMAIL"],
    "data": [
      ["<HASH>", "<HASH>", "<HASH>"]
    ]
  }' \
  -F 'access_token=<TOKEN>' \
  https://graph.facebook.com/<VERSION>/<AUDIENCE_ID>/users
```

## Removing Users

### Individual Removal
```bash
curl -X DELETE \
  --data-urlencode 'payload={"schema": "EMAIL_SHA256", "data": ["<HASH1>", "<HASH2>"]}' \
  -d 'access_token=<TOKEN>' \
  https://graph.facebook.com/<VERSION>/<AUDIENCE_ID>/users
```

### Bulk Account Removal
```bash
DELETE /act_<ACCOUNT_ID>/usersofanyaudience
```

## User Replacement API

The `/{audience_id}/usersreplace` endpoint enables atomic replacement without resetting learning phases.

**Constraints:**
- Audience must have fewer than 100 million users
- Cannot convert between value-based and non-value-based audiences
- Only one replacement operation at a time
- 90-minute session window maximum

### Replacement Status Codes

| Code | Error | Action |
|------|-------|--------|
| 1870145 | Update in progress | Wait for "Normal" status |
| 1870158 | Timeout reached | Use ADD operation after completion |
| 1870147 | Invalid batch sequence | Start batch_seq at 1 |
| 1870159 | Operation completed | Wait before adding more data |
| 1870144 | Audience too large | Audience exceeds 100M users |

## Common Error Codes

| Code | Subcode | Issue | Resolution |
|------|---------|-------|------------|
| 100 | 1713098 | Invalid JSON format | Validate schema/parameters |
| 200 | 1870050 | Permission denied | Link ad account to Business Manager |
| 200 | 1870090 | Terms not accepted | Accept Custom Audience ToS |

## Audience Limits

- Standard Data File: 500 audiences per account
- Website Custom Audiences: 10,000
- Mobile App Audiences: 200
- Lookalike Audiences: 500

## Expiration Policy

File-based custom audiences unused in active ad sets for 2+ years are periodically flagged for deletion.
