# Authorization — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/overview/authorization
**Fetched:** 2026-03-28

---

## Overview

The authorization process for Meta's Marketing API involves verifying users and apps, then granting appropriate permissions. This system operates through app roles, access levels, and permission tiers.

## App Roles

Developers can assign roles within the app dashboard including Administrator, Developer, and Tester based on team needs. **Note:** Certain use cases may require app review to obtain specific ad management permissions.

## Access Levels and Permissions Structure

Enterprise apps face an additional Graph API authorization layer called "access levels." During app review, applications must request specific permissions and features.

All developers must comply with Meta's Platform Terms and Developer Policies. Importantly, "API calls at ANY access level target production data."

### Standard vs. Advanced Access

- **Standard Access**: Automatically approved for all available permissions and features; suitable for development and initial workflows
- **Advanced Access**: Requires approval through the app review process

## Key Distinctions for Ad Management

The documentation clarifies that "standard access" in this context differs from the "Standard Access to Ads Management" feature itself. Advanced access under Standard Access to Ads Management still requires app review approval.

### Access Level Requirements

**Standard Access to Ads Management** supports:
- Unlimited ad account management
- Extremely limited volumes per account (development only)
- Limited Business Manager and Catalog APIs
- Creation of one system user plus one admin user

**Advanced Access to Ads Management** supports:
- Unlimited ad account management with proper permissions
- Rate-limited volumes suitable for production
- Full Business Manager and Catalog API access
- Creation of ten system users plus one admin user

## Maintaining Advanced Access

Apps must sustain this status through:
- Minimum 1,500 successful Marketing API calls in the preceding 15 days
- Error rate below 15% over the same period

## Required Permissions

**For single-account management:** `ads_read` and `ads_management` at standard access

**For multi-account management:** Same permissions at advanced access level

### Common Use Cases and Requirements

| Scenario | Permissions | Resource |
|----------|------------|----------|
| Read and manage own ads | `ads_management` | Standard Access to Ads Management |
| Read ad reports only | `ads_read` | Standard Access to Ads Management |
| Multi-account read and manage | `ads_management` + `ads_read` | Standard Access to Ads Management |

## OAuth Scope Implementation

For managing third-party accounts, use the parameter:

```
scope=ads_management
```

With the complete OAuth URL format:
```
https://www.facebook.com/v25.0/dialog/oauth?client_id=YOUR_APP_ID&redirect_uri=YOUR_URL&scope=ads_management
```

**Critical:** Include a trailing slash in the redirect URL.

## Business Verification

Organizations accessing sensitive data must complete business verification to confirm corporate identity, required for certain restricted data categories.
