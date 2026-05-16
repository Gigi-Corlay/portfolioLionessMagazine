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

## ER DIAGRAM
```mermaid
erDiagram

USER ||--o{ ARTICLE : writes
USER ||--o{ DONATION : makes
USER ||--o{ NOTIFICATION : receives
MAGAZINE_ISSUE ||--o{ ARTICLE : contains

USER {
  int id PK
  string username
  string email
  string password
  string profile_image
  boolean is_active
  datetime created_at
}

ARTICLE {
  int id PK
  int user_id FK
  int issue_id FK
  string title
  text content
  string image
  string language
  string status
  string category
  datetime created_at
  datetime updated_at
}

MAGAZINE_ISSUE {
  int id PK
  string title
  string cover_image
  string pdf_url
  string language
  date published_date
}

DONATION {
  int id PK
  int user_id FK
  float amount
  string donor_name
  string payment_status
  datetime created_at
}

NOTIFICATION {
  int id PK
  int user_id FK
  string message
  boolean is_read
  datetime created_at
}
```
## 1.SEQUENCE DIAGRAM — USER LOGIN
```mermaid
sequenceDiagram

actor User

participant Frontend
participant Backend
participant Database
participant SessionManager

User->>Frontend: Open login page

Frontend-->>User: Display login form

User->>Frontend: Enter email & password

Frontend->>Backend: POST /login request

Backend->>Database: Verify user credentials

Database-->>Backend: User data / validation result

alt Valid credentials

    Backend->>SessionManager: Generate authentication session/token

    SessionManager-->>Backend: Session token created

    Backend-->>Frontend: Login success + user session

    Frontend-->>User: Redirect to member dashboard

else Invalid credentials

    Backend-->>Frontend: Authentication error message

    Frontend-->>User: Display login error

end
```

## 2. SEQUENCE DIAGRAM — RETRIEVE ARTICLES
```mermaid
sequenceDiagram

actor User
participant Frontend
participant Backend
participant Database

User->>Frontend: Open Articles page

Frontend->>Backend: GET /articles request

Backend->>Database: Fetch articles
Database-->>Backend: Articles data

Backend-->>Frontend: JSON response
Frontend-->>User: Display articles list
```
## 3. SEQUENCE DIAGRAM — DONATION (HelloAsso)
```mermaid
sequenceDiagram

actor User
participant Frontend
participant Backend
participant HelloAsso
participant Database

User->>Frontend: Click "Support LIONESS"

Frontend->>Backend: Request donation page
Backend-->>Frontend: Return HelloAsso donation link

Frontend->>HelloAsso: Redirect user to donation platform

User->>HelloAsso: Complete donation payment

HelloAsso-->>Backend: Payment confirmation

Backend->>Database: Save donation information
Database-->>Backend: Confirmation saved

Backend-->>Frontend: Success response
Frontend-->>User: Donation success message
```

## 4. SEQUENCE DIAGRAM — ARTICLE SUBMISSION
```mermaid
sequenceDiagram

actor User
participant Frontend
participant Backend
participant Database
participant Editor

User->>Frontend: Write article submission

Frontend->>Backend: Submit article form

Backend->>Database: Save article (status: pending)

Database-->>Backend: Confirmation saved

Backend-->>Editor: Notify editorial team

Editor->>Backend: Review and approve article

Backend->>Database: Update article status

Backend-->>Frontend: Publish approved article

Frontend-->>User: Article submission confirmation
```

