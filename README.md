# Portfolio Lioness Magazine

## System Architecture

```mermaid
flowchart TD

U[User]

FE[Front-end HTML / CSS / JavaScript]
LANG[Language Selection FR / EN]

BE[Back-end Django Python]
DB[(Database SQLite / PostgreSQL)]

CAL[Calaméo PDF Magazines]
HELLOASSO[HelloAsso Donation Platform]
EMAIL[Email Service Notifications]

DF[Data Flow Layer HTTP Requests + JSON Responses]

U --> FE

FE --> LANG
LANG --> FE

FE --> DF
DF --> BE

BE -->|CRUD Users & Articles| DB
DB --> BE

BE --> FE

BE --> CAL
BE --> HELLOASSO
BE --> EMAIL

classDef userNode stroke:#fb7185,fill:#fff1f2
classDef frontendNode stroke:#38bdf8,fill:#f0f9ff
classDef backendNode stroke:#a78bfa,fill:#f5f3ff
classDef databaseNode stroke:#4ade80,fill:#f0fdf4
classDef externalNode stroke:#facc15,fill:#fefce8
classDef dataflowNode stroke:#f97316,fill:#fff7ed
classDef languageNode stroke:#60a5fa,fill:#eff6ff

class U userNode
class FE frontendNode
class BE backendNode
class DB databaseNode
class CAL externalNode
class HELLOASSO externalNode
class EMAIL externalNode
class DF dataflowNode
class LANG languageNode
```


