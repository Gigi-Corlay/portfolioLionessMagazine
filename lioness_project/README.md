# LIONESS – The Magazine for Queens

LIONESS is a bilingual (French/English) digital platform designed to promote, celebrate, and empower African and Afro-descendant women through inspiring content, entrepreneurship, community engagement, and digital publications.

The platform provides comprehensive access to the LIONESS digital magazine, member registration, and a secure personalized dashboard.

---

## 📖 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [MVP Scope](#-mvp-scope)
- [Technologies Used](#-technologies-used)
- [Application Architecture](#-application-architecture)
- [Database Design & ERD](#-database-design--erd)
- [Project Structure](#-project-structure)
- [Installation Guide](#-installation-guide)
- [Environment Configuration](#-environment-configuration)
- [Production & Deployment (Render & Cloudinary)](#-production--deployment-render--cloudinary)
- [Running the Project](#-running-the-project)
- [Authentication System](#-authentication-system)
- [Internationalization (i18n)](#-internationalization-i18n)
- [Security Measures](#-security-measures)
- [Testing Strategy](#-testing-strategy)
- [Git Workflow](#-git-workflow)
- [Technical Decisions](#-technical-decisions)
- [Team Collaboration](#-team-collaboration)
- [License](#-license)

---

## 🏗️ Application Architecture

```mermaid
flowchart TD
    U[User]
    FE[Front-end HTML / CSS / JavaScript]
    LANG[Language Selection FR / EN]
    BE[Back-end Django Python]
    DB[(Database PostgreSQL Render)]
    CLOUDINARY[(Cloudinary Media Storage)]
    CAL[Calaméo PDF Magazines]
    EMAIL[Email Service Notifications]
    DF[Data Flow Layer HTTP Requests + JSON Responses]

    U --> FE
    FE --> LANG
    LANG --> FE
    FE --> DF
    DF --> BE
    BE -->|CRUD Users & Articles| DB
    DB --> BE
    BE -->|Upload & Stream Images| CLOUDINARY
    CLOUDINARY --> FE
    BE --> FE
    BE --> CAL
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
    class CLOUDINARY databaseNode
    class CAL externalNode
    class EMAIL externalNode
    class DF dataflowNode
    class LANG languageNode
```

## Database Design & ERD
```mermaid
erDiagram
    USER ||--o{ PROFILE : has
    USER ||--o{ NOTIFICATION : receives
    
    USER {
        int id PK
        string username
        string email
        string password
        string first_name
        string last_name
        boolean is_active
        datetime date_joined
    }

    PROFILE {
        int id PK
        int user_id FK
        string country
        string occupation
        string profile_picture_url
        text bio
        datetime created_at
        datetime updated_at
    }

    ARTICLE {
        int id PK
        string title
        string author
        text content
        string image_url
        string category
        boolean published
        datetime created_at
    }
```
    ----

## 🔄 System Workflows & Sequence Diagrams
### 1. Sequence Diagram — User Login

```mermaid
sequenceDiagram
    actor User
    participant Frontend
    participant Backend
    participant Database
    participant SessionManager

    User->>Frontend: Open login page
    Frontend-->>User: Display login form
    User->>Frontend: Enter email and password
    Frontend->>Backend: POST /login request
    Backend->>Database: Verify user credentials
    Database-->>Backend: Validation result

    alt Valid credentials
        Backend->>SessionManager: Generate authentication session
        SessionManager-->>Backend: Session token created
        Backend-->>Frontend: Login success
        Frontend-->>User: Redirect to member dashboard
    else Invalid credentials
        Backend-->>Frontend: Authentication error message
        Frontend-->>User: Display login error
    end
```

```mermaid
erDiagram

    USER {
        int id PK
        string username
        string email
        string password
        string profile_image
        boolean is_active
        datetime created_at
    }

    MAGAZINE_ISSUE {
        int id PK
        string title
        string cover_image
        string pdf_url
        string language
        date published_date
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

    %% Future Version 2
    DONATION_V2 {
        int id PK
        int donation_id FK
        string payment_method
        string transaction_id
        string currency
        string provider
        datetime paid_at
    }


    %% Future Version 2
    NOTIFICATION_V2 {
        int id PK
        int notification_id FK
        string title
        string type
        string action_url
        datetime read_at
    }

    USER ||--o{ ARTICLE : writes
    MAGAZINE_ISSUE ||--o{ ARTICLE : contains
    USER ||--o{ DONATION : makes
    USER ||--o{ NOTIFICATION : receives

    DONATION ||--o| DONATION_V2 : extends
    NOTIFICATION ||--o| NOTIFICATION_V2 : extends
---

### 2. Sequence Diagram — Retrieve Articles by Category
```mermaid
    sequenceDiagram
    actor User
    participant Frontend
    participant Backend
    participant Database
    participant Cloudinary

    User->>Frontend: Click on Category Tab (e.g., News)
    Frontend->>Backend: GET /blog/category/news/
    Backend->>Database: Filter Articles (category='news', published=True)
    Database-->>Backend: Return Article Metadata & Image URLs
    Backend-->>Frontend: Render category_articles.html with Context
    Frontend->>Cloudinary: Fetch hosted images asset directly
    Cloudinary-->>Frontend: Stream images fluidly
    Frontend-->>User: Display categorized items grid
```

---

## 🎯 Project Overview
### LIONESS was built to structure a complete digital ecosystem where members can:
- Browse an editorial catalog of inspiring publications and opinion pieces.

- Discover successful women entrepreneurs through targeted showcases.

- Join an empowered community through a secure, authenticated members-only space.

The project adheres to Agile development methodologies and is delivered as a fully functioning MVP built on top of the Django framework.

---

## 🚀 Features
### Public & Core Editorial Features
- **Dynamic Magazine Engine:** Features a structured article publication system automatically sorting content into 9 official thematic categories mapped from the original design mockups: *News, Mood, Agenda Business, Guest Focus, Cover, Well-being, What if we talked about it ?, Lifestyle, The Most Impactful Personalities*.

- **Contextual Filtering:** Users seamlessly navigate editorial channels via specialized controllers (```views.articles_by_category```), displaying dynamic publication feeds.

- **Calaméo Integration:** Smooth embedding of professional, interactive PDF magazine players directly inside the responsive user interface.

---

### Authentication & Member Space

* **Registration & Extended Profiles**: Standard account registration handled as atomic transactions, automatically coupled with an extended `Profile` model that hooks into important context data (*Country of Residence*, *Occupation*, *Biography*).

* **Secure Dashboard Layout**: Tailored member panel (```dashboard.html```) equipped with a persistent multi-tiered sidebar drawer, fluid accessibility toggles for mobile viewpoints (```#sidebarToggle```), and automated dynamic state handlers to apply active link styles visual feedback.  

---

## 🏆 MVP Scope

### Must Have (Fully functional & implemented)
* Global Homepage and descriptive About section.
* End-to-end Authentication System (Registration, Secure Login, Logout) featuring Django's native cryptographic password hashing.
* Personalized Espace Member UI (`dashboard.html`) managing navigation drawer persistence states and feeding latest items.  
* Comprehensive Publication System (`models.py`, `views.py`, `admin.py`) built directly under the `blog_magazine` module.  
* Transparent Bilingual execution pipeline (FR / EN) driven by locale middleware.  

### Should Have
* Live profile context updating capabilities (`profile_view`) within the workspace dashboard using multi-part forms (`request.FILES`).
* Registration confirmation receipts processed via transactional email or local logging channels.

### Could Have / Future Steps
* Direct user submission portal enabling members to draft and propose draft posts for administrative approval.

* Integrated donation workflow via secure external platform gateway (e.g., HelloAsso setup).

* Centralized podcast player layout structures.

---

## 🛠 Technologies Used

* **Backend**: Python 3.1O+ | Django 4.2+ (Template Processing Engine, Object-Relational Mapper, Native Authentication Suite).  

- **Textual Databases**: PostgreSQL (Production text & relational storage managed on Render) | SQLite3 (Optional local file-based testing layer).

- **Media Cloud Storage**: Cloudinary (Production asset storage serving images, avatars, and visual media banners seamlessly).

- **Hosting & DevOps**: Render Platform (WSGI Server Management via Gunicorn/WhiteNoise).

- **Frontend**: HTML5 | CSS3 (Native custom properties `:root` declaration tracking a strict typography and palette design system) | Bootstrap 5 | JavaScript (ES6 targeting layout drawers and credential visibility interactions).

- **i18n Layer**: Django `LocaleMiddleware` combined with granular block compilation tags (`{% blocktrans %}`) and structural `gettext_lazy` markers. 

---

## 🗄 Database Design

The application utilizes Django's built-in object-relational mapping to manage system configurations and structural content:  

### `Article` Model Schema (`blog_magazine`)

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer (PK) | Unique primary key identifying the database record. |
| `title` | CharField(255) | The headline or title of the publication. |
| `author` | CharField(150) | Optional author credit or pen name. |
| `content` | TextField | Main body layout supporting clean carriage returns using `pre-line` filters. |
| `image` | CloudinaryField | Image attachment reference routed and securely hosted directly inside Cloudinary. |
| `category` | CharField(50) | String token field mapped tightly to the 9 default choices (Default: `'news'`). |
| `published` | BooleanField | Public visibility control flag (Default: `True`). |
| `created_at` | DateTimeField | Automatic registration tracking timestamp (`auto_now_add`). |

### `Profile` Model Schema (`accounts`)

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer (PK) | Unique primary identification token. |
| `user` | OneToOneField | Strict 1:1 relational map binding direct record context to Django's native `User` entity. |
| `country` | CharField(100) | Location data captured during member signup flows. |
| `occupation` | CharField(100) | Member professional specialization field. |
| `profile_picture` | CloudinaryField | Avatar profile portrait file hosted dynamically in Cloudinary buckets. |
| `bio` | TextField | Plain-text descriptive user profile background summary. |

---

## 📂 Project Structure

```plaintext
portfolioLionessMagazine/
│
├── accounts/               # Account workflows and extended user attributes
│   ├── forms.py            # Overrides (RegisterForm, LoginForm, ProfileForm)
│   ├── models.py           # Profile model structural extension definition
│   ├── signals.py          # Auto-instantiation bindings leveraging user post_save hooks
│   ├── views.py            # Authentication handlers and workspace profile mutation logic
│   └── urls.py
│
├── blog_magazine/          # Editorial core publishing engine
│   ├── admin.py            # Panel overrides managing list layouts, search indexes, and active filters
│   ├── models.py           # Article database models and the official CATEGORY_CHOICES arrays
│   ├── urls.py             # Route definitions tracking slugs and numerical primary IDs
│   └── views.py            # Controller views (articles_by_category and article_detail)
│
├── dashboard/              # Authenticated workspace processing layers
│   ├── views.py            # Landing workspace index feeding recent active magazine updates
│   └── urls.py
│
├── lioness_project/        # Root Django deployment and orchestration settings
│   ├── settings.py         # Global parameters detailing i18n middleware and Cloudinary storage backend
│   └── urls.py             # Root collection mapping system-wide endpoints and i18n_patterns
│
├── templates/              # Visual view layout repository
│   ├── base.html           # Main master boilerplate layout framework
│   ├── accounts/           # Presentation layer templates login.html and register.html
│   ├── dashboard/
│   │   └── dashboard.html  # Global master interface wrapper framework for signed-in members
│   └── blog_magazine/
│       ├── category_articles.html # Group view list rendered according to active categories
│       └── article_detail.html    # Standalone dynamic reading window showcasing selected articles
│
├── static/
│   ├── css/
│   │   ├── auth.css        # Focused layout styles managing standard authentication screens
│   │   └── dashboard.css   # Global application theme declarations tracking core CSS variables
│   └── js/
│
├── .gitignore              # Project exclusion rules (venv, db.sqlite3)
├── requirements.txt        # Frozen dependencies manifest (including cloudinary & dj-database-url)
└── db.sqlite3
```
## ⚙️ Installation Guide
```bash
g# Clone the repository
git clone [https://github.com/Gigi-Corlay/portfolioLionessMagazine.git](https://github.com/Gigi-Corlay/portfolioLionessMagazine.git)
cd portfolioLionessMagazine

# Instantiate virtual environment
python -m venv venv

# Linux / Mac activation
source venv/bin/activate

# Windows activation
venv\Scripts\activate

# Dependency deployment
pip install -r requirements.txt
```
---

## 🔧 Environment Configuration

Create a `.env` configuration file at the root of your project:

```env
DEBUG=True
SECRET_KEY=your_secure_django_cryptographic_key_goes_here
ALLOWED_HOSTS=127.0.0.1,localhost

# Database Connection (Render PostgreSQL in prod, falls back to SQLite locally)
DATABASE_URL=postgres://user:password@host:port/dbname

# Cloudinary Integration API Keys
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

```
---

## 🚀 Production & Deployment (Render & Cloudinary)

The platform is deployed live on **Render** using a two-tier backend separation for robust modern state management:

- **Textual/Relational Data:** Managed via a secure PostgreSQL instance on Render.

- **Media/Static Files Data:** Uploaded and served globally via a Cloudinary CDN storage bucket.

## Build and Deployment Settings on Render

- **Environment:** `Python 3`

- **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`

- **Start Command:** `gunicorn lioness_project.wsgi:application`

Production Environment Variables Panel

- `DEBUG: False`

- `SECRET_KEY: [Encrypted Token Key]`

- `DATABASE_URL: [Render PostgreSQL External Connection String]`

- `CLOUDINARY_CLOUD_NAME: [Cloudinary Cloud Identity]`

- `CLOUDINARY_API_KEY: [Cloudinary Credential Key]`

- `CLOUDINARY_API_SECRET: [Cloudinary Private Access Secret]`

- `ALLOWED_HOSTS: https://portfoliolionessmagazine.onrender.com`

---

## ▶️ Running the Project
```bash
# Apply migrations to prepare database schemas (User, Profile, Article)
python manage.py migrate

# Create an administrative user
python manage.py createsuperuser

# Start the local development server
python manage.py runserver
```

**Open:**
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/

---

## 🌍 Internationalization (i18n)

- LocaleMiddleware enabled
- Language switching FR/EN
- ```{% trans %}``` and ```{% blocktrans %}``` used

---

## 🛡️ Security Measures

- **CSRF Protection**

  - All forms include:
  ```django
  {% csrf_token %}
  ```

- **Secure ORM usage**

  - No raw SQL queries
  - Uses Django ORM:
  ```python
    Article.objects.filter(...)
  ```

- **XSS protection**
 - Django auto-escapes template variables:
```django
  {{ article.content }}
```
- CSS ```white-space: pre-line``` preserves formatting safely

- **Access control**
  - Protected views use:
  ```python
  @login_required
  ```
  - Unauthorized users are redirected automatically

---

##  🧪 Testing Strategy

To maintain continuous stability and system health, unit tests are bundled within the modules ensuring authorization contexts and publishing dataflows execute successfully.

```bash

# Run test suite
python manage.py test

# Measure test statement coverage
coverage run --source='.' manage.py test
coverage report -m
```
---

## 🐙 Git Workflow

The engineering lifecycle relies on a clean, scalable Git strategy:

- `main / master`: Represents the stable, production-ready release pipeline automatically monitored and deployed by Render hooks.

 Feature Branches: Isolated iterations are constructed using specific branch namings (`feature/accounts-auth`, `feature/cloudinary-media`) to isolate development cycles before peer integration review.

---

## 📚 Technical Decisions
**1. Inline Magazine Classification Architecture**

Categories are managed using a fixed ```CATEGORY_CHOICES``` structure inside the model layer instead of a separate relational table.

### ✔ Benefits:
- Simpler database schema (MVP-friendly)
- Easier admin control via ```list_filter```
- Faster development iteration

---

**2. Signal-Driven User Lifecycle (```signals.py```)**
User profiles are automatically created using Django signals:
- Trigger: ```post_save``` on ```User```
- Automatically creates related ```Profile```

### ✔ Benefits:
- Prevents ```DoesNotExist``` errors
- Ensures profile consistency at creation time
- Improves UX in dashboard access

---

**3. Template Inheritance Strategy**
All dashboard-related pages inherit from:
```
dashboard/dashboard.html
```
**Pages like:**
- category_articles.html
- article_detail.html

Override blocks such as:
``` django
{% block nav_articles %}active{% endblock %}
```
### ✔ Benefits:
- Avoids code duplication
- Centralizes layout logic
- Simplifies UI maintenance

---

## 📄 License

This platform was developed as part of an academic portfolio.

*All rights reserved © LIONESS*

---

## Auteur
Georgia BOULNOIS
