# FIN1 Study Guide
*Finance 1 - Living Document for Financial Analysis, Valuation, and Capital Markets*

> **Last Updated**: September 2025
> **Course**: Finance 1 (FIN1-C), Fall 2025
> **Professor**: Sam Hanson (Section C)
> **Teaching Fellows**: Joy Haddad & Josh Kuppersmith
> **Important Resources**:
> - [[resources/FIN1 Introductory Note.pdf|Course Overview Note]]
> - [[resources/FIN1 Course Requirements Memo.pdf|Course Requirements Memo]]
> - [[resources/FIN1 Tips for Preparation.pdf|Tips for Preparation]]

---

## 📚 Course Overview

### Course Objectives
Finance 1 focuses on understanding the determinants of economic value and how managers and firms can add value through **investment decisions**, regardless of funding choices. The course adopts a decision-oriented approach through case method learning.

**Key Questions Addressed:**
- What investments maximize long-run value for owners?
- Is a firm's growth strategy creating value? How much?
- What rate of return are investments expected to earn?
- Is that return sufficient given the risks?
- What is a company worth to owners and potential acquirers?

### Course Structure
**Finance 1** is divided into three progressive modules:

#### Module 1: Forecasting and Valuing Free Cash Flows
- Analyze financial statements to understand business models
- Distinguish between accounting earnings and cash flows
- Learn DCF and multiples analysis
- Master NPV for capital investment evaluation

#### Module 2: Capital Markets, Portfolio Choice, and Discount Rates
- Understand investor requirements and required returns
- Learn relationship between risk and return
- Master portfolio theory and diversification
- Calculate appropriate discount rates

#### Module 3: Integrated Value-Based Decisions
- Apply concepts from multiple perspectives:
  - Corporate investor
  - Growth equity investor
  - Impact investor
  - Active investor
  - Public markets investor
- Comprehensive cases with complex financial decisions

### How to Use This Guide
- Master core concepts through frameworks
- Practice calculations with templates
- Review case applications by module
- Prepare for exams with checklists

## 📋 Course Requirements & Grading

### Grade Breakdown
- **Class Participation**: 50%
  - Including preparation: Completion of tutorials, polls, spreadsheet uploads, and online exercises
- **Test 1**: 10% (Tuesday, October 21st)
- **Test 2**: 10% (Tuesday, November 18th)
- **Final Exam**: 30% (Monday, December 15th)

### Important Dates
- **Online Exercises** (90 minutes each):
  - Exercise 1: September 29 - October 6
  - Exercise 2: October 14 - 17
  - Exercise 3: October 29 - November 3
  - Exercise 4: November 12 - 17
  - *Available 3pm opening day through 11:59pm closing day*

### Class Participation Excellence
**High-quality participation involves:**
- Explaining logic clearly, not just providing numbers
- Making comments accessible to everyone
- Building on section mates' contributions
- Integrating ideas and providing empirical support
- Drawing managerial inferences from analyses
- For finance newcomers: Asking thoughtful questions

### Preparation Requirements
- **Excel uploads**: Due by 8:00 AM on class day
- **Individual work**: Notify professor if using collaborative help
- **Midpoint feedback**: Interim participation assessment provided

## 📖 Pre-Class Preparation Approach

### Typical Case Preparation (75-150 minutes)
1. **Read Canvas assignment in full** (start here always)
2. **Read the case** with study questions in mind (10-25m)
3. **Read "[Case] Day X Tools"** for relevant concepts (5m)
4. **Complete textbook readings** - focused pages highlighted (10-30m)
5. **Complete video tutorials** on Canvas (20-40m)
6. **Work Excel exhibits** - fill templated sections (20-40m)
7. **Connect analysis to study questions** (10-30m)

### Canvas Navigation for Each Case
- **Case Materials**: PDF and exhibits
- **Tools PowerPoint**: Finance concepts for the case
- **Tutorial Videos**: Interactive learning modules
- **Excel Templates**: Pre-formatted analysis files
- **Textbook Readings**: Specific pages identified
- **Poll/Upload Requirements**: Due 8am class day

### GenAI Usage Guidelines

#### Recommended Approach: "Use Your Brain First"
1. Complete preparation independently first
2. Use GenAI to clarify concepts, terms, and tools
3. Ask GenAI to quiz you, not answer for you
4. Upload completed work for cell-by-cell help
5. Use Socratic questioning for discussion prep

#### What GenAI Can Help With:
- Explaining financial concepts (margins, DuPont, DCF)
- Clarifying tutorial questions you missed
- Checking specific Excel formula logic
- Practicing case discussion questions

#### What GenAI Should NOT Do:
- Complete your models from scratch
- Answer assignment questions directly
- Perform your calculations
- Make judgments about case recommendations

**Note**: Tests and final exam will not allow GenAI access

### Course Progression
- **Modules 1-2**: More guidance (tools, tutorials, templates)
- **Module 3+**: Less scaffolding as skills develop
- **Finance 2**: Minimal guidance - focus on decision-making

---

## 💰 Core Finance Frameworks

### 1. Time Value of Money (TVM)

#### Basic Formulas
```
Future Value: FV = PV × (1 + r)^n
Present Value: PV = FV / (1 + r)^n
```

#### Annuity Formulas
```
PV of Annuity = PMT × [(1 - (1+r)^-n) / r]
FV of Annuity = PMT × [((1+r)^n - 1) / r]

Growing Annuity PV = PMT × [(1 - ((1+g)/(1+r))^n) / (r-g)]
Perpetuity PV = PMT / r
Growing Perpetuity PV = PMT / (r - g)
```

#### NPV and IRR
```
NPV = Σ(CFt / (1+r)^t) - Initial Investment
IRR: Rate where NPV = 0
```

**Decision Rules:**
- NPV > 0 → Accept project
- IRR > Cost of Capital → Accept project
- When conflicts: Use NPV (theoretically superior)

### 2. Financial Statement Analysis

#### Key Financial Ratios

##### Liquidity Ratios
| Ratio | Formula | Interpretation |
|-------|---------|----------------|
| Current Ratio | Current Assets / Current Liabilities | > 1.5 healthy |
| Quick Ratio | (CA - Inventory) / CL | > 1.0 good |
| Cash Ratio | Cash / Current Liabilities | > 0.2 adequate |

##### Leverage Ratios
| Ratio | Formula | Interpretation |
|-------|---------|----------------|
| Debt-to-Equity | Total Debt / Total Equity | < 1.0 conservative |
| Debt-to-Assets | Total Debt / Total Assets | < 0.5 safe |
| Interest Coverage | EBIT / Interest Expense | > 3.0 comfortable |
| Debt Service Coverage | EBITDA / (Interest + Principal) | > 1.25 adequate |

##### Profitability Ratios
| Ratio | Formula | Interpretation |
|-------|---------|----------------|
| ROE | Net Income / Equity | 15-20% good |
| ROA | Net Income / Assets | 5-10% good |
| ROIC | NOPAT / Invested Capital | > WACC value creation |
| Gross Margin | Gross Profit / Sales | Industry-specific |
| Operating Margin | EBIT / Sales | Higher is better |

#### Cash Flow Analysis
```
Operating Cash Flow (Indirect):
Net Income
+ Depreciation & Amortization
+/- Changes in Working Capital
= Cash from Operations

Free Cash Flow:
EBIT × (1 - Tax Rate)
+ Depreciation & Amortization
- CapEx
- Δ Net Working Capital
= Free Cash Flow
```

### 3. Cost of Capital

#### WACC (Weighted Average Cost of Capital)
```
WACC = (E/V) × Re + (D/V) × Rd × (1 - Tc)

Where:
E = Market value of equity
D = Market value of debt
V = E + D = Total firm value
Re = Cost of equity
Rd = Cost of debt
Tc = Corporate tax rate
```

#### Cost of Equity Methods

##### CAPM (Capital Asset Pricing Model)
```
Re = Rf + β × (Rm - Rf)

Where:
Rf = Risk-free rate
β = Beta (systematic risk)
Rm = Market return
(Rm - Rf) = Market risk premium
```

##### Build-Up Method
```
Re = Rf + Equity Risk Premium + Size Premium + Company-Specific Premium
```

##### Gordon Growth Model
```
Re = (D1/P0) + g

Where:
D1 = Next year's dividend
P0 = Current stock price
g = Growth rate
```

#### Beta Calculation and Adjustment
```
Levered Beta = Unlevered Beta × [1 + (1-T) × (D/E)]

Industry Beta Approach:
1. Find comparable companies
2. Unlever their betas
3. Average unlevered betas
4. Relever for target capital structure
```

### 4. Valuation Methods

#### DCF Valuation

##### Enterprise Value Approach
```
Enterprise Value = Σ(FCFt / (1+WACC)^t) + Terminal Value / (1+WACC)^n
Equity Value = Enterprise Value - Net Debt
```

##### Equity Value Approach
```
Equity Value = Σ(FCFEt / (1+Re)^t) + Terminal Value / (1+Re)^n

Where FCFE = FCF - Interest × (1-T) + Net Borrowing
```

##### Terminal Value Calculations
```
Gordon Growth: TV = FCFn+1 / (WACC - g)
Exit Multiple: TV = EBITDAn × Exit Multiple
```

#### Relative Valuation Multiples

| Multiple | Formula | Use Case |
|----------|---------|----------|
| P/E | Price / EPS | Mature companies |
| EV/EBITDA | Enterprise Value / EBITDA | Cross-border comparisons |
| P/B | Price / Book Value | Financial institutions |
| EV/Sales | Enterprise Value / Sales | High-growth companies |
| PEG | P/E / Growth Rate | Growth companies |

#### Real Options Valuation
- **Expansion Option**: Value of growth opportunities
- **Abandonment Option**: Value of exit flexibility
- **Timing Option**: Value of waiting
- **Switching Option**: Value of operational flexibility

---

## 📊 Financial Modeling Toolkit

### 1. Working Capital Management

#### Cash Conversion Cycle
```
CCC = Days Inventory Outstanding + Days Sales Outstanding - Days Payables Outstanding

DIO = (Inventory / COGS) × 365
DSO = (Accounts Receivable / Sales) × 365
DPO = (Accounts Payable / COGS) × 365
```

#### Working Capital Needs
```
NWC = Current Assets - Current Liabilities
ΔNWC = NWCt - NWCt-1

Operating Working Capital = (CA - Cash) - (CL - Short-term Debt)
```

### 2. Capital Budgeting

#### Project Evaluation Framework
```
1. Calculate incremental cash flows
2. Include opportunity costs
3. Ignore sunk costs
4. Consider tax effects
5. Account for working capital changes
6. Calculate terminal value
```

#### Sensitivity Analysis Template
| Variable | Base Case | -20% | -10% | +10% | +20% |
|----------|-----------|------|------|------|------|
| Sales Volume | NPV | | | | |
| Price | NPV | | | | |
| Variable Costs | NPV | | | | |
| Discount Rate | NPV | | | | |

#### Break-Even Analysis
```
Accounting Break-Even = Fixed Costs / (Price - Variable Cost)
Cash Break-Even = (Fixed Costs - Depreciation) / (Price - Variable Cost)
Financial Break-Even = (Fixed Costs + Interest) / (Price - Variable Cost)
NPV Break-Even: Quantity where NPV = 0
```

### 3. Capital Structure Decisions

#### MM Propositions
**Without Taxes:**
- Prop I: VL = VU (capital structure irrelevant)
- Prop II: Re = Ra + (Ra - Rd) × (D/E)

**With Taxes:**
- Prop I: VL = VU + T × D (tax shield value)
- Prop II: Re = Ru + (Ru - Rd) × (1-T) × (D/E)

#### Trade-Off Theory
```
Optimal Capital Structure balances:
+ Tax benefits of debt
- Financial distress costs
- Agency costs of debt
```

#### Pecking Order Theory
1. Internal financing (retained earnings)
2. Debt financing
3. Equity financing (last resort)

---

## 💼 Complete Case Lineup & Key Concepts

### Module 1: Forecasting and Valuing Free Cash Flows

| Case | Key Concepts | Tools/Analysis |
|------|--------------|----------------|
| **Butler Lumber Day 1** | • Growing sales requires growing assets<br>• Growth in assets must be funded | • Ratio analysis<br>• Sources and uses of funds<br>• Cash conversion cycle |
| **Butler Lumber Day 2** | • Income ≠ Cash flow | • Percent of sales forecasting |
| **Mighty Squirrel** | • Developing a financial plan | • Financial modeling |
| **Project Helios** | • Time value of money<br>• Discounting and best alternative | • Discounting mechanics<br>• Net present value |
| **Patrimonio Hoy** | • Household borrowing ≠ lending rate | • Internal rate of return |
| **Ocean Carriers** | • Compute relevant, incremental cash flow | • Free cash flow formula |
| **Progyny** | • Value of going concern in steady state | • Perpetuity value |
| **Hamilton** | • Option value<br>• Value of experimentation | • Decision trees<br>• Scenarios and real options |
| **Selling for a Song** | • How growth and discount rates drive DCF | • Perpetuity value and multiples |
| **Tottenham** | • Using multiples to estimate value | • Multiples analysis |

### Module 2: Capital Markets, Risk and Return

| Case | Key Concepts | Tools/Analysis |
|------|--------------|----------------|
| **Cook County Day 1** | • Stock returns are approximately normal<br>• Mean-variance optimization | • Mean return<br>• Standard deviation/volatility |
| **Partners Day 1** | • Maximum Sharpe ratio portfolios<br>• 1-2 investment optimization | • Portfolio return/volatility<br>• Sharpe ratio |
| **Partners Day 2** | • Many investment optimization<br>• Two fund separation | • Portfolio optimization |
| **Optimalen Day 1** | • Market efficiency<br>• Risk for marginal investment | • Portfolio Improvement Rule<br>• Alpha |
| **Optimalen Day 2** | • Idiosyncratic vs systematic risk<br>• Benefits of diversification | • Regression<br>• Beta |
| **DraftKings Day 1** | • Inputs to cost of capital<br>• Apply PIR to broad market | • Asset/unlevered beta |
| **DraftKings Day 2** | • Value loss from incorrect hurdle rates<br>• Cost of capital for unlevered firm | • WACC calculation |

### Module 3: Integrated Value-Based Decisions

| Case | Key Concepts | Perspective |
|------|--------------|-------------|
| **MGH and the Enbrel Royalty** | • Value to diversified vs undiversified investors<br>• Markets drive innovation | Corporate investor |
| **All-American Pipeline** | • Use project not firm-wide cost of capital<br>• Firms need not diversify | Corporate investor |
| **Dicerna** | • Probability-weighted valuation<br>• Term sheet incentives | Growth equity investor |
| **Impact Developers Fund** | • Share repurchases to concentrate ownership | Impact investor |
| **Kerr McGee Day 1** | • Activism types<br>• Growth can destroy value | Activist investor |
| **Kerr McGee Day 2** | • Going concern vs liquidation value | Equity analyst |
| **Peloton** | • Comprehensive review | Multiple perspectives |

## 💼 Case Applications by Module (Additional Detail)

### Module 1: Financial Statement Analysis

#### 🏗️ Butler Lumber - Working Capital Crisis
**Focus**: Cash flow management and growth financing
- **Key Issues**:
  - Rapid growth straining cash
  - Trade credit dependencies
  - Bank loan limitations
- **Analysis Framework**:
  ```
  Sustainable Growth Rate = ROE × (1 - Payout Ratio)
  External Financing Needed = (A/S)ΔS - (L/S)ΔS - PM×S×(1-d)
  ```
- **Key Learning**: Growth requires cash; profitable ≠ cash rich

#### 🍺 Mighty Squirrel Brewing - Financial Analysis
**Focus**: Startup financial assessment
- **Analysis Points**:
  - Unit economics
  - Break-even analysis
  - Funding requirements
  - Valuation challenges

### Module 2: Capital Budgeting

#### ☀️ Project Helios - Solar Investment
**Focus**: NPV analysis with subsidies
- **Key Considerations**:
  - Government incentives
  - Technology risk
  - Environmental benefits
- **NPV Calculation**:
  ```
  Include: Investment tax credits
  Consider: Accelerated depreciation
  Account for: Energy price volatility
  ```

#### 🏠 Patrimonio Hoy - Social Impact
**Focus**: Valuing social enterprises
- **Dual Bottom Line**:
  - Financial returns
  - Social impact metrics
  - Blended value creation

#### 🚢 Ocean Carriers - Capital Investment
**Focus**: Ship purchase decision
- **Analysis Elements**:
  - Freight rate forecasting
  - Vessel depreciation
  - Scrap value consideration
  - Tax jurisdiction effects

### Module 3: Cost of Capital

#### 🏥 Progyny - WACC Calculation
**Focus**: Fertility benefits company valuation
- **WACC Components**:
  - Comparable company betas
  - Appropriate risk-free rate
  - Market risk premium estimation
  - Target capital structure

#### 🎭 Hamilton - Entertainment Finance
**Focus**: Valuing creative properties
- **Unique Challenges**:
  - Revenue predictability
  - Intellectual property valuation
  - Risk assessment for creative works

### Module 4: Portfolio Theory

#### ⚽ Tottenham Hotspurs - Stadium Financing
**Focus**: Sports facility investment
- **Financial Engineering**:
  - Stadium naming rights
  - Seat licenses
  - Revenue diversification
  - Debt structuring

#### 🏛️ Cook County Pension - Asset Allocation
**Focus**: Institutional portfolio management
- **Portfolio Optimization**:
  ```
  Efficient Frontier Construction:
  - Expected returns by asset class
  - Correlation matrix
  - Risk tolerance constraints
  - Liability matching
  ```

### Module 5: Advanced Valuation

#### 🏨 Partners Healthcare - Hospital System
**Focus**: Healthcare consolidation valuation
- **Synergy Analysis**:
  - Cost synergies
  - Revenue synergies
  - Implementation costs
  - Integration timeline

#### 💊 MGH Enbrel Royalty - Pharma Finance
**Focus**: Drug royalty stream valuation
- **Cash Flow Modeling**:
  - Patent expiration
  - Competition entry
  - Market share erosion
  - Probability-weighted scenarios

---

## 📈 Valuation Model Templates

### DCF Model Structure

```
Revenue Projections (5-10 years)
- Growth rates by segment
- Market size constraints
- Competitive dynamics

Operating Costs
- COGS (% of sales)
- SG&A (% of sales or fixed + variable)
- D&A (% of PP&E or CapEx)

Working Capital
- Target days for AR, Inventory, AP
- Calculate annual changes

CapEx
- Maintenance vs growth
- % of sales or specific projects

Free Cash Flow Calculation
EBIT × (1-T)
+ D&A
- CapEx
- ΔNWC
= FCF

Terminal Value
- Gordon Growth: FCF × (1+g) / (WACC-g)
- Multiple: EBITDA × Exit Multiple

Present Value
- Discount FCFs at WACC
- Discount TV at WACC
- Sum = Enterprise Value

Equity Value
Enterprise Value
- Net Debt
+ Cash
= Equity Value

Per Share Value = Equity Value / Shares Outstanding
```

### LBO Model Framework

```
Sources & Uses
Uses:                    Sources:
- Purchase Price         - Senior Debt
- Fees                  - Subordinated Debt
- Refinancing           - Equity
Total Uses = Total Sources

Returns Analysis
Entry Equity = X
Exit Equity = Enterprise Value - Net Debt
IRR = (Exit/Entry)^(1/years) - 1
Money Multiple = Exit/Entry

Credit Metrics
- Debt/EBITDA by year
- Interest coverage
- Fixed charge coverage
- Debt paydown schedule
```

---

## 📝 Common Pitfalls & Solutions

### Valuation Mistakes

| Common Error | Solution |
|-------------|----------|
| Using book value of debt | Use market value |
| Wrong tax rate | Use marginal rate for WACC |
| Inconsistent growth assumptions | Terminal g < economy growth |
| Ignoring working capital | Include in FCF projections |
| Double-counting | Be consistent: FCFF with WACC or FCFE with Re |

### WACC Calculation Errors

| Issue | Correct Approach |
|-------|-----------------|
| Risk-free rate | Match treasury maturity to cash flows |
| Market risk premium | Use long-term historical average (6-8%) |
| Beta | Use industry average if limited history |
| Capital structure | Use target, not current |
| Cost of debt | Use YTM on traded debt or synthetic rating |

---

## 🎓 Exam Preparation Checklist

### Key Exam Dates
- **Test 1**: Tuesday, October 21st
- **Test 2**: Tuesday, November 18th
- **Final Exam**: Monday, December 15th

### Review Sessions
- **Teaching Fellows**: Joy Haddad & Josh Kuppersmith
- **Schedule**: Twice weekly afternoons (check Canvas)
- **Format**: Hybrid (in-person + Zoom)
- **Focus**: Online exercise material after solutions posted
- **Note**: TFs won't review specific cases

### Conceptual Understanding
- [ ] Time value of money concepts
- [ ] DCF valuation methodology
- [ ] WACC components and calculation
- [ ] Capital structure theories
- [ ] Portfolio theory basics
- [ ] Option valuation concepts

### Calculation Skills
- [ ] NPV and IRR calculations
- [ ] WACC computation
- [ ] Free cash flow projections
- [ ] Terminal value calculations
- [ ] Financial ratio analysis
- [ ] Beta levering/unlevering

### Application Ability
- [ ] Build simple DCF model
- [ ] Perform sensitivity analysis
- [ ] Calculate break-even points
- [ ] Evaluate capital projects
- [ ] Assess financing alternatives
- [ ] Value companies in different industries

---

## 📌 Quick Reference

### Essential Formulas Card
```
NPV = Σ(CFt/(1+r)^t) - I0
WACC = (E/V)Re + (D/V)Rd(1-T)
Re = Rf + β(Rm-Rf)
FCF = EBIT(1-T) + D&A - CapEx - ΔNWC
Terminal Value = FCF(1+g)/(WACC-g)
P/E = Price/EPS
EV/EBITDA = (Equity + Debt - Cash)/EBITDA
```

### Discount Rate Guidelines
| Project Type | Risk Adjustment |
|-------------|----------------|
| Expansion | Use firm WACC |
| New market | Add 2-3% premium |
| New product | Add 3-5% premium |
| International | Add country risk premium |
| Start-up | 20-40% rates common |

### Valuation Multiple Ranges
| Industry | Typical EV/EBITDA |
|----------|-------------------|
| Tech/Software | 15-25x |
| Healthcare | 12-18x |
| Consumer | 8-12x |
| Industrial | 6-10x |
| Utilities | 5-8x |

---

## 🔄 Maintenance Instructions

### After Each Class
1. Add case notes using framework
2. Update relevant formulas
3. Include case-specific calculations
4. Note unique valuation challenges
5. Add to module summaries
6. **Review post-class materials**:
   - Classroom Excel models
   - Daily wrap-up slides
   - Section-specific pages on Canvas

### Weekly Practice
1. Build one DCF model
2. Calculate WACC for a company
3. Practice ratio analysis
4. Review TVM problems
5. Work through case calculations
6. Complete online exercises when available
7. Review post-class materials on Canvas

### Before Exams
1. Review all formulas
2. Practice model building
3. Complete sensitivity analyses
4. Review case applications by module:
   - Module 1: Focus on FCF and valuation
   - Module 2: Focus on portfolio theory and CAPM
   - Module 3: Focus on integrated perspectives
5. Check calculation accuracy
6. Review case lineup concepts from Introductory Note

---

*Remember: Finance is about making decisions under uncertainty—master the tools, understand the assumptions, and always consider the context.*