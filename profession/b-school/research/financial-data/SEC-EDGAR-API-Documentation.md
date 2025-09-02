# SEC EDGAR API Documentation

## Overview
The SEC EDGAR (Electronic Data Gathering, Analysis, and Retrieval) database provides free public access to corporate filings required by the U.S. Securities and Exchange Commission. This document covers three powerful Python libraries for programmatic access to EDGAR data.

## Quick Comparison Matrix

| Feature | sec-edgar | edgartools | edgar-crawler |
|---------|-----------|------------|---------------|
| **Purpose** | Bulk download filings | Modern API & analysis | Extract structured text |
| **Ease of Use** | Medium | Easy | Complex |
| **Installation** | `pip install secedgar` | `pip install edgartools` | Manual setup |
| **Best For** | Mass downloads | Financial analysis | NLP/Text mining |
| **API Design** | Class-based | Modern Python | Script-based |
| **Data Format** | Raw HTML/XML | DataFrames/Objects | Structured JSON |
| **Financial Statements** | ❌ | ✅ Parsed | ❌ |
| **XBRL Support** | ❌ | ✅ Full | ❌ |
| **Text Extraction** | Basic | Advanced | Specialized |
| **Async Support** | ✅ | ✅ | ❌ |
| **Rate Limiting** | Manual | Automatic | Manual |
| **Documentation** | Good | Excellent | Academic |
| **Active Development** | Moderate | Very Active | Academic |
| **License** | Apache-2.0 | MIT | GPL-3.0 |

## 1. edgartools - Modern & Comprehensive
*Best for: Financial analysis, clean API, quick prototyping*

### Installation
```bash
pip install edgartools
```

### Key Features
- **Intuitive API** - Clean, Pythonic interface
- **Financial Statement Parsing** - Automatic extraction to DataFrames
- **XBRL Support** - Full parsing of structured data
- **Smart Objects** - Each filing type has specialized methods
- **LLM-Ready** - Text extraction optimized for AI
- **Automatic Rate Limiting** - No SEC blocks

### Basic Usage
```python
from edgar import *

# Setup (required by SEC)
set_identity("your.email@example.com")

# Get company
company = Company("AAPL")  # or CIK: "0000320193"

# Get filings
filings = company.get_filings()
tenk = filings.filter(form="10-K")[0]

# Get financials directly
financials = company.get_financials()
income_stmt = financials.income_statement()
balance_sheet = financials.balance_sheet()
cash_flow = financials.cashflow_statement()

# Work with specific filing
filing = tenk.obj()  # Convert to specialized object
print(filing.business)  # Item 1
print(filing.risk_factors)  # Item 1A
print(filing.mda)  # Item 7

# Get clean text
text = filing.text()  # Clean text for NLP
html = filing.html()  # Original HTML
```

### Advanced Features
```python
# Insider transactions
form4 = filings.filter(form="4")[0].obj()
for transaction in form4.transactions:
    print(f"{transaction.date}: {transaction.shares} shares @ ${transaction.price}")

# Fund holdings (13F)
holdings = filings.filter(form="13F-HR")[0].obj()
for holding in holdings.holdings:
    print(f"{holding.issuer}: {holding.value:,}")

# Search all filings
filings = get_filings(form="8-K", date="2024-01-01:")
```

### Strengths
- Most user-friendly API
- Best documentation and examples
- Automatic financial statement extraction
- Built-in data visualization support
- Active development & community

### Limitations
- Newer library (less battle-tested)
- May not handle edge cases in old filings
- Focused on common filing types

---

## 2. sec-edgar - Reliable Bulk Downloads
*Best for: Downloading many filings, archival, research datasets*

### Installation
```bash
pip install secedgar
```

### Key Features
- **Bulk Downloads** - Efficiently download many filings
- **Multiple Company Support** - Download from multiple companies at once
- **Filing Type Enum** - Comprehensive filing type support
- **Async Downloads** - Fast parallel downloads
- **Date Range Support** - Download historical data

### Basic Usage
```python
from secedgar import filings, FilingType

# Single company
my_filings = filings(
    cik_lookup="AAPL",  # Ticker or CIK
    filing_type=FilingType.FILING_10K,
    start_date="2020-01-01",
    end_date="2023-12-31",
    user_agent="Your Name (email@example.com)"
)
my_filings.save("/path/to/save")

# Multiple companies
my_filings = filings(
    cik_lookup=["AAPL", "MSFT", "GOOGL"],
    filing_type=FilingType.FILING_10Q,
    count=10,  # Last 10 filings
    user_agent="Your Name (email@example.com)"
)
my_filings.save("/path/to/save")

# Daily filings
from datetime import date
daily = filings(
    start_date=date(2024, 1, 1),
    end_date=date(2024, 1, 31),
    user_agent="Your Name (email@example.com)"
)
urls = daily.get_urls()
```

### Filing Types
```python
# Common filing types
FilingType.FILING_10K    # Annual report
FilingType.FILING_10Q    # Quarterly report
FilingType.FILING_8K     # Current report
FilingType.FILING_DEF14A # Proxy statement
FilingType.FILING_4      # Insider trading
FilingType.FILING_S1     # Registration statement
FilingType.FILING_13F    # Institutional holdings
```

### Advanced Usage
```python
# Jupyter Notebook support
import nest_asyncio
nest_asyncio.apply()

# Custom date ranges
my_filings = filings(
    cik_lookup="TSLA",
    filing_type=FilingType.FILING_8K,
    start_date="2023-01-01",
    end_date="2023-12-31",
    user_agent="Research Bot (research@university.edu)"
)

# Get filing URLs without downloading
urls = my_filings.get_urls()
```

### Strengths
- Mature and stable library
- Excellent for bulk operations
- Comprehensive filing type coverage
- Good for building datasets

### Limitations
- No parsing of financial data
- Returns raw HTML/XML only
- Requires manual text extraction
- No XBRL support

---

## 3. edgar-crawler - Academic Text Extraction
*Best for: NLP research, structured text extraction, academic studies*

### Installation
```bash
git clone https://github.com/lefterisloukas/edgar-crawler
cd edgar-crawler
pip install -r requirements.txt
```

### Key Features
- **Structured JSON Output** - Converts filings to clean JSON
- **Item-Level Extraction** - Extract specific sections (Item 1A, Item 7, etc.)
- **Academic Focus** - Designed for NLP research
- **Table Removal** - Option to remove tables for clean text
- **Batch Processing** - Process many filings efficiently

### Configuration
```json
{
  "download_filings": {
    "start_year": 2020,
    "end_year": 2023,
    "quarters": [1, 2, 3, 4],
    "filing_types": ["10-K", "10-Q", "8-K"],
    "cik_tickers": ["AAPL", "MSFT", "0000789019"],
    "user_agent": "Academic Research (email@university.edu)",
    "raw_filings_folder": "RAW_FILINGS",
    "skip_present_indices": true
  },
  "extract_items": {
    "raw_filings_folder": "RAW_FILINGS",
    "extracted_filings_folder": "EXTRACTED_FILINGS",
    "filing_types": ["10-K", "10-Q"],
    "items_to_extract": ["1", "1A", "3", "7", "8"],
    "remove_tables": true,
    "skip_extracted_filings": true
  }
}
```

### Usage
```bash
# Download filings
python download_filings.py

# Extract structured text
python extract_items.py
```

### Output Format (10-K)
```json
{
  "cik": "320193",
  "company": "Apple Inc.",
  "filing_type": "10-K",
  "filing_date": "2023-11-03",
  "period_of_report": "2023-09-30",
  "items": {
    "1": "Business description text...",
    "1A": "Risk factors text...",
    "3": "Legal proceedings text...",
    "7": "MD&A text...",
    "8": "Financial statements text..."
  }
}
```

### Strengths
- Best for text extraction research
- Clean JSON output
- Removes HTML artifacts
- Academic paper support
- Item-level granularity

### Limitations
- Complex setup
- No financial data parsing
- Limited to specific filing types
- Requires manual configuration
- GPL license (copyleft)

---

## Implementation Examples

### Example 1: Download Apple's Last 5 Years of 10-Ks
```python
# Using sec-edgar
from secedgar import filings, FilingType

apple_10ks = filings(
    cik_lookup="AAPL",
    filing_type=FilingType.FILING_10K,
    count=5,
    user_agent="Research (email@example.com)"
)
apple_10ks.save("./apple_10ks/")
```

### Example 2: Get Financial Statements
```python
# Using edgartools
from edgar import Company

apple = Company("AAPL")
financials = apple.get_financials()

# Income Statement
income = financials.income_statement()
print(f"Revenue: ${income.loc['Revenues']:,}")
print(f"Net Income: ${income.loc['NetIncomeLoss']:,}")

# Balance Sheet
balance = financials.balance_sheet()
print(f"Total Assets: ${balance.loc['Assets']:,}")
print(f"Total Liabilities: ${balance.loc['Liabilities']:,}")
```

### Example 3: Extract Risk Factors for NLP
```python
# Using edgar-crawler (after configuration)
import json

with open("EXTRACTED_FILINGS/AAPL/10-K/2023-11-03.json") as f:
    filing = json.load(f)
    risk_factors = filing["items"]["1A"]
    
# Now use with NLP models
from transformers import pipeline
sentiment = pipeline("sentiment-analysis")
result = sentiment(risk_factors[:512])  # Chunk for model limits
```

### Example 4: Monitor Insider Trading
```python
# Using edgartools
from edgar import Company
from datetime import datetime, timedelta

company = Company("TSLA")
filings = company.get_filings(
    form="4",
    date=(datetime.now() - timedelta(days=30), datetime.now())
)

for filing in filings:
    form4 = filing.obj()
    for transaction in form4.transactions:
        if transaction.transaction_type == "P":  # Purchase
            print(f"{transaction.reporting_owner}: Bought {transaction.shares} shares")
```

---

## Best Practices

### 1. Rate Limiting
```python
# Always identify yourself
user_agent = "John Doe, Research at University (john@university.edu)"

# Add delays for sec-edgar
import time
time.sleep(0.1)  # 10 requests per second max

# edgartools handles this automatically
```

### 2. Error Handling
```python
try:
    filings = company.get_filings()
except Exception as e:
    print(f"Error fetching filings: {e}")
    # Implement retry logic
```

### 3. Data Storage
```python
# Save raw filings for reproducibility
import os
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

# Cache parsed data
import pickle
with open("data/processed/apple_financials.pkl", "wb") as f:
    pickle.dump(financials, f)
```

### 4. Compliance
- Always provide accurate user agent
- Respect rate limits (10 requests/second)
- Don't redistribute raw EDGAR data
- Cite SEC as data source

---

## Use Case Selection Guide

### Choose edgartools if you need:
- Quick financial analysis
- Clean, modern API
- Parsed financial statements
- XBRL data extraction
- Active development/support

### Choose sec-edgar if you need:
- Bulk download many filings
- Build large datasets
- Archive historical filings
- Simple, stable solution

### Choose edgar-crawler if you need:
- Academic NLP research
- Structured text extraction
- Item-level granularity
- Remove tables/formatting
- Reproducible research

---

## Additional Resources

### Official Documentation
- [edgartools Docs](https://edgartools.readthedocs.io/)
- [sec-edgar Docs](https://sec-edgar.github.io/sec-edgar/)
- [edgar-crawler Paper](https://dl.acm.org/doi/10.1145/3701716.3715289)

### SEC EDGAR Resources
- [EDGAR Search](https://www.sec.gov/edgar/searchedgar/companysearch.html)
- [SEC Developer Resources](https://www.sec.gov/developer)
- [EDGAR File Structure](https://www.sec.gov/edgar/filer-information/current-edgar-technical-specifications)
- [CIK Lookup](https://www.sec.gov/edgar/searchedgar/cik.htm)

### Tutorials & Examples
- [edgartools Examples](https://github.com/dgunning/edgartools/tree/main/notebooks)
- [Financial Analysis with EDGAR](https://www.edgartools.io/)
- [SEC Filing Types Guide](https://www.sec.gov/forms)

---

## Cost Analysis

All three libraries are **completely free** to use:
- No API keys required
- No subscription fees
- Direct access to SEC's public data
- Only requirement: Identify yourself in user agent

Compare to commercial alternatives:
- Bloomberg Terminal: $24,000+/year
- Refinitiv: $20,000+/year  
- S&P Capital IQ: $25,000+/year

---

## Summary

The SEC EDGAR database provides powerful free access to U.S. public company filings. These three Python libraries offer different approaches:

1. **edgartools** - Best overall for financial analysis and modern Python development
2. **sec-edgar** - Best for bulk downloads and building datasets
3. **edgar-crawler** - Best for academic text extraction and NLP research

All are free, open-source, and actively maintained. Choose based on your specific use case and technical requirements.

---
*Last Updated: August 25, 2025*
*Data Source: SEC EDGAR Database (public domain)*