# Donner Company Process Flow - Horizontal (Left-Right) Flow

```mermaid
flowchart LR
    Start([Customer Order Received]) --> PreProd

    subgraph PreProd[Pre-Production]
        A1[Receive customer order with artwork]
        A2[Write material specifications]
        A3[Send order to purchasing agent]
        A4[Enter order into production log]
        A5[Send blueprint to supervisor]
        A6[Wait for materials to arrive]
        A7[Schedule production]
        
        A1 --> A2
        A2 --> A3
        A3 --> A4
        A4 --> A5
        A5 --> A6
        A6 --> A7
    end

    PreProd --> Prep

    subgraph Prep[Preparation Stage]
        B1[Digitize hole locations and sizes]
        B2[Inspect laminate for visual defects]
        B3[Shear sheets into panels]
        B4[Punch location holes]
        
        B1 --> B2
        B2 --> B3
        B3 --> B4
    end

    Prep --> ImageTrans

    subgraph ImageTrans[Image Transfer Stage]
        C1[Pin panel to drill table]
        C2{Drilling Decision:<br/>Order Size?}
        C3A[Manual Drilling<br/>7 stations]
        C3B[CNC Drilling<br/>1 machine]
        C4[Process through copper bath]
        C5[Wash scrub coat with DFPR]
        C6[Lay artwork on panels]
        C7[Expose to UV light]
        C8[Develop panels]
        C9[Electroplate copper conductors]
        C10[Strip DFPR chemically]
        C11[Etch copper off base]
        C12[Strip tin leaving copper]
        
        WIP1[/WIP Storage/]
        WIP2[/WIP Storage/]
        
        C1 --> C2
        C2 -->|≤100 boards| C3A
        C2 -->|>100 boards| C3B
        C3A --> WIP1
        C3B --> WIP1
        WIP1 --> C4
        C4 --> C5
        C5 --> C6
        C6 --> C7
        C7 --> C8
        C8 --> C9
        C9 --> WIP2
        WIP2 --> C10
        C10 --> C11
        C11 --> C12
    end

    ImageTrans --> Fab

    subgraph Fab[Fabrication Stage]
        D1[Apply soldermask epoxy coating]
    end

    Fab --> End([Complete])

    style C2 fill:#ffe6cc
    style C3A fill:#e6f3ff
    style C3B fill:#e6f3ff
    style WIP1 fill:#ffcccc
    style WIP2 fill:#ffcccc
```

## Why Horizontal Flow Works Best

**Advantages:**
- Natural left-to-right reading pattern matches process progression
- Ideal for wide screens and presentations
- Shows time progression clearly
- Better for linear processes like Donner's production flow

## Key Process Insights

1. **Single Decision Point**: Only drilling has a resource choice (Manual vs CNC)
2. **Two Queue Points**: Natural WIP accumulation after drilling and electroplating
3. **Completely Serial**: No parallel paths except drilling resource choice
4. **16 Production Steps**: From digitizing through soldermask application

## Drilling Decision Analysis

### Breakeven Calculation
For drilling operation with ~500 holes per board:

**Manual Drilling (7 stations)**
- Setup: 15 minutes
- Run: 0.08 min/hole × 500 holes = 40 min/board
- Total for 100 boards: 15 + (40 × 100) = 4,015 minutes

**CNC Drilling (1 machine)**
- Setup: 240 minutes
- Run: 0.004 min/hole × 500 holes = 2 min/board
- Total for 100 boards: 240 + (2 × 100) = 440 minutes

**Breakeven Point**: ~6 boards
- Below 6 boards: Manual is faster
- Above 6 boards: CNC is faster
- At 100 boards: CNC is 9x faster!

---
*Source: Operations at the Donner Company (602-040)*
*Last Updated: 2025-09-09*