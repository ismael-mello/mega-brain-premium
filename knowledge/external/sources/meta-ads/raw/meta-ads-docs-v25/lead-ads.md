# Lead Ads — Meta Marketing API

**Source:** https://developers.facebook.com/docs/marketing-api/guides/lead-ads/
**Fetched:** 2026-03-28

---

## Overview

Lead ads enable businesses to collect customer information through simplified forms on Facebook and Instagram. The forms leverage pre-filled data, streamlining the signup process for potential customers while providing advertisers with quality lead information.

## Prerequisites

Before implementing lead ads, you'll need:

- **Facebook Page**: Establishes your business presence and owns all generated leads
- **Instagram Account** (optional): Required only for running ads on Instagram
- **Facebook App**: Required to access the Marketing API
- **App Review**: Must complete app review with `leads_retrieval` and `pages_manage_ads` permissions
- **Business Verification**: Complete verification after app approval
- **Access Token**: Either user or page tokens work; page tokens are recommended due to volume limits based on active page users

## Key Limitations

**"Apps in development mode cannot retrieve leads"** — only test users with app roles can access leads. Published apps retain full access to all leads.

## Implementation Steps

### 1. Create a Lead Form

Develop the form structure that will appear in your ads, configuring questions and field types.

### 2. Create the Ad

Use either Ads Manager or the Marketing API to create your lead ad, associating it with your form ID.

## Lead Data Integration

### CRM Integration Options

- **Native CRM Partners**: Direct integration with Meta-supported CRM platforms
- **Webhooks**: Real-time lead delivery to your systems using Graph API webhooks
- **Graph API**: Programmatic bulk retrieval of lead data as JSON objects

### Conversions API Integration

Share lead data back to Meta through the Conversions API to improve ad optimization and lead quality scoring.

## Retrieving Leads

Three primary methods exist:

**Bulk Reading**: "Fetch new leads several times daily" via Graph API for periodic synchronization

**Webhooks**: Recommended for CRM integration, delivering leads in real-time as they're submitted

**Meta Business Suite**: Manual download option through the Lead Center
