# Mermaid Diagram Templates

Copy any template below and modify for your needs!

## 1. Basic Decision Flow Template

```mermaid
flowchart TD
    Start([Start]) --> Input[/Input Data/]
    Input --> Process[Process]
    Process --> Decision{Condition?}
    Decision -->|True| ActionA[Action A]
    Decision -->|False| ActionB[Action B]
    ActionA --> Result[(Store Result)]
    ActionB --> Result
    Result --> End([End])
```

## 2. Error Handling Template

```mermaid
flowchart LR
    Try[Try Operation] --> Catch{Error?}
    Catch -->|No Error| Success[Success]
    Catch -->|Error Type 1| Handle1[Handle Type 1]
    Catch -->|Error Type 2| Handle2[Handle Type 2]
    Catch -->|Unknown| LogError[Log & Alert]
    Handle1 --> Retry{Retry?}
    Retry -->|Yes| Try
    Retry -->|No| Fail[Operation Failed]
```

## 3. API Sequence Template

```mermaid
sequenceDiagram
    participant C as Client
    participant A as API
    participant D as Database
    participant E as External Service
    
    C->>A: Request
    A->>A: Validate
    A->>D: Query
    D-->>A: Results
    A->>E: External Call
    E-->>A: Response
    A-->>C: Final Response
```

## 4. State Machine Template

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing: Start
    Processing --> Success: Complete
    Processing --> Error: Fail
    Error --> Processing: Retry
    Error --> Failed: Max Retries
    Success --> [*]
    Failed --> [*]
```

## 5. Gantt Chart Template

```mermaid
gantt
    title Project Timeline
    dateFormat YYYY-MM-DD
    section Phase 1
    Task 1          :a1, 2024-01-01, 30d
    Task 2          :after a1, 20d
    section Phase 2
    Task 3          :2024-02-01, 12d
    Task 4          :24d
```

## 6. Mind Map Template

```mermaid
mindmap
  root((Main Topic))
    Branch 1
      Sub 1.1
      Sub 1.2
        Detail A
        Detail B
    Branch 2
      Sub 2.1
      Sub 2.2
    Branch 3
      Sub 3.1
        Detail C
      Sub 3.2
    Branch 4
```

## 7. Entity Relationship Template

```mermaid
erDiagram
    USER ||--o{ ORDER : places
    USER {
        int id PK
        string email
        string name
        datetime created_at
    }
    ORDER ||--|{ ORDER_ITEM : contains
    ORDER {
        int id PK
        int user_id FK
        datetime order_date
        string status
    }
    ORDER_ITEM {
        int id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal price
    }
    PRODUCT ||--o{ ORDER_ITEM : "ordered in"
    PRODUCT {
        int id PK
        string name
        decimal price
        int stock
    }
```

## 8. Git Flow Template

```mermaid
gitGraph
    commit
    branch develop
    checkout develop
    commit
    branch feature/new-feature
    checkout feature/new-feature
    commit
    commit
    checkout develop
    merge feature/new-feature
    checkout main
    merge develop tag: "v1.0.0"
```

## 9. Pie Chart Template

```mermaid
pie title Tech Stack Distribution
    "JavaScript" : 45
    "Python" : 30
    "Go" : 15
    "Rust" : 10
```

## 10. Class Diagram Template

```mermaid
classDiagram
    class Animal {
        +String name
        +int age
        +void eat()
        +void sleep()
    }
    class Dog {
        +String breed
        +void bark()
        +void wagTail()
    }
    class Cat {
        +String color
        +void meow()
        +void scratch()
    }
    Animal <|-- Dog
    Animal <|-- Cat
```

## Tips- Change `TD` to `LR` for Horizontal Flow

- Add emojis for visual appeal: 🚀 ✅ ❌ ⚠️ 
- Use subgraphs to group related nodes
- Color nodes with `style` or `class` definitions