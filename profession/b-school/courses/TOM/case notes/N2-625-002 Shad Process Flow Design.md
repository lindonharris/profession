---
# Case Metadata
case_number: "N2-625-002"
title: "Shad Process Flow Design"
course: "TOM"
date_published: 2025-08-12
date_read: 2025-10-08
class_number: 10
professor: "Allison Mnookin"
tags: [case-study, operations-management, process-design, simulation-exercise, lean-manufacturing, kaizen]
industry: "Electronics Manufacturing"
company: "Small Electronics Manufacturing Company (OEM)"
geographic_focus: "N/A - Simulation Exercise"
key_topics: [process-flow-design, takt-time, cycle-time, materials-requirements-planning, quality-management, kaizen, variability-management, inventory-optimization]
protagonists: ["Student Team (Factory Demonstration Team)"]
decision_point: "Design and optimize a production process for three product models while managing uncertain demand, quality requirements, and cost constraints"
teaching_objectives: [process-design-fundamentals, work-decomposition-serial-vs-parallel, materials-requirements-planning, quality-process-integration, continuous-improvement-kaizen, operations-strategy]
---

# Shad Process Flow Design

## Quick Facts
- **Case #**: N2-625-002
- **Course**: [[TOM]]
- **Class #**: 10
- **Date Read**: 2025-10-08
- **Industry**: Electronics Manufacturing
- **Geography**: N/A - Simulation Exercise

## Executive Summary
This is a hands-on simulation exercise where student teams design and operate a production process for three models of light-flashing electronic modules (Economy, Deluxe, Imperial) for an OEM customer. Teams must manage uncertain demand arriving every 30 seconds, maintain perfect quality and sequence delivery, implement materials requirements planning, and conduct kaizen improvements between two factory demonstration runs while maximizing net profit.

## Case Context

### Company Background
- Small electronics manufacturing company producing products for OEM customers
- Hired to design production process for new innovative light-flashing electronic module
- Three product models with varying complexity and revenue:
  - **Economy**: $250 revenue, simplest design (Green LED, 2 resistors, capacitor)
  - **Deluxe**: $260 revenue, medium complexity (Red LED, 3 resistors, capacitor)
  - **Imperial**: $325 revenue, most complex (Yellow LED, Buzzer, 2 resistors, capacitor)

### Industry Landscape
- Low-margin business requiring efficient materials usage and quick order fulfillment
- Extremely quality-conscious customer with zero defect tolerance
- Competitive pressure on cost, quality, and delivery performance
- Just-in-time delivery expectations with sequence accuracy requirements

### Timeline of Events
- **Day 1 (October 8, 2025)**:
  - 3:00 pm: Kick-off session in Aldrich classrooms
  - 3:45-9:00 pm: Organization, practice, and process design session
  - Teams develop process design, test materials, assign roles, enter design into Shad Universe
- **Day 2 (October 9, 2025)**:
  - 8:30-9:00 am: Setup and preparation
  - 9:00-10:42 am: Factory Demonstration Run 1
  - 10:42-11:50 am: Kaizen session with customer feedback and process improvements
  - 1:20-3:03 pm: Factory Demonstration Run 2 (with improvements)
  - 3:30-4:00 pm: Cleanup and materials kit return

## Key Protagonists
- **Student Team (Factory Demonstration Team)**: Responsible for designing production process, managing operations
  - **Team Captain**: Overall coordination, role assignments, submissions to Shad Universe
  - **Co-Captain** (optional): Spread captain responsibilities
  - **Chief Financial Officer**: Financial planning for operations
  - **MRP Lead**: Material requirements planning and inventory management
  - **Supply Chain Manager**: Inbound materials management and supplier coordination
  - **Direct Labor**: Production workers executing assembly tasks

- **Customer Audit Team**: Simulates customer receiving, quality inspection, and acceptance process
  - **Receiving Auditor**: Records product deliveries
  - **Functional Quality Auditor**: Tests product functionality
  - **Visual Quality Auditors**: Inspects appearance and specifications
  - **Acceptance Auditor**: Verifies sequence and accepts products
  - **Rejection Auditor**: Logs all defects
  - **Procurement Auditors**: Operates supply depot for materials ordering
  - **Factory Liaison(s)**: Observes and provides feedback for kaizen

## Central Problem/Decision

### The Question
How should the team design and operate a production process that can:
1. Meet uncertain customer demand arriving every 30 seconds (takt time)?
2. Produce three different product models in varying mix (50% Economy, 33% Deluxe, 17% Imperial)?
3. Deliver products in exact sequence ordered with perfect quality?
4. Minimize costs while managing inventory efficiently?
5. Continuously improve through kaizen methodology?

### Constraints
1. **Product specifications**: No deviations permitted from design specs (Exhibits 1-3)
2. **Quality requirements**: 100% functional and visual inspection, zero defects tolerance
3. **Sequence delivery**: Out-of-sequence products rejected even if correct model
4. **Customer demand**: 1 order every 30 seconds, uncertain mix and sequence
5. **Materials ordering**: Only during first minute of each 3-minute window, 9 board maximum per order, 60 boards total per run
6. **Cost structure**: 5% inventory holding charge on maximum inventory value during any period
7. **Physical workspace**: Fixed table setup configuration
8. **Time constraints**: 15-30 minute demonstration runs

### Success Metrics
- **Net Profit**: Gross profit (revenue - COGS) minus 5% inventory holding charge
- **Revenue**: Only from accepted products ($250 Economy, $260 Deluxe, $325 Imperial)
- **Quality metrics**: Functional rejects, visual rejects, sequence rejects
- **Delivery responsiveness**: Time from order to acceptance
- **Inventory efficiency**: Minimizing WIP and finished goods inventory
- **Throughput**: Units delivered per hour

## Analysis

### Process Design Considerations

#### Work Decomposition and Takt Time
- **Takt time**: 30 seconds per unit (120 units/hour demand rate)
- **Model-specific takt times**:
  - Economy: 60 seconds (50% of mix)
  - Deluxe: 90 seconds (33% of mix)
  - Imperial: 180 seconds (17% of mix)
- **Key decision**: Serial vs. parallel work decomposition
  - If single worker cycle time > takt time → must decompose work
  - Parallel processing can reduce cycle time but increases coordination complexity
  - Balance line to match bottleneck to takt time

#### Variability Management
- **Demand variability**: Uncertain sequence and exact mix within hours
- **Process variability**: Worker cycle time variations, assembly complexity differences
- **Quality variability**: Defect occurrences requiring rework
- **Material variability**: Two interchangeable buzzer types, two capacitor types, chip orientation variations
- **Buffer strategies**:
  - WIP buffers between process steps
  - Finished goods inventory to decouple from demand spikes
  - Trade-off: Responsiveness vs. inventory costs

#### Materials Requirements Planning (MRP)
- **Lead time**: 3-minute ordering windows (order in first minute, receive in third minute)
- **Ordering constraints**: Maximum 9 boards per window, 60 total per run
- **Inventory costs**: 5% of maximum inventory value held
- **Strategy considerations**:
  - Build-to-stock vs. build-to-order vs. hybrid
  - Safety stock levels for uncertain demand
  - Consumption-based replenishment tracking
  - Wire management (sold by cm, used in 2cm or 4cm lengths)

#### Quality Process Integration
- **Inspection points**:
  - IC chip orientation check (pin 1 at F14)
  - Functional test (battery snap contact)
  - Visual inspection (component positions, wire colors/lengths ±1cm, specifications)
  - Sequence verification
- **Defect handling**: Rejected units return to factory inventory, no revenue credit
- **Prevention strategies**: Standardized work methods, poka-yoke, quality at source

### Strengths (of Exercise Design)
- Realistic simulation of operations challenges: demand uncertainty, quality requirements, cost pressures
- Hands-on experiential learning of process design concepts
- Real-time feedback through Shad Universe app metrics
- Kaizen practice for continuous improvement mindset
- Team collaboration and role specialization experience

### Weaknesses (Potential Challenges)
- Short practice time (5 hours) to design, test, and refine process
- Materials kit limitations (must reuse components, limited wire)
- Coordination complexity between factory and audit teams
- Physical workspace constraints
- Learning curve on Shad Universe app functionality

### Opportunities
- Apply process fundamentals: takt time, cycle time, throughput time, Little's Law
- Experiment with lean principles: reduce muda (7 wastes), implement 5S
- Test different production strategies: push vs. pull, batch vs. one-piece flow
- Practice root cause analysis and problem-solving
- Develop leadership and team management skills

### Threats
- Quality defects leading to revenue loss and sequence disruptions
- Inventory accumulation causing profitability erosion
- Materials shortages from poor MRP execution
- Team coordination breakdowns during high-pressure demonstration
- Insufficient kaizen improvements between runs

## Financial Analysis
| Component | Cost | Notes |
|--------|-------|-------|
| Circuit Board + IC Chip | $150 | Highest cost component, pre-assembled |
| Capacitor (100 µF) | $10 | Two interchangeable types available |
| LED (any color) | $10 each | Red, Green, or Yellow |
| Buzzer | $75 | Two interchangeable types, only for Imperial |
| Resistor (1KΩ ¼W) | $10 | All models use 2 resistors |
| Wire (any color) | $2.50/cm | Sold by cm, used in 2cm or 4cm lengths |
| Bare wire | $2.50/cm | Made by stripping green wire |

**Product COGS and Gross Margin**:
- **Economy**: COGS ~$210 (board $150 + LED $10 + 2 resistors $20 + capacitor $10 + wire $20) → Margin $40 (16%)
- **Deluxe**: COGS ~$220 (board $150 + LED $10 + 3 resistors $30 + capacitor $10 + wire $20) → Margin $40 (15%)
- **Imperial**: COGS ~$295 (board $150 + LED $10 + buzzer $75 + 2 resistors $20 + capacitor $10 + wire $30) → Margin $30 (9%)

**Inventory Holding Charge**: 5% of maximum inventory value during any 3-minute window

## Key Exhibits
- **Exhibit 1**: Economy Model design specifications (Green LED, 2 resistors, capacitor, specific wire routing)
- **Exhibit 2**: Deluxe Model design specifications (Red LED, 3 resistors, capacitor, different wire configuration)
- **Exhibit 3**: Imperial Model design specifications (Yellow LED, buzzer, 2 resistors, capacitor, most complex wiring)
- **Exhibit 4**: Process Design Assignment template (philosophy, metrics, critical design considerations)
- **Exhibit 5-6**: Materials Kit contents and packing list (60 boards, ~350 resistors, LEDs, buzzers, wire, tools)
- **Exhibit 7**: Component details (IC chip orientation, interchangeable buzzers/capacitors, wire types)
- **Exhibit 8**: Material costs and revenue credits by product model
- **Exhibit 9**: Factory table setup configuration
- **Exhibit 10**: Shad Universe app functionality (Dashboard, Materials, Product Deliveries tabs)
- **Exhibit 11-12**: Customer Audit table layout and process flow
- **Exhibit 13**: Customer Audit Team roles and responsibilities
- **Exhibit 14**: Factory Simulation detailed timeline (T-6:00 through T+27:00)

## Discussion Questions
1. **What do you know about customer demand? How do you plan to meet it?**
   - Customer orders 1 unit every 30 seconds (takt time)
   - Expected mix: 50% Economy, 33% Deluxe, 17% Imperial (but uncertain sequence)
   - Must deliver in exact sequence ordered
   - Strategy: Calculate cycle times for each model, determine if single worker can meet takt or needs work decomposition, decide on build-to-stock buffer vs. build-to-order approach

2. **As you look at the product designs in Exhibit 1, 2, and 3, imagine how you might set up a factory and break up the work if one person cannot create a board fast enough to meet demand. Would you decompose your assembly work into serial or parallel processes? Why? What will impact the sequence of work?**
   - Serial advantages: Simpler coordination, easier quality control, less training needed
   - Parallel advantages: Faster throughput if cycle time > takt time, can balance workload
   - Sequence considerations: Component proximity, logical assembly order (base → components → wiring → testing), minimize handling, group similar tasks
   - Trade-offs: Communication overhead, WIP buffers between stations, line balancing challenges

3. **What are the cost levers? Consider how might you plan to procure and manage inventory.**
   - **Cost levers**:
     - Material procurement timing and quantities (avoid excess inventory charges)
     - Defect reduction (rejected units = lost materials + no revenue)
     - Inventory levels (5% holding charge on maximum value)
     - Production strategy (build-to-stock vs. build-to-order)
   - **Inventory management**:
     - Develop MRP spreadsheet tracking consumption rates
     - Order based on actual usage, not forecasts
     - Balance safety stock vs. holding costs
     - Monitor work-in-process levels between stations

4. **What actions might you take to enable your team to improve?**
   - **Before Run 1**: Practice assembly, time operations, standardize work methods, assign clear roles, test materials ordering process
   - **During Kaizen**: Use customer feedback, apply 7 wastes framework, implement 5S principles, prototype improvements, measure KPI changes
   - **For Run 2**: Refine process flow, improve quality checks, optimize inventory levels, enhance team communication, implement lessons learned

## My Analysis & Recommendations

### Option 1: Build-to-Stock with Buffer Inventory
**Approach**: Build initial inventory during T-6:00 to T=0:00 prep time, maintain finished goods buffer
**Pros**:
- Decouples production from demand variability
- Can smooth production pace
- Reduces pressure on workers during demonstration
- Accommodates cycle time > takt time situations

**Cons**:
- High inventory holding costs (5% charge)
- Risk of wrong product mix in buffer
- Capital tied up in WIP and finished goods
- May not respond well to demand shifts

### Option 2: Pure Build-to-Order (Pull System)
**Approach**: No finished goods inventory, produce exactly to each order as received
**Pros**:
- Minimizes inventory holding costs
- Perfect sequence delivery (produce in order)
- No obsolescence risk
- Lean operations

**Cons**:
- Requires cycle time ≤ takt time for all models
- High pressure on workers
- No buffer for quality issues
- Vulnerable to process disruptions

### Option 3: Hybrid Approach (Recommended)
**Approach**: Small finished goods buffer (2-3 units per model), produce primarily to order with safety stock
**Pros**:
- Balances inventory costs and operational flexibility
- Can handle minor quality issues without sequence disruption
- Moderate pressure on workers
- Responsive to demand while maintaining buffer

**Cons**:
- Still incurs some inventory costs
- Requires sophisticated MRP management
- Buffer size optimization challenging

### Recommended Action
**Implement Hybrid Approach with Kaizen Focus**

**Process Design**:
1. **Work Decomposition**: 2-3 station serial flow
   - Station 1: IC board QC check, resistors placement
   - Station 2: LED, capacitor, buzzer (if needed) placement
   - Station 3: Wire cutting and installation, functional test

2. **Initial Inventory Strategy**:
   - T-6:00 to T=0:00: Build 3 Economy, 2 Deluxe, 1 Imperial (6 units FG buffer)
   - Estimated inventory value: ~$1,500, holding charge ~$75

3. **MRP Strategy**:
   - Pre-order 9 boards at T-6:00, T-3:00 to start with 18 boards
   - Order materials every 9-12 minutes (3-4 windows) based on consumption
   - Track inventory via Excel: Beginning + Purchases - Accepted = Ending

4. **Quality Process**:
   - IC chip orientation check at Station 1
   - In-process checks at each station
   - Functional test before delivery (battery snap)
   - Standardized work instructions with photos

### Implementation Plan
1. **Day 1 Practice (3:45-9:00 pm)**:
   - First hour: Time all operations, measure cycle times, identify bottlenecks
   - Second hour: Design 2-3 station layout, create standard work procedures
   - Third hour: Practice full production runs, test MRP ordering process
   - Fourth hour: Role assignments, Shad Universe familiarization, process design submission
   - Final hour: Final practice run with metrics tracking

2. **Day 2 Run 1 (9:00-10:42 am)**:
   - Execute designed process
   - Track metrics: defects, inventory levels, delivery times, revenue
   - Observe pain points and improvement opportunities

3. **Kaizen Session (10:42-11:50 am)**:
   - Receive customer feedback (first 10 minutes)
   - Review intact demonstration area for insights
   - Brainstorm improvements using 7 wastes framework
   - Test improvements and measure KPI changes
   - Document on whiteboard, submit photo to Shad Universe

4. **Day 2 Run 2 (1:20-3:03 pm)**:
   - Implement kaizen improvements
   - Target metrics: Reduce defects by 50%, reduce inventory by 25%, maintain/improve throughput

## Class Discussion Notes
> [To be filled during/after class discussion]

### My Participation
- **Times Spoken**: 0
- **Cold Called**: No

### Key Insights from Discussion
-

### Alternative Perspectives
-

### Professor's Takeaways
-

## Personal Reflections & Key Takeaways

### Synthesis of Learning
1. **Process design requires balancing competing objectives**: This exercise crystallizes the fundamental tension in operations management between cost (inventory), quality (defects), and delivery (responsiveness). The 5% inventory holding charge forces teams to minimize buffer stock, but zero-defect tolerance and sequence requirements create pressure for safety inventory. The optimal solution likely involves sophisticated real-time decision-making rather than a fixed strategy.

2. **Takt time is the heartbeat of production systems**: Understanding that customer demand rate (30 seconds) dictates the maximum allowable cycle time is crucial. If any model's assembly exceeds its takt time, work decomposition becomes mandatory. This connects directly to line balancing concepts and the importance of measuring process capabilities before designing the system.

3. **Kaizen mindset transforms continuous improvement from concept to practice**: The structured approach to identifying muda (7 wastes), applying 5S principles, and measuring KPI impacts provides a repeatable framework for operational excellence. The time-boxed nature of the kaizen session mirrors real-world constraints and emphasizes rapid experimentation and learning.

### Applications to Future Situations
- Manufacturing process design: Use takt time calculations and cycle time measurements to determine optimal work decomposition
- Inventory optimization: Balance holding costs against service level requirements using quantitative models
- Quality management: Integrate inspection points strategically rather than relying on end-of-line detection
- Team leadership: Clear role definition and cross-training enable flexibility and backup capacity
- Continuous improvement: Regular structured kaizen events can yield significant operational gains

### Questions for Further Research
- How do real-world manufacturers handle product mix uncertainty and sequence requirements?
- What simulation tools exist for process design validation before physical implementation?
- How can statistical process control be integrated into manual assembly operations?
- What are best practices for MRP parameter setting (reorder points, safety stock) in uncertain demand environments?
- How do lean principles scale from manual assembly to automated production lines?

## Related Cases & Readings
- [[624-092 Hospital for Special Surgery]] - Process redesign and operational efficiency
- [[9-606-015 Toyota Production System]] - Lean manufacturing principles
- [[9-693-051 Quality Management at Dell Computer]] - Quality integration in assembly operations

## Additional Resources
- Shad Universe Portal: https://shad-universe.app (access via Canvas)
- Team Assignments: Available on Canvas
- Shad Simulation Clarifications Document: Canvas link
- Product demonstration videos: QR codes in Exhibits 1-3
- Kaizen methodology: HBS Note 619-016 "Conducting a Kaizen" by Willy Shih

---
*Original PDF*: [[N2-625-002.pdf]]
