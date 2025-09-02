# PitchBook API Documentation

## Overview
PitchBook offers programmatic API access with enterprise subscriptions for accessing comprehensive private market data.

## API Access Details

### Authentication
- **Method**: API Key Authentication
- **Header Format**: `authorization: PB-Token {API_KEY}`
- **API Version**: Public API v2
- **Architecture**: RESTful implementation

### Pricing Structure
- **Base Cost**: $24,000-25,000/year for standard 3-user plan
- **Additional Users**: $7,000 per additional seat
- **API Access**: Requires additional API credits (credit-based consumption model)
- **Sales Process**: Mandatory - no self-service signup available

### Available Data Access Methods

#### 1. Direct API
- REST API with real-time access
- Credit-based consumption per request
- Sandbox environment available for testing
- Direct integration with third-party systems

#### 2. Excel & PowerPoint Plugins
- Pull data directly into Office applications
- Included with enterprise subscription
- Custom data analysis and presentation capabilities

#### 3. Chrome Extension
- Quick access to PitchBook data while browsing
- Included with subscription

#### 4. CRM Integration
- Direct integration with existing CRM systems
- Premium add-on feature

## Data Coverage

### Companies
- 3.5M+ private and public companies worldwide
- Valuations and financial histories
- Ownership structures
- Key personnel and board members

### Deals & Transactions
- 1.9M+ deals tracked
- M&A transactions
- Venture capital investments
- Private equity buyouts
- IPOs and exits

### Investors
- 450,000+ investors profiled
- Venture capitalists
- Private equity firms
- Hedge funds
- Limited partners

### Funds
- 110,000+ funds tracked
- Fund performance metrics
- Portfolio holdings
- Terms and conditions
- Fundraising history

## API Endpoints & Capabilities

### Core Data Types Available
- Companies and profiles
- Deals and transactions
- People and executives
- Investors and LPs
- Funds and performance
- Service providers
- Market intelligence

### Use Cases
1. **Due Diligence** - Access comprehensive company and investor profiles
2. **Deal Sourcing** - Identify investment opportunities and trends
3. **Benchmarking** - Compare fund and portfolio performance
4. **Market Research** - Analyze market trends and competitor activity
5. **Fundraising** - Identify potential LPs and track fundraising activity
6. **Portfolio Monitoring** - Track portfolio company performance and exits

## Technical Implementation

### Getting Started
1. Contact PitchBook sales team for demo
2. Estimate API consumption requirements
3. Work with sandbox environment for testing
4. Purchase API credits based on usage estimates
5. Receive production API key
6. Implement authentication in your application

### API Request Example
```http
GET https://api.pitchbook.com/v2/companies/{company_id}
Headers:
  authorization: PB-Token YOUR_API_KEY
```

## Limitations & Considerations

### Access Restrictions
- No free tier or trial available
- Requires enterprise agreement
- API key only provided after sales process
- Usage tracked via credit system

### Data Delivery
- Real-time API access
- Batch data exports available
- Historical data included
- Regular data updates

## Alternatives & Workarounds

### Third-Party Scrapers
Several third-party services offer PitchBook data extraction:
- **Apify PitchBook Scraper**: $19/month + usage
- **Unified.to Integration**: 30-day free trial available
- Note: These may violate PitchBook's terms of service

### Competitor Comparison
- **Crunchbase**: More transparent pricing, starts at $99/month
- **CB Insights**: Similar enterprise pricing model
- **S&P Capital IQ**: Comparable data coverage and pricing

## Contact & Support
- **Sales Inquiries**: Contact required for pricing
- **API Support**: Available to enterprise customers
- **Documentation**: Provided after subscription
- **Sandbox Access**: Available during evaluation

## Key Takeaways
- PitchBook provides comprehensive API access but requires significant investment
- Minimum ~$25k/year commitment plus API credits
- No self-service or trial options available
- Extensive data coverage makes it valuable for serious institutional users
- Consider alternatives if budget is limited or use case is narrow

---
*Last Updated: August 2025*
*Sources: PitchBook pricing pages, API documentation, user reports*