# API Versioning — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/overview/versioning
**Fetched:** 2026-03-28

---

## Current Version
The Marketing API current version is **v25.0**.

## Versioning Model
Facebook maintains a primary and extended versioning model. All significant API changes release in new versions, allowing multiple Marketing API versions to coexist with different functionality.

## Deprecation Schedule
New Marketing API versions maintain compatibility with the previous version for **90 days minimum**. During this window, you can make calls to both current and deprecated versions. After expiration, the old version stops functioning, and calls may fail or upgrade automatically.

### Example Timeline
Marketing API v17.0 launched May 23, 2023; v16.0 expired February 6, 2024 — providing the required 90-day transition period.

## Making Versioned Requests
All Marketing API endpoints require explicit versioning via this format:

```
https://graph.facebook.com/v{n}/{request-path}
```

Example request:
```bash
curl -G \
-d "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/v25.0/me/adaccounts"
```

Where `{n}` represents the required version number.

## Key Version Rules

**Unversioned Calls**: Invalid — Marketing API requires explicit version specification (differs from Graph API).

**Backward Compatibility**: Apps can call the latest version available when created, plus any newer undeprecated versions launched subsequently. Apps cannot access versions released before creation.

**Version Persistence**: If unused after creation, apps lose access to original versions when newer ones launch.

## Migrations
Migrations address exceptional scenarios involving fundamental data model changes. They apply across all versions and provide **minimum 90-day windows** for implementation. Active migrations appear on the dedicated migrations page.

### Managing Migrations
- **App Dashboard**: Configure migrations via Settings > Migrations
- **Graph API**: Manage through the `/app` node migrations field
- **Client-Side Override**: Add `migrations_override` parameter with JSON blob:
  ```
  migrations_override={"migration1":true, "migration2":false}
  ```

## Auto-Version Upgrade (May 2024+)
When a version approaches deprecation, unaffected endpoints automatically upgrade to the next available version — avoiding request failures for unchanged functionality.

**Affected Endpoints Don't Auto-Upgrade**: If endpoints change between versions, manual updates remain necessary.

**Response Header**: Auto-upgraded calls include notification header:
```
X-Ad-Api-Version-Warning: 'The call has been auto-upgraded to vXXX as vXXX has been deprecated'
```

**Opt-Out**: Disable via Marketing API App Product Settings.

## Frequently Asked Questions

**Unversioned Calls**: Cannot be made; requests fail without version specification.

**Calling Older Versions**: Possible until deprecation (subject to auto-upgrade rules starting May 2024).

**Difference from Platform API**: Marketing API uses 90-day deprecation; Platform API guarantees 2 years for core APIs.

**Migrations vs. Versioning**: Migrations toggle on/off in settings; versioning embeds directly in endpoint URLs for transparency.

**Multi-Version Auto-Upgrade**: Applies across any deprecated version to next available, potentially skipping intermediate versions if no endpoint changes.

**Manual Upgrades Still Needed**: Yes — despite auto-upgrade, developers should proactively update affected endpoints rather than relying on automatic transitions.
