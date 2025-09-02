# WRDS (Wharton Research Data Services) API Documentation

## Overview
WRDS is the leading academic financial database platform, providing programmatic access to 600+ datasets from 60+ data vendors through institutional subscriptions. Unlike commercial providers (PitchBook/Preqin), WRDS is specifically designed for academic research with deep historical data archives.

## Access at HBS

### Eligibility
- **✅ HBS Faculty, Students, Staff** - Full remote access
- **❌ Executive Education & Fellows** - No access
- **❌ Alumni** - No access
- **Note**: No accounts during summer/semester breaks

### Authentication Requirements
- Individual WRDS account (not class accounts for API)
- Two-Factor Authentication (2FA) via Duo Security
- SSH access for programmatic connections
- Academic use only (no commercial purposes)

## API Access Methods

### 1. Python API (Recommended)
```python
# Installation
pip install wrds

# Basic connection
import wrds
conn = wrds.Connection()  # Prompts for username/password

# With .pgpass file (automated access)
conn = wrds.Connection(wrds_username='your_username')
```

### 2. R Package
```r
# Installation
install.packages("RPostgres")
library(RPostgres)

# Connection
wrds <- dbConnect(Postgres(),
                  host='wrds-pgdata.wharton.upenn.edu',
                  port=9737,
                  dbname='wrds',
                  user='your_username')
```

### 3. Direct SQL via SAS/STATA
- SSH to WRDS Cloud
- Native SAS/STATA commands
- Requires active licenses

## Authentication Setup

### Creating .pgpass File (Recommended)
```bash
# Create file in home directory
echo "wrds-pgdata.wharton.upenn.edu:9737:wrds:username:password" >> ~/.pgpass

# Set permissions (critical)
chmod 600 ~/.pgpass
```

### Connection Parameters
- **Host**: wrds-pgdata.wharton.upenn.edu
- **Port**: 9737
- **Database**: wrds
- **SSL**: Required

## Available Datasets

### Core Financial Databases

#### CRSP (Center for Research in Security Prices)
- **Stock Data**: Daily/monthly prices, returns, volumes (1925+)
- **Indices**: Market indices and benchmarks
- **Treasuries**: Risk-free rates (1961+ daily, 1925+ monthly)
- **Mutual Funds**: Fund returns and holdings

#### Compustat
- **Fundamentals**: Financial statements (80,000+ companies)
- **Global**: International company data
- **Bank**: Banking-specific fundamentals
- **Segments**: Business segment data

#### Market Microstructure
- **TAQ (Trade and Quote)**: Intraday tick data
- **ISSM**: Historical intraday (pre-1993)
- **TRACE**: Bond transaction data
- **OptionMetrics**: Options prices and Greeks

### Analyst & Estimates
- **IBES**: Analyst forecasts and recommendations
- **First Call**: Historical estimates
- **Thomson Reuters**: Ownership and insiders

### Alternative Data
- **Dealscan**: Loan and debt agreements
- **BoardEx**: Board composition and networks
- **RavenPack**: News sentiment scores
- **Audit Analytics**: Accounting quality metrics

### Economic & Reference
- **FRED**: Federal Reserve economic data
- **Fama-French**: Factor portfolios
- **Penn World Tables**: International comparisons
- **Linking Tables**: CUSIP/PERMNO/GVKEY mappings

## Python API Methods

### Connection Management
```python
import wrds
conn = wrds.Connection()

# List available libraries/databases
libraries = conn.list_libraries()

# List tables in a library
tables = conn.list_tables(library='crsp')

# Describe table structure
schema = conn.describe_table(library='crsp', table='dsf')

# Close connection
conn.close()
```

### Data Retrieval

#### Method 1: get_table()
```python
# Simple table extraction
data = conn.get_table(
    library='comp',
    table='funda',
    columns=['gvkey', 'datadate', 'at', 'lt'],
    obs=10000  # Limit rows
)
```

#### Method 2: raw_sql()
```python
# Complex queries with SQL
query = """
    SELECT a.gvkey, a.datadate, a.at, a.lt, b.prccm
    FROM comp.funda a
    LEFT JOIN comp.secm b
    ON a.gvkey = b.gvkey 
    AND a.datadate = b.datadate
    WHERE a.fyear BETWEEN 2015 AND 2020
    AND a.indfmt = 'INDL'
    AND a.datafmt = 'STD'
    AND a.popsrc = 'D'
    AND a.consol = 'C'
"""
data = conn.raw_sql(query, date_cols=['datadate'])
```

### Advanced Features

#### Chunked Downloads (Large Datasets)
```python
# For datasets >1GB
for chunk in conn.raw_sql(query, chunksize=10000):
    process_chunk(chunk)  # Process in batches
```

#### Date Handling
```python
# Automatic date parsing
data = conn.raw_sql(query, date_cols=['datadate', 'rdq'])
```

## Common Use Cases

### 1. Stock Returns Analysis
```python
# Get Apple's stock returns
apple = conn.raw_sql("""
    SELECT date, ret, vol, shrout
    FROM crsp.dsf
    WHERE permno = 14593  -- Apple's PERMNO
    AND date >= '2020-01-01'
    ORDER BY date
""", date_cols=['date'])
```

### 2. Fundamental Data
```python
# Annual fundamentals for S&P 500
sp500_fundamentals = conn.raw_sql("""
    SELECT a.*
    FROM comp.funda a
    JOIN comp.idxcst_his b
    ON a.gvkey = b.gvkey
    WHERE b.gvkeyx = '000003'  -- S&P 500 index
    AND a.datadate BETWEEN b.from AND b.thru
    AND a.fyear = 2023
""", date_cols=['datadate'])
```

### 3. Merging CRSP and Compustat
```python
# Using CCM linking table
merged = conn.raw_sql("""
    SELECT a.permno, a.date, a.ret,
           b.gvkey, b.at, b.ni
    FROM crsp.dsf a
    JOIN crsp.ccmxpf_lnkhist c
    ON a.permno = c.lpermno
    AND a.date BETWEEN c.linkdt AND c.linkenddt
    JOIN comp.funda b
    ON c.gvkey = b.gvkey
    AND b.datadate = DATE_TRUNC('year', a.date)
    WHERE a.date >= '2020-01-01'
    AND c.linktype IN ('LC', 'LU')
""")
```

## Performance Optimization

### Best Practices
1. **Filter early**: Use WHERE clauses to reduce data transfer
2. **Select columns**: Only request needed columns
3. **Use indices**: PERMNO for CRSP, GVKEY for Compustat
4. **Date ranges**: Always specify date boundaries
5. **Chunking**: Use for datasets >1GB

### Query Optimization
```python
# Bad: Downloads entire table then filters
data = conn.get_table(library='crsp', table='dsf')
data = data[data['date'] >= '2020-01-01']

# Good: Filters on server
data = conn.raw_sql("""
    SELECT * FROM crsp.dsf 
    WHERE date >= '2020-01-01'
""")
```

## Rate Limits & Quotas

### Connection Limits
- Max 5 concurrent connections per user
- 10-hour query timeout
- 50GB memory limit per query

### Best Practices
- Close connections when done
- Use connection pooling for applications
- Implement retry logic for failed queries

## R Implementation

### Basic Setup
```r
library(RPostgres)
library(dplyr)

# Connect
wrds <- dbConnect(Postgres(),
                  host='wrds-pgdata.wharton.upenn.edu',
                  port=9737,
                  dbname='wrds',
                  sslmode='require',
                  user='username')

# Query
data <- dbGetQuery(wrds, "
    SELECT * FROM crsp.dsf 
    WHERE date >= '2020-01-01' 
    LIMIT 1000
")

# Using dplyr
crsp_dsf <- tbl(wrds, in_schema("crsp", "dsf"))
result <- crsp_dsf %>%
    filter(date >= '2020-01-01') %>%
    select(permno, date, ret) %>%
    collect()

# Disconnect
dbDisconnect(wrds)
```

## WRDS Cloud Features

### JupyterLab Access
- Web-based Python/R notebooks
- Pre-installed libraries
- Direct data access
- Share notebooks with collaborators

### SSH Access
```bash
ssh username@wrds-cloud.wharton.upenn.edu

# Run Python scripts
python3 my_analysis.py

# Submit batch jobs
qsub -N myjob analysis_script.sh
```

## Comparison with Commercial APIs

| Feature | WRDS | PitchBook | Preqin |
|---------|------|-----------|---------|
| **Cost** | Via institution | $25k+/year | $25k+/year |
| **Focus** | Academic research | PE/VC deals | Alternative assets |
| **Historical Data** | Excellent (1925+) | Good | Good |
| **Data Quality** | Research-grade | Commercial-grade | Commercial-grade |
| **API Access** | Python, R, SQL | REST only | REST + Feeds |
| **Support** | Academic/technical | Sales-focused | Sales-focused |
| **Best For** | Empirical research | Deal sourcing | Fund analysis |

## Limitations & Restrictions

### Usage Restrictions
- Academic research only
- No commercial use
- No redistribution
- Cannot share credentials
- Must cite in publications

### Technical Limitations
- No real-time data
- Some datasets have embargo periods
- Complex queries may timeout
- Limited to subscribed datasets

## Support Resources

### Documentation
- [WRDS Research Applications](https://wrds-www.wharton.upenn.edu/pages/support/research-applications/)
- [Python API Docs](https://wrds-www.wharton.upenn.edu/pages/support/programming-python/)
- [Sample Programs](https://wrds-www.wharton.upenn.edu/pages/support/sample-programs/)

### HBS Support
- Baker Library: infoservices@hbs.edu
- Phone: 1.617.495.6040
- Research Computing Services

### WRDS Support
- Email: wrds@wharton.upenn.edu
- Support portal (requires login)
- Video tutorials and webinars

## Implementation Checklist

### Initial Setup
- [x] Obtain WRDS account through HBS ✅ 2025-09-01
- [x] Set up 2FA with Duo ✅ 2025-09-01
- [ ] Install wrds Python package
- [ ] Create .pgpass file
- [ ] Test connection
- [ ] Explore available datasets

### Development
- [ ] Identify required datasets
- [ ] Design efficient queries
- [ ] Implement error handling
- [ ] Add data validation
- [ ] Document data sources
- [ ] Create reproducible workflow

## Code Repository Structure
```
project/
├── config/
│   └── .pgpass          # Credentials (git-ignored)
├── src/
│   ├── wrds_conn.py    # Connection utilities
│   ├── data_pull.py    # Data extraction
│   └── analysis.py     # Analysis code
├── data/
│   ├── raw/            # Original WRDS data
│   └── processed/      # Cleaned data
├── notebooks/          # Jupyter notebooks
└── requirements.txt    # Python dependencies
```

---
*Last Updated: August 25, 2025*
*Access: Via HBS institutional subscription*
*Usage: Academic research only*