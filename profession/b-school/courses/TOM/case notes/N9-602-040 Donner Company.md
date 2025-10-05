---
# Case Metadata
case_number: "N9-602-040"
title: "Operations at the Donner Company"
course: "TOM"
date_published: 2024-06-24
date_read: 2025-09-09
professor: "TBD"
tags: [case-study, operations, manufacturing, process-analysis, bottlenecks, capacity-planning]
industry: "Electronics Manufacturing"
company: "Donner Company"
geographic_focus: "United States"
key_topics: [capacity management, bottleneck analysis, quality control, delivery performance, process flow]
protagonists: [Edward Plummer, Bruce Altmeyer, David Flaherty, Lloyd Searby]
decision_point: "October 1987 - How to improve productivity, quality, and delivery performance"
teaching_objectives: [process analysis, capacity calculations, bottleneck identification, trade-offs in operations]
---

# Operations at the Donner Company

## Quick Facts
- **Case #**: N9-602-040
- **Course**: [[TOM]]
- **Date Read**: 2025-09-09
- **Industry**: Electronics Manufacturing (Printed Circuit Boards)
- **Geography**: United States

## Executive Summary
> Donner Company, a specialist in low-volume printed circuit board manufacturing for experimental and pilot production runs, faces critical operational challenges in October 1987. President Edward Plummer must address deteriorating productivity, quality problems (returns increased from <1% to 3%), and delivery delays (averaging 9 days late) that threaten to cap sales at $2M instead of the potential $3M if performance improves.

## Case Context

### Company Background
- Founded in 1985, specializes in prototype and small batch PCB production
- Management team consists of engineers with deep electronics industry experience
- Plummer and Altmeyer created patented processes and modified commercial machinery
- Positioned as specialists in anticipating/resolving problems in new designs
- Focus on "soldermask over bare copper" (SMOBC) boards

### Industry Landscape
- 750 PCB manufacturers in the US
- Two categories: captive (in-house for large firms like IBM, AT&T) and contract manufacturers
- Large firms outsource simple high-volume boards or fast-turnaround prototypes
- Industry growth parallels computer, telecommunications, and defense sectors
- Vulnerable to cyclical downturns in these industries

### Timeline of Events
- 1985: Company founded
- January 1986: Moved to current location
- October 1986: Fully utilizing existing plant space
- April 1987: Lloyd Searby joins as sales manager
- August 1987: Hired 8 new production workers; quality/delivery problems begin
- September 1987: 60 orders processed, ranging from 1 to 1,050 boards
- October 1987: Decision point - planning for 1988 operations
- November 1987: 1,800 sq ft addition due for completion

## Key Protagonists
- **Edward Plummer**: President
  - Background: Engineer with substantial electronics experience
  - Key decisions: Process design, capacity planning, operational improvements
  
- **Bruce Altmeyer**: Design Engineer
  - Background: Co-creator of patented processes
  - Key decisions: Inspects artwork, determines processing methods, spends 10 hrs/week on shop floor problems

- **David Flaherty**: Shop Supervisor
  - Background: Reports to Altmeyer
  - Key decisions: Scheduling, work assignments, manages 22 production employees

- **Lloyd Searby**: Sales Manager (joined April 1987)
  - Background: New to company
  - Key decisions: Sales forecasting, concerned about quality/delivery impact on growth

## Central Problem/Decision

### The Question
> How should Donner Company restructure its operations to simultaneously improve productivity, quality, and delivery performance while maintaining its competitive advantage in low-volume, quick-turnaround orders?

### Constraints
1. Limited capital for equipment purchases (already spent $80K on CNC drill)
2. 8 newly hired workers still developing skills (3 more months needed)
3. High product variety (order sizes from 1 to 1,050 boards)
4. Frequent rush orders (4-day delivery) and design changes mid-production
5. Space constraints (addition not complete until November)

### Success Metrics
- Reduce customer returns from 3% to <1%
- Achieve on-time delivery (currently 9 days late average)
- Maintain 3-week delivery promise for orders <1,000 boards
- Reach $3M sales target for 1988
- Improve machine utilization and reduce idle time

## Analysis

### Strengths
- Technical expertise and patented processes
- Experienced management team from electronics industry
- Arthur Dief's perfect record on small orders (≤8 boards)
- CNC drill provides automated capability for larger orders
- Strong position in prototype/pilot production niche

### Weaknesses
- Unpredictable daily bottlenecks without clear pattern
- Poor scheduling visibility (Flaherty waits for materials before scheduling)
- Inefficient work methods (plater walks 18 feet repeatedly)
- No formal quality standards enforcement
- Standards don't reflect actual rework/movement time
- Worker reassignments create confusion and friction

### Opportunities
- Sales could reach $3M with improved delivery performance
- Competitors moving to 4-week delivery creates differentiation opportunity
- 1,800 sq ft expansion coming in November
- Process improvements possible in nearly every operation
- Better utilization of CNC drill for appropriate orders

### Threats
- Competition from 750 other PCB manufacturers
- Large customers may bring complex boards in-house
- Cyclical industry vulnerable to economic downturns
- Sales capped at $2M if forced to match competitor 4-week delivery
- New workers causing quality issues

## Financial Analysis
| Metric | September 1987 | August 1987 | Notes |
|--------|----------------|-------------|-------|
| Net Sales | $124,800 | $144,400 | Monthly variation |
| Gross Profit | 12.7% | 18.8% | Declining margins |
| Net Profit | 2.5% | 10.25% | Significant drop |
| Direct Labor % | 25.9% | 22.6% | Rising labor costs |
| Pre-shipment Rejects | 7% | - | 1% losses, 6% rework |
| Customer Returns | 3% | <1% | Tripled since August |
| Late Deliveries | 9 days | 10 days | Persistent problem |

## Key Exhibits
- Exhibit 1: P&L showing declining profitability (2.5% in Sept vs 10.25% in Aug)
- Exhibit 2: Standard production times - 1,536 total hours for September
- Exhibit 3: $80,000 CNC Micronic-Jr. drill (policy: only for orders >100 boards)
- Exhibit 4: Order size distribution - 60 orders ranging from 1 to 1,050 boards
- Exhibit 5: Shipping pattern - heavy end-of-month concentration

## Discussion Questions

### Official Assignment Questions
1. **Process Flow Diagram**: Draw a process flow diagram representing the typical operations at Donner's production. For simplicity, you only need to go up to the soldermask step.

2. **CNC Drill Scheduling**: What orders would you schedule on the Micronic Jr. CNC drill? (Note that customer orders that are sent to Manual Drilling are assigned to ONE of the seven drills. Orders are never split among multiple drills.)

   **Answer**: 
   
   **Breakeven Analysis:**
   For an order of n boards with 500 holes/board:
   - Manual Time = 15 + (n × 500 × 0.08) = 15 + 40n minutes
   - CNC Time = 240 + (n × 500 × 0.004) = 240 + 2n minutes
   - Setting equal: 15 + 40n = 240 + 2n → **n = 5.9 boards**
   
   **Recommended CNC Scheduling Policy:**
   - **Always CNC**: Orders ≥ 30 boards (frees manual capacity)
   - **CNC if manual busy**: Orders 6-29 boards when manual utilization >85%
   - **Always Manual**: Orders ≤ 5 boards (below breakeven)
   
   **Rationale**: The 7 manual stations provide parallel processing capability. Small orders should use manual stations even above the 6-board breakeven to preserve CNC capacity for larger orders. The current 100-board policy severely underutilizes the $80,000 CNC investment.

3. **Electroplate Capacity Analysis**: 
   - What is the capacity of just the electroplate process step for a 1-panel (i.e., 8 boards) order? 
   - For a 5-panel order? 
   - Using these calculations and perhaps a few more for other order sizes, sketch a graph of the capacity of the electroplate operation versus order size (in boards). 
   - How do you explain the shape of this graph?

   **Answer**:
   
   From Exhibit 2: Setup = 25 min, Run = 8.5 min/panel
   
   **1-Panel Order (8 boards):**
   - Total Time = 25 + (1 × 8.5) = 33.5 minutes
   - Capacity = 1 panel/33.5 min = 1.79 panels/hour = **14.33 boards/hour**
   
   **5-Panel Order (40 boards):**
   - Total Time = 25 + (5 × 8.5) = 67.5 minutes  
   - Capacity = 5 panels/67.5 min = 4.44 panels/hour = **35.56 boards/hour**
   
   **General Formula:** Capacity = 480N/(25 + 8.5N) boards/hour
   
   **Graph Shape:** Concave curve starting at 14.33 boards/hr for small orders, asymptotically approaching 56.47 boards/hr (480/8.5) for large orders. Shows diminishing returns as setup time impact decreases with order size.

4. **Utilization Calculations**: 
   - During September 1987, what was the labor utilization for the overall process? 
   - What was the machine utilization for electroplate?

   **Answer**:
   
   **Labor Utilization:**
   - Standard production hours (Exhibit 2): 1,535.9 hours
   - Available hours: 22 employees × 8 hrs/day × 22 days = 3,872 hours
   - **Labor Utilization = 1,535.9 / 3,872 = 39.7%**
   
   **Electroplate Machine Utilization:**
   - Electroplate hours used (Exhibit 2): 127.0 hours
   - Available machine hours: 8 hrs/day × 22 days = 176 hours
   - **Machine Utilization = 127.0 / 176 = 72.2%**

5. **Problem Identification**: What are the discernible problems facing Donner?

   **Answer**:
   
   **Operating Problems:**
   1. **Unpredictable bottlenecks** - Shift daily without pattern
   2. **Quality failures** - Returns increased from 1% to 3%
   3. **Late deliveries** - Averaging 9 days late
   4. **Low productivity** - Only 39.7% labor utilization
   5. **Inefficient methods** - Plater walks 18 feet repeatedly (15% wasted time)
   
   **Management Problems:**
   6. **Poor scheduling visibility** - Flaherty waits for materials before scheduling
   7. **New worker training** - 8 workers hired in August still learning
   8. **No quality standards** - Standards vary by customer/order
   9. **Incomplete operations** - 6% of September production required rework
   10. **End-of-month shipping** - Creates uneven workflow (see Exhibit 5)

### Key Assumptions for Analysis
- Donner operates one 8-hour shift per workday
- All setups occur "on-the-line" (setup for an order at each process step is not performed until the previous order has completed that step)
- Orders sent to manual drilling are assigned to ONE of the seven drills (never split)

## My Analysis & Recommendations

### Black Ink Analysis (Pre-Class)

#### Industry Positioning
- **Circuit board manufacturer** - Operating in highly technical, precision-dependent electronics supply chain
- Position requires balancing quality, delivery, and cost in custom/low-volume segment
- Customer relationships critically dependent on reliability and technical capability

#### Operational Performance Diagnosis
- **Quality Issues**:
  - Preshipment rejection = 7% (6% due to incomplete operations, 1% total losses)
  - Informal inspections causing false negatives (25 "perfect" boards rejected for minor nicks)
  - Customer returns increased from 1% to 3%

- **Delivery Performance**:
  - Shipments averaging 9 days late
  - End-of-month shipping concentration creating workflow imbalance
  - Four-day rush orders disrupting normal production flow

- **Productivity Problems**:
  - Plater spending 15% of time walking between desk and tanks
  - Only 39.7% labor utilization despite apparent bottlenecks
  - CNC drill underutilized due to >100 board policy

#### Root Cause Analysis
- **Quantifiable issues across productivity, quality, delivery** - not isolated problems
- Systemic failures in:
  - Scheduling visibility (Flaherty waits for materials before scheduling)
  - Process standardization (quality standards vary by customer)
  - Resource allocation (daily reassignments causing confusion)
  - Equipment utilization (arbitrary policies vs. economic analysis)

### Recommended Action
> Implement a hybrid approach addressing both technology and process improvements:
> 1) Create dedicated small-order cell for orders ≤30 boards (Arthur Dief model)
> 2) Purchase additional CNC drill to eliminate drilling bottleneck
> 3) Implement detailed output measurement at each operation for better visibility
> 4) Develop standard quality specifications and formal inspection protocols

### Implementation Plan
1. **Immediate (Week 1-2)**: Calculate true CNC breakeven; implement operation-level metrics
2. **Short-term (Month 1)**: Establish small-order cell; standardize quality criteria
3. **Medium-term (Month 2-3)**: Install second CNC machine; train on bottleneck management
4. **Long-term (Month 4+)**: Use November expansion for cellular manufacturing layout

## Class Discussion Notes

### My Participation
- **Times Spoken**: [Not tracked]
- **Cold Called**: [Not tracked]

### Key Insights from Discussion

#### Strategic Solution Framework
The class developed a comprehensive approach to Donner's problems:
- **CNC Machine Investment**: Purchase additional CNC drill to reduce bottlenecks at drilling operation
- **Quality System Overhaul**: Move from informal to formal inspection with standardized criteria
- **Detailed Performance Measurement**: Implement output tracking at each operation for visibility
- **Scheduling Improvements**: Develop better visibility into WIP and upcoming order requirements

#### Small Batch Manufacturing Reality
- **Small batch orders** are Donner's core competency but create inherent complexity
- Traditional high-volume manufacturing approaches don't translate to this environment
- Need different metrics focused on flexibility and responsiveness vs. pure efficiency
- Arthur Dief's success with small orders validates dedicated cell approach

#### Technology vs. Process Solutions
Discussion revealed tension between:
- Equipment purchases (another CNC machine) as quick fixes
- Process improvements (better scheduling, quality standards) as sustainable solutions
- Consensus: both needed but process improvements have higher ROI

### Alternative Perspectives
- Some argued for focusing on order selection - reject unprofitable small orders
- Others suggested pricing strategy changes to discourage rush orders
- Debate on whether to specialize further or try to serve broader market
- Discussion on whether informal quality standards actually provide competitive advantage through flexibility

### Professor's Takeaways
- Bottleneck management in high-mix environments requires different approaches than traditional TOC
- Equipment utilization policies must be based on economic analysis, not rules of thumb
- Quality problems often stem from system design, not worker performance
- Small improvements in process design can exceed benefits of major capital investments 

## Personal Reflections & Key Takeaways

### Synthesis of Learning
1. **Bottleneck Management in High-Mix Environments**: The case demonstrates that traditional bottleneck management fails when product variety is extreme. Donner's daily shifting bottlenecks aren't a flaw but an inherent characteristic of high-mix, low-volume manufacturing. Class discussion reinforced that the solution isn't finding "the" bottleneck, but creating flexible systems with real-time visibility. The professor's emphasis on TOC limitations in this context challenged conventional operations thinking.

2. **Economic vs. Arbitrary Decision Rules**: The CNC drill policy (>100 boards) exemplifies how arbitrary thresholds destroy value. With actual breakeven at 6 boards, Donner wastes $80,000 equipment while overloading manual stations. The class consensus that "all policies must be economically justified" extends beyond equipment to quality standards, order acceptance, and resource allocation decisions.

3. **Technology vs. Process Improvement Balance**: While my pre-class analysis favored buying another CNC machine, the discussion revealed that process improvements (scheduling visibility, quality standards, cellular layout) offer higher ROI. The professor's point that "small improvements in process design can exceed benefits of major capital investments" fundamentally shifts how I'll approach operational problems.

4. **The Small Batch Paradox**: Donner's core competency in small batch/custom work creates the very complexity that undermines performance. The class insight that these operations need "different metrics focused on flexibility and responsiveness vs. pure efficiency" explains why traditional manufacturing solutions fail. Arthur Dief's success validates that specialized approaches for distinct order types outperform universal flexibility.

### Applications to Future Situations
- Audit all operational policies for economic justification - legacy rules often persist without scrutiny
- In high-variety operations, design for rapid constraint identification rather than constraint elimination
- Consider dedicated resources for distinct order types rather than pursuing complete flexibility
- Small batch manufacturing requires fundamentally different metrics and management systems than high-volume production

### Questions for Further Research
- How can real-time constraint identification systems be implemented in high-mix environments?
- What's the optimal degree of cellular manufacturing for different volume/variety combinations?
- How do digital twins and simulation help manage unpredictable bottleneck patterns?

## Related Cases & Readings
- [[Process Fundamentals Reading]]
- [[Benihana of Tokyo]] - process design and capacity
- [[National Cranberry]] - bottleneck analysis

## Additional Resources
- Goldratt's "The Goal" - Theory of Constraints
- Quick changeover techniques for reducing setup times
- Cellular manufacturing design principles

---
*Original PDF*: [[N9-602-040 Donner Company.pdf]]