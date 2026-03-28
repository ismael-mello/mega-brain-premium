# Conversions API Overview — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/conversions-api/
**Fetched:** 2026-03-28

---

## Overview

The Conversions API connects advertiser marketing data (website events, app events, business messaging events, and offline conversions) from a server, website, platform, app, or CRM to Meta's systems for ad targeting optimization, cost reduction, and results measurement.

Instead of maintaining separate connection points for different data sources, advertisers can use a single API to send multiple event types and simplify their technology stack. Server events link to a dataset ID and process similarly to Meta Pixel, Facebook SDK for iOS/Android, Partner Metrics SDK for Apps, offline event sets, or CSV uploads — enabling use for measurement, reporting, and ad optimization across channels.

## Getting Started

1. **Choose Integration Method**: Select the approach best suited to your needs and review prerequisites
2. **Implement & Send Requests**: Make POST requests and understand event discarding, batch requests, and event transaction timing
3. **Verify Setup**: Confirm event receipt, deduplication, and proper matching

## Core Features

**Multiple Event Types Supported**:
- Website events
- App events
- Business messaging events
- Offline conversions

**Key Capabilities**:
- Server-to-Meta direct integration
- Event deduplication and matching
- Measurement and reporting
- Ad optimization across channels
- Offline event attribution
- Custom audience creation

## Documentation Sections

- **Parameters**: Required and optional parameters for improving ad attribution and delivery optimization
- **Payload Helper**: Guidance on payload structure when sending from your server to Facebook
- **Troubleshooting**: Error code management and resolution
- **Offline Events**: Tracking conversions from offline sources
- **App Events**: Integration for mobile application tracking
- **Business Messaging**: Event tracking for business communications
- **Best Practices**: Recommendations for optimal performance and measurement

## Additional Resources

- Meta Pixel event documentation (standard and custom events)
- Business Help Center articles on Conversions API
- Direct integration playbook (PDF)
- Data processing options and Limited Data Use implementation
