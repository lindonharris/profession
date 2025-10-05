# TOM Study Guide
*Technology and Operations Management - Living Document for Process Excellence & Operational Strategy*

> **Last Updated**: September 2025
> **Professor**: Allison Mnookin - Section C
> **Course**: Technology and Operations Management (TOM-C), Fall 2025

---

## 📚 How to Use This Guide

This guide serves as your comprehensive TOM reference, designed to:
- Master process analysis and optimization
- Build capacity planning and bottleneck management skills
- Understand supply chain dynamics
- Apply continuous improvement methodologies

**Navigation Tips:**
- Use calculation templates for problem sets
- Reference process mapping symbols and conventions
- Practice bottleneck identification on cases
- Review formulas before exams

---

## 🏭 Core Operations Frameworks

### 1. Process Analysis Fundamentals

#### Process Metrics
| Metric | Formula | Units | Interpretation |
|--------|---------|-------|----------------|
| **Flow Time (T)** | Time from start to finish | Time | Total time in system |
| **Throughput Rate (R)** | Units completed / Time period | Units/Time | System output rate |
| **Work-in-Process (WIP)** | Units in system | Units | Inventory in process |
| **Cycle Time (CT)** | Time between unit completions | Time/Unit | Pace of production |
| **Utilization (U)** | Actual output / Capacity | % | Resource usage |
| **Efficiency** | Standard time / Actual time | % | Performance vs standard |

#### Little's Law
**WIP = Throughput Rate × Flow Time**
```
I = R × T
```

Applications:
- Restaurant: Customers = Arrival Rate × Time in Restaurant
- Hospital: Patients = Admission Rate × Length of Stay
- Factory: Inventory = Production Rate × Lead Time

### 2. Process Types & Characteristics

#### Process Archetypes
| Type | Volume | Variety | Examples | Characteristics |
|------|--------|---------|----------|-----------------|
| **Job Shop** | Low | High | Custom furniture, R&D | Flexible, high skill, high cost/unit |
| **Batch** | Medium | Medium | Bakery, Pharmaceuticals | Some standardization, setup times |
| **Line Flow** | High | Low | Auto assembly, Fast food | Standardized, efficient, inflexible |
| **Continuous** | Very High | Very Low | Oil refining, Chemicals | Capital intensive, 24/7 operation |

#### Product-Process Matrix
```
         Low Volume          High Volume
         High Variety        Low Variety

High    | Job Shop  →  Batch Process |
Flex    |     ↘              ↘      |
        | (Off diagonal = inefficient)|
Low     | Batch  →  Line  →  Continuous|
Flex    |                            |
```

### 3. Capacity Analysis

#### Bottleneck Identification
1. **Calculate capacity** of each step: Units/Time
2. **Find minimum capacity** = Bottleneck
3. **System capacity** = Bottleneck capacity
4. **Utilization** = Demand / Capacity

#### Capacity Calculations
```
Capacity = (# Resources × Time Available) / Processing Time per Unit

Effective Capacity = Theoretical Capacity × Availability × Performance × Quality
                   = Theoretical × OEE (Overall Equipment Effectiveness)
```

#### Theory of Constraints (TOC)
1. **Identify** the constraint (bottleneck)
2. **Exploit** the constraint (maximize utilization)
3. **Subordinate** everything to the constraint
4. **Elevate** the constraint (add capacity)
5. **Repeat** (find new constraint)

### 4. Variability & Uncertainty Management

#### Sources of Variability
- **Arrival variability**: Customer demand patterns
- **Processing variability**: Task time variations
- **Resource variability**: Machine breakdowns, worker absence

#### Impact of Variability
**Kingman's Formula** (VUT Equation):
```
Average Wait Time = (V × U × T)

Where:
V = Variability factor (CV²arrival + CV²process)/2
U = Utilization (ρ = λ/μ)
T = Average processing time
```

Higher variability → Longer queues → Lower effective capacity

#### Buffering Strategies
1. **Inventory buffers**: Safety stock
2. **Capacity buffers**: Extra resources
3. **Time buffers**: Lead time padding

---

## 📊 Operations Analysis Toolkit

### 1. Process Flow Diagramming

#### Standard Symbols
```
○ = Start/End
□ = Process/Activity
◇ = Decision
△ = Inventory/Storage
→ = Flow direction
⟳ = Rework loop
```

#### Process Mapping Steps
1. **Define boundaries**: Start and end points
2. **List activities**: All process steps
3. **Sequence activities**: Order and dependencies
4. **Add decision points**: Where flow splits
5. **Identify resources**: Who/what performs each step
6. **Measure metrics**: Time, cost, quality at each step

### 2. Queueing Theory Basics

#### M/M/1 Queue (Single Server)
```
Arrival rate: λ
Service rate: μ
Utilization: ρ = λ/μ (must be < 1)

Average # in system (L): ρ/(1-ρ)
Average # in queue (Lq): ρ²/(1-ρ)
Average time in system (W): 1/(μ-λ)
Average wait time (Wq): ρ/(μ-λ)
```

#### M/M/c Queue (Multiple Servers)
- More complex formulas
- Lower wait times than c separate M/M/1 queues
- Pooling benefit from shared queue

### 3. Inventory Management

#### Economic Order Quantity (EOQ)
```
EOQ = √(2DS/H)

Where:
D = Annual demand
S = Setup/ordering cost
H = Holding cost per unit per year

Total Cost = (D/Q)S + (Q/2)H + DC
```

#### Newsvendor Model
```
Critical Ratio = (Price - Cost)/(Price - Salvage Value)
               = Cu/(Cu + Co)

Order quantity where: P(Demand ≤ Q*) = Critical Ratio
```

#### Safety Stock
```
Safety Stock = z × σ × √L

Where:
z = Service level z-score
σ = Demand standard deviation
L = Lead time
```

---

## 💼 Case Repository & Applications

### Manufacturing Operations

#### 🏭 Donner Company - PCB Manufacturing
*[Case Notes](case%20notes/N9-602-040%20Donner%20Company.md)*
*[Process Flow Diagrams](case%20notes/Donner%20Process%20Flow.md)*

**Focus**: Job shop vs line flow decision based on order size
- **Key Trade-offs**:
  - Setup time vs processing efficiency
  - Flexibility vs standardization
  - Order size breakeven analysis
- **Process Analysis**:
  - Manual vs CNC drilling decision point
  - Bottleneck shifts with product mix
  - Setup time impact on small orders
- **Calculations**:
  ```
  Breakeven: Manual Time = CNC Setup + CNC Run Time
  Manual: 0.5 min/hole × N holes
  CNC: 240 min setup + 0.08 min/hole × N holes
  Breakeven = 500 holes
  ```
- **Key Insights**:
  - Different processes optimal for different volumes
  - Bottlenecks shift with product mix
  - Setup reduction critical for flexibility
- **Frameworks Applied**: Process selection matrix, Bottleneck analysis, Setup time reduction

#### 🥤 National Cranberry Cooperative - Seasonal Processing
*[Case Notes](case%20notes/9-688-122%20National%20Cranberry%20Cooperative.md)*

**Focus**: Capacity planning with seasonal demand and quality variation
- **Operational Challenges**:
  - Truck waiting times during peak
  - Wet vs dry berry processing
  - Quality variability (% wet berries)
  - Seasonal capacity planning
- **Capacity Analysis**:
  - Receiving: 5 dumpers × 75 bbls/hr = 375 bbls/hr
  - Drying: 3 dryers × 200 bbls/hr = 600 bbls/hr
  - Separating: 3 lines × 400 bbls/hr = 1,200 bbls/hr
  - **Bottleneck**: Receiving during peak hours
- **Solution Options**:
  1. Add dumpers ($75K each)
  2. Convert dry bins to wet ($10K each)
  3. Install light grading system
  4. Truck scheduling system
- **Key Takeaway**: Bottleneck location depends on product mix (wet/dry ratio)

### Service Operations

#### 🍔 Benihana of Tokyo - Restaurant Operations
*[To be added when case is covered]*

**Focus**: Service capacity and customer experience design
- Teppanyaki format efficiency
- Table utilization optimization
- Batching and customer flow
- Experience standardization

### Supply Chain Management

#### 🍺 Beer Game Simulation
*[Exercise on November 13]*

**Focus**: Bullwhip effect and supply chain coordination
- Information delays
- Order batching
- Price fluctuations
- Shortage gaming

---

## 🔧 Continuous Improvement Methodologies

### 1. Lean Manufacturing / Toyota Production System

#### Seven Wastes (TIMWOOD)
1. **T**ransportation: Unnecessary movement
2. **I**nventory: Excess stock
3. **M**otion: Unnecessary worker movement
4. **W**aiting: Idle time
5. **O**verproduction: Making too much/too early
6. **O**verprocessing: Unnecessary steps
7. **D**efects: Rework and scrap

#### Lean Tools
| Tool | Purpose | Application |
|------|---------|-------------|
| **5S** | Workplace organization | Sort, Set, Shine, Standardize, Sustain |
| **Kanban** | Pull system | Visual signals for production |
| **Kaizen** | Continuous improvement | Small, incremental changes |
| **Value Stream Mapping** | Process visualization | Identify waste in flow |
| **Poka-Yoke** | Error proofing | Prevent defects |
| **SMED** | Setup reduction | Single Minute Exchange of Dies |

### 2. Six Sigma

#### DMAIC Process
1. **Define**: Problem and goals
2. **Measure**: Current performance
3. **Analyze**: Root causes
4. **Improve**: Implement solutions
5. **Control**: Sustain improvements

#### Process Capability
```
Cp = (USL - LSL)/(6σ)
Cpk = min[(USL - μ)/(3σ), (μ - LSL)/(3σ)]

Six Sigma = 3.4 defects per million (Cpk ≥ 2.0)
```

### 3. Digital Operations & Industry 4.0

#### Key Technologies
- **IoT Sensors**: Real-time monitoring
- **Predictive Analytics**: Anticipate failures
- **Digital Twins**: Virtual process models
- **RPA**: Robotic process automation
- **AI/ML**: Optimization algorithms

---

## 📈 Problem Set Templates

### Process Analysis Problem
```
Given:
- Process steps and times
- Resource availability
- Demand rate

Find:
1. Bottleneck location
2. System capacity
3. Utilization of each resource
4. Flow time
5. WIP (using Little's Law)

Solution Approach:
1. Map the process
2. Calculate capacity of each step
3. Identify minimum (bottleneck)
4. Calculate metrics
```

### Queueing Problem
```
Given:
- Arrival rate (λ)
- Service rate (μ)
- Number of servers (c)

Find:
1. Utilization (ρ)
2. Average queue length (Lq)
3. Average wait time (Wq)
4. Probability of waiting

Solution Approach:
1. Verify stability (ρ < 1)
2. Apply appropriate formula (M/M/1 or M/M/c)
3. Calculate metrics
```

### Inventory Problem
```
Given:
- Annual demand (D)
- Ordering cost (S)
- Holding cost (H)
- Lead time (L)
- Service level

Find:
1. EOQ
2. Reorder point
3. Safety stock
4. Total cost

Solution Approach:
1. Calculate EOQ
2. Determine safety stock for service level
3. Set reorder point = Lead time demand + Safety stock
4. Calculate total cost
```

---

## 📝 Template for New Case Analysis

```markdown
#### 🏭 [Case Name] - [Operations Focus]
*[Case Notes](case%20notes/filename.md)*

**Focus**: [Primary operational challenge]
- **Operational Issues**:
  - [Issue 1]
  - [Issue 2]
  - [Issue 3]
- **Process Characteristics**:
  - Type: [Job shop/Batch/Line/Continuous]
  - Volume: [High/Medium/Low]
  - Variety: [High/Medium/Low]
- **Capacity Analysis**:
  - Bottleneck: [Location]
  - Utilization: [%]
  - Throughput: [Units/time]
- **Key Calculations**:
  ```
  [Show main calculations]
  ```
- **Improvement Options**:
  1. [Option 1]: $[Cost], [Impact]
  2. [Option 2]: $[Cost], [Impact]
- **Recommendation**: [Your solution]
- **Key Takeaway**: [Main learning]
```

---

## 🎓 Exam Preparation Checklist

### Conceptual Understanding
- [ ] Can you identify process types and characteristics?
- [ ] Do you understand Little's Law applications?
- [ ] Can you explain bottleneck theory?
- [ ] Do you know lean principles and tools?
- [ ] Can you describe bullwhip effect causes?

### Analytical Skills
- [ ] Can you calculate process capacity?
- [ ] Can you identify bottlenecks?
- [ ] Can you apply queueing formulas?
- [ ] Can you solve EOQ problems?
- [ ] Can you analyze process flow diagrams?

### Problem Solving
- [ ] Can you map a process from description?
- [ ] Can you recommend process improvements?
- [ ] Can you evaluate capacity expansion options?
- [ ] Can you analyze trade-offs (efficiency vs flexibility)?
- [ ] Can you optimize inventory levels?

---

## 📌 Quick Reference

### Essential Formulas
```
Little's Law: WIP = R × T
Utilization: U = Demand/Capacity
EOQ: √(2DS/H)
Safety Stock: z × σ × √L
OEE: Availability × Performance × Quality
Takt Time: Available Time / Customer Demand
```

### Common Bottleneck Solutions
| Problem | Solutions |
|---------|-----------|
| Long setup times | SMED, Batching, Dedicated lines |
| High variability | Standardization, Training, Maintenance |
| Low utilization | Demand management, Flexibility |
| Quality issues | Poka-yoke, SPC, Training |
| Waiting/Queues | Capacity addition, Scheduling |

### Process Improvement Checklist
1. **Eliminate** non-value-added activities
2. **Combine** related operations
3. **Rearrange** for better flow
4. **Simplify** necessary operations
5. **Automate** where beneficial
6. **Standardize** to reduce variation

---

## 🔄 Maintenance Instructions

### After Each Class
1. Add new case using template
2. Update relevant frameworks
3. Include key calculations
4. Note exam-relevant topics
5. Add to problem set examples

### Weekly Practice
1. Solve one process analysis problem
2. Practice bottleneck identification
3. Review queueing formulas
4. Work through problem sets

### Before Exams
1. Review all formulas
2. Practice process mapping
3. Solve sample problems
4. Review case calculations
5. Check problem set solutions

---

*Remember: Operations excellence comes from seeing processes systematically, identifying constraints, and relentlessly pursuing improvement.*