# Preqin API Documentation

## Overview
Preqin provides comprehensive alternative assets data through two main API offerings: REST API for targeted queries and Feeds API for bulk data transfer.

## API Products

### 1. Preqin API (REST)
**URL**: `https://developer.preqin.com/Preqin-API/`
- RESTful architecture for targeted data queries
- Real-time access to specific data points
- OAuth2 authentication
- Credit-based consumption model

### 2. Preqin Feeds API
**URL**: `https://feeds.preqin.com/`
- Bulk data transfer system
- CSV/file-based delivery
- System-to-system integration
- Delta updates supported (incremental changes)

## Authentication

### OAuth2 Configuration
- **Flow Type**: Password flow (recommended)
- **Scope**: `preqin.feeds.api.v1.default`
- **Base URL**: `https://feeds.preqin.com`
- **Token Type**: Bearer token

## Available Endpoints

### Core Data Categories

#### Investor Data
- Institutional investor profiles
- Commitment tracking
- ESG metrics
- Contact information
- Investment preferences

#### Fund Manager Data
- GP profiles and track records
- Contact details
- Fund management history
- Team information
- ESG compliance

#### Fund Data
- Fund details and terms
- Performance metrics
- Cashflow data
- Portfolio holdings
- Benchmark comparisons

#### Fund Performance
- Historical returns
- IRR, TVPI, DPI metrics
- Quarterly valuations
- Peer group analysis
- Vintage year comparisons

#### Deal Data
- Transaction details
- Buyout deals
- Venture capital investments
- Debt tranches
- Exit information

#### Service Provider Data
- Law firms
- Fund administrators
- Auditors
- Placement agents
- Investment consultants

#### Market Intelligence
- Industry news
- Market trends
- Research reports
- Regulatory updates

## Asset Class Coverage

### Primary Asset Classes
1. **Private Equity (PE)**
   - Buyout funds
   - Growth equity
   - Turnaround/distressed

2. **Venture Capital (VC)**
   - Early stage
   - Late stage
   - Seed funding

3. **Private Debt (PD)**
   - Direct lending
   - Mezzanine
   - Distressed debt

4. **Real Estate (RE)**
   - Core/Core-plus
   - Value-add
   - Opportunistic

5. **Infrastructure (INF)**
   - Core infrastructure
   - Core-plus
   - Value-add/opportunistic

6. **Natural Resources (NR)**
   - Energy
   - Mining
   - Agriculture/Timber

7. **Hedge Funds (HF)**
   - Long/short equity
   - Event-driven
   - Macro strategies

8. **Secondaries**
   - LP portfolio sales
   - GP-led transactions
   - Direct secondaries

## Data Specifications

### Coverage Statistics
- **Companies**: 3.5M+ private and public
- **Investors**: 450,000+ institutional
- **Fund Managers**: 110,000+ active
- **Funds**: 53,000+ private capital, 39,900+ hedge funds
- **Deals**: 485,000+ transactions
- **Service Providers**: 6,800+ firms

### Data Collection
- 450+ multi-lingual analysts globally
- Direct contact with industry professionals
- Regular verification and updates
- Proprietary research methodology

## Feed Types & Formats

### Available Feed Endpoints
```
/api/company/currentinvestor    # Current investor data
/api/company/dealbuyout         # Buyout deal data
/api/company/dealvc             # VC deal data
/api/company/financial          # Company financials
/api/fund/{assetclass}          # Fund data by asset class
/api/fundperformance/{assetclass} # Performance metrics
/api/cashflow/{assetclass}      # Cashflow data
/api/investor/{assetclass}      # Investor profiles
/api/fundmanager/{assetclass}   # Fund manager data
/api/deal/debttranches          # Debt tranche details
/api/serviceprovider/{type}    # Service provider data
/api/esg/investor               # ESG investor metrics
/api/esg/fundmanager            # ESG fund manager data
/api/esg/fund                   # ESG fund metrics
```

### Delta Updates
- Retrieve only changed data since last call
- Format: `?deltaDate=YYYYMMDD`
- Supports up to 1 month of historical deltas
- Reduces data transfer and processing overhead

## Implementation Resources

### Documentation Files
1. **Data Dictionary** (.xlsx)
   - Field definitions
   - Data types
   - Enumeration values

2. **Implementation Guide** (.docx)
   - Setup instructions
   - Best practices
   - Integration patterns

3. **API Schema** (.xlsx)
   - Endpoint specifications
   - Request/response formats
   - Error codes

## Use Cases

### Investment Research
- Fund due diligence
- Manager selection
- Performance benchmarking
- Peer analysis

### Deal Sourcing
- Identify active investors
- Track recent transactions
- Monitor exit activity
- Analyze valuation trends

### Portfolio Management
- Performance tracking
- Risk assessment
- Exposure analysis
- Reporting automation

### Market Intelligence
- Fundraising trends
- LP activity monitoring
- Competitive analysis
- Regulatory tracking

### Risk & Compliance
- ESG monitoring
- Regulatory reporting
- Investment limits tracking
- Concentration analysis

## Pricing & Access

### Subscription Model
- Enterprise pricing only
- Contact sales for quotes
- No public pricing available
- Based on:
  - Number of users
  - Data coverage needed
  - API usage volume
  - Additional features

### Access Requirements
- Sales consultation required
- Demo and needs assessment
- No self-service option
- No free trial available

### AWS Marketplace
- Some datasets available
- Pay-as-you-go pricing
- Limited compared to full API
- Good for specific use cases

## Technical Considerations

### Rate Limits
- Not publicly documented
- Discussed during sales process
- Credit-based system
- Enterprise agreements specify limits

### Data Formats
- JSON for REST API
- CSV for Feeds API
- Excel exports available
- Custom formats negotiable

### Update Frequency
- Varies by data type
- Real-time for some metrics
- Daily/weekly for others
- Historical data included

## Integration Best Practices

### Initial Setup
1. Define data requirements
2. Estimate usage volume
3. Contact Preqin sales
4. Test in sandbox environment
5. Implement authentication
6. Build data pipeline
7. Monitor usage/credits

### Data Management
- Implement caching strategies
- Use delta updates when possible
- Store historical data locally
- Build reconciliation processes
- Monitor data quality

## Support & Resources

### Developer Support
- **Email**: apiqueries@preqin.com
- **Documentation**: developer.preqin.com
- **Account Management**: Via sales rep
- **Technical Support**: Enterprise customers only

### Additional Tools
- Excel plugins available
- PowerBI connectors
- Tableau integration
- Custom integrations supported

## Comparison with Competitors

### vs PitchBook
- Similar coverage and pricing
- Preqin stronger in fund performance
- More transparent API documentation
- Better hedge fund coverage

### vs Crunchbase
- Preqin more institutional focused
- Deeper performance data
- Higher price point
- Less startup/tech focus

### vs S&P Capital IQ
- Preqin specialized in alternatives
- S&P broader market coverage
- Similar enterprise pricing
- Different data strengths

## Key Advantages
- Comprehensive alternative assets coverage
- Strong fund performance data
- Global data collection network
- ESG metrics integration
- Established industry reputation

## Limitations
- High cost barrier
- No self-service option
- Complex sales process
- Limited trial access
- Enterprise-only focus

---
*Last Updated: August 2025*
*Sources: Preqin developer documentation, API specifications, market research*