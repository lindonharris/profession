# Reading 10: Introduction to Valuation

## Overview
This reading examines how financial information is used to estimate economic value through valuation. It covers fundamental economic principles underlying stock valuation and demonstrates two common approaches: (1) multiples (price-to-earnings and price-to-book) and (2) discounted future earnings using abnormal earnings models. Examples use Burberry, Inditex, and The Gap.

## Fundamental Valuation Principles

### Principle 1: Investors Purchase Securities for Future Cash Flows
- Stocks valued for future cash flows (dividends + sale proceeds)
- Debt securities valued for interest + principal payments
- Equity cash flows more uncertain than debt (not contractually specified)

### Principle 2: Investors Require Higher Expected Returns for Riskier Investments
- Risk hierarchy: Government bonds < Corporate bonds < Stocks
- Historical returns validate this (1926-2010):
  - US Treasuries: 3.6%
  - Corporate bonds: 5.5%
  - Large cap stocks: 9.9%
  - Small cap stocks: 12.1%

## Challenges in Valuing Stocks
- Historical data limitations (many firms pay no dividends)
- Risk measures imperfect for future predictions
- Two approaches address these challenges:
  1. **Multiples**: Use comparable firms' metrics
  2. **Discounted earnings**: Forecast future earnings and discount

## Valuation Using Multiples

### Price-to-Earnings Multiple Formula
```
P/E = Share Price / Earnings per Share
```

**Key Insights**:
- Reflects investor expectations of future earnings
- Higher P/E suggests higher growth expectations or lower risk
- Current earnings proxy for future earnings

**Example P/E Multiples (2014)**:
- Burberry: 20.0
- Inditex: 29.4
- The Gap: 14.3

**Factors Explaining P/E Differences**:
1. **Growth expectations**: Higher expected growth → Higher P/E
2. **Risk perceptions**: Lower risk → Higher P/E
3. **Earnings volatility**: More stable earnings → Higher P/E
4. **Financial leverage**: Conservative leverage → Lower earnings volatility

**P/E Limitations**:
- Highly sensitive to temporary earnings shocks
- Undefined for firms with losses (30% of listed firms)
- Solution: Use earnings from continuing operations

### Price-to-Book Multiple Formula
```
P/B = Share Price / Book Value per Share
```

**Key Insights**:
- Book equity = Capital invested in firm
- Higher P/B suggests superior return generation ability
- Less affected by temporary earnings issues

**Example P/B Multiples (2014)**:
- Burberry: 5.55
- Inditex: 7.54
- The Gap: 5.97

### Using Multiples for Valuation

**Three-Step Process**:
1. **Identify comparables**: Select benchmark firms
2. **Calculate weighted average multiple**: Weight by market cap
3. **Apply to target**: Multiply by target's metric

**Example: Valuing Burberry using Inditex & Gap**:
- Weighted P/E: 26.9
- Burberry EPS: £0.74
- Estimated value: £19.91 (vs actual £14.77)

**Limitations of Multiples Approach**:
- Requires truly comparable firms
- Industry membership ≠ comparability
- Undefined for negative denominators
- Sensitive to accounting choices

## Discounted Future Earnings Valuation

### Discounted Dividends Formula
```
Equity Value = PV(Future Dividends)
            = Div₁/(1+r) + Div₂/(1+r)² + ...
```

**Limitations**:
- Many firms pay no dividends (56% in 2013)
- Difficult to forecast future dividends

### Reframing Using Abnormal Earnings

**Dividend Identity**:
```
Dividends = Earnings + (Beginning BV - Ending BV)
```

**Abnormal Earnings Equity Value Formula**:
```
Equity Value = Book Value + PV(Abnormal Earnings)
```

**Abnormal Earnings Formula**:
```
Abnormal Earnings = Net Income - (Required Return × Beginning Book Value)
```

### Abnormal Earnings Interpretation
- Represents ability to earn returns > required return
- Sources: Superior technology, patents, economies of scale, management
- Competition causes mean reversion over 5-7 years

### Terminal Values
**Terminal Value Formula**:
```
Terminal Value = Abnormal Earnings / (r - g)
```

**Where**:
- r = Required return
- g = Growth rate (must be < r)

### Burberry Valuation Example (2014)

**Assumptions**:
- Required return: 9.5%
- Book value per share: £2.66
- Forecasted EPS: £0.77-£1.27 (2015-2020)
- Terminal growth: 5%

**Calculation**:
1. PV of abnormal earnings 2015-2020: £2.81
2. Terminal value (2021+): £10.43
3. Beginning book value: £2.66
4. **Total equity value**: £15.89 (vs actual £14.77)

## The P/B Multiple Revisited

### P/B Multiple from Abnormal Earnings Formula
```
P/B = 1 + [E(ROE) - r] / (r - g)
```

**Key Relationships**:
- If E(ROE) = r → P/B = 1
- If E(ROE) > r → P/B > 1
- If E(ROE) < r → P/B < 1

### Impact of Growth on Value

**When ROE > Required Return**:
- Growth creates value
- Higher growth → Higher P/B

**When ROE = Required Return**:
- Growth irrelevant to value
- P/B = 1 regardless of growth

**When ROE < Required Return**:
- Growth destroys value
- Higher growth → Lower P/B

### Empirical Evidence
Strong positive relationship between ROE and P/B across:
- Selected retailers
- S&P 500 companies
- Dow Jones Industrial Average

### Explaining Observed P/B Multiples

**Implied Assumptions for 2014 Multiples**:

| Company | ROE | Growth | Cost of Equity | Implied P/B | Actual P/B |
|---------|-----|--------|----------------|-------------|------------|
| Inditex | 28.0% | 3.7% | 6.9% | 7.6 | 7.54 |
| Burberry | 32.0% | 4.6% | 9.5% | 5.6 | 5.55 |
| The Gap | 44.0% | 3.7% | 10.5% | 5.9 | 5.97 |

**Explanations for High ROEs**:
1. **Conservative accounting**: Marketing expensed (understates book value)
2. **Brand value**: Not on balance sheet
3. **Market optimism**: May overestimate sustainability

## Valuation Method Comparison

### Multiples Approach

**Advantages**:
- Simple to implement
- Market-based benchmarks
- Works with current data

**Disadvantages**:
- Requires comparable firms
- Sensitive to temporary shocks
- Undefined for negative values

### Discounted Abnormal Earnings

**Advantages**:
- Firm-specific valuation
- No comparables needed
- Works with losses
- Incorporates growth and risk

**Disadvantages**:
- Requires earnings forecasts
- Terminal value assumptions critical
- Complex calculations

## Key Analytical Insights

### P/E Multiple Analysis
- Compare to industry peers
- Adjust for one-time items
- Consider growth and risk differences
- Watch for earnings manipulation

### P/B Multiple Analysis
- Evaluate ROE sustainability
- Consider off-balance sheet assets
- Assess competitive advantages
- Monitor growth expectations

### Growth Value Creation
- Growth only valuable if ROE > cost of equity
- Sustainable competitive advantages rare
- Mean reversion typically occurs
- Terminal values often optimistic

## Practical Application Guidelines

### When to Use Multiples
- Quick valuations needed
- Many comparable firms available
- Stable industry conditions
- Market-based perspective desired

### When to Use Discounted Earnings
- Few/no comparables exist
- Detailed forecasts available
- Firm-specific analysis needed
- Major strategic changes expected

### Red Flags in Valuation
- P/B multiples requiring perpetual high ROEs
- Growth rates exceeding cost of equity
- Terminal values dominating total value
- Wide variation in "comparable" multiples

## Key Takeaways

1. **Valuation fundamentals**: Based on future cash flows and risk
2. **Two main approaches**: Multiples (simple) vs discounted earnings (detailed)
3. **P/E sensitive to earnings volatility**: Use normalized earnings
4. **P/B related to ROE**: Higher sustainable ROE → Higher P/B
5. **Growth paradox**: Only creates value if ROE > required return
6. **Terminal values critical**: Often 60-80% of total value
7. **Mean reversion reality**: Abnormal returns rarely sustainable
8. **Accounting matters**: Conservative accounting inflates ROE/multiples
9. **Comparability challenge**: Same industry ≠ comparable
10. **Market optimism**: Often assumes perpetual outperformance

## Summary
Valuation bridges financial reporting and investment decisions. While multiples offer simplicity, they require truly comparable firms. Discounted abnormal earnings models provide firm-specific valuations but require detailed forecasts and terminal value assumptions. Both approaches have merits, and analysts often use multiple methods to triangulate value. Understanding the relationship between P/B multiples, ROE, and growth is crucial for assessing whether market valuations reflect realistic expectations about future performance.