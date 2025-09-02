# Research

## Directory Structure

```
research/
├── academic-databases/      # University-provided research databases
├── alternative-investments/ # Private equity, VC, hedge fund data
└── financial-data/         # Public markets and financial datasets
```

## 📚 Academic Databases
Research databases available through university subscriptions.

### [WRDS - Wharton Research Data Services](WRDS-API-Documentation.md)
- **Access**: HBS institutional subscription
- **Coverage**: CRSP, Compustat, IBES, TAQ, OptionMetrics, 600+ datasets
- **Cost**: Free via HBS
- **API**: Python, R, SQL
- **Best for**: Academic empirical research

## 🏦 Alternative Investments
Private markets data providers and APIs.

### [Private Markets APIs](alternative-investments/private-markets-apis/)
Comprehensive analysis of commercial PE/VC data providers:
- **[PitchBook vs Preqin Comparison](API-Comparison-Summary.md)**
- **[PitchBook API](PitchBook-API-Documentation.md)** - $25k+/year, VC/deal focus
- **[Preqin API](Preqin-API-Documentation.md)** - $25k+/year, fund performance focus

## 📈 Financial Data
Public markets data, regulatory filings, and economic indicators.

### [SEC EDGAR API Tools](SEC-EDGAR-API-Documentation.md)
- **Access**: Completely free, no API keys required
- **Libraries**: edgartools, sec-edgar, edgar-crawler
- **Data**: All SEC filings since 1994
- **Best for**: Financial analysis, NLP research, bulk downloads

---

## Quick Decision Guide

### For Academic Research
→ **Use WRDS** (free via HBS, comprehensive historical data)

### For PE/VC Commercial Use
→ **PitchBook** (deals) or **Preqin** (funds) at $25k+/year

### For Startups/Small Budgets
→ **Crunchbase** ($99/month) or **free alternatives**

---
*Last Updated: August 25, 2025*