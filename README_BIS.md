# LIONESS – The Magazine for Queens

LIONESS is a bilingual (French/English) digital platform designed to promote, celebrate, and empower African and Afro-descendant women through inspiring content, entrepreneurship, community engagement, and digital publications.

The platform provides access to the LIONESS digital magazine, member registration, a personalized dashboard, and support for the association through donations.

---

# 📖 Table of Contents

- Project Overview
- Features
- MVP Scope
- Technologies Used
- Application Architecture
- Database Design
- Project Structure
- Installation Guide
- Environment Configuration
- Running the Project
- Authentication System
- Internationalization (i18n)
- Security Measures
- Testing Strategy
- Git Workflow
- API Documentation
- Future Improvements
- Screenshots
- Team Collaboration
- Author

---

# 🎯 Project Overview

LIONESS was created to provide a digital ecosystem where women can:

- Read inspiring magazine content
- Discover successful women entrepreneurs
- Join a supportive community
- Access resources and opportunities
- Support the organization through donations

The project follows Agile development principles and was built as an MVP (Minimum Viable Product) using Django.

---

# 🚀 Features

## Public Features

### Homepage

- Presentation of the LIONESS project
- Community introduction
- Services showcase
- Magazine section
- Responsive navigation

### About Section

- Organization mission
- Community values
- Project objectives

### Magazine Access

- Digital magazines integration via Calaméo
- Responsive magazine cards
- Direct access to magazine issues

### Donations

- Donation support through HelloAsso
- External secure payment processing

---

## Authentication Features

### User Registration

Users can:

- Create an account
- Provide personal information
- Set secure credentials

Stored information:

- First Name
- Last Name
- Email
- Country
- Occupation

### User Login

Members can:

- Authenticate securely
- Access protected pages
- View personalized content

### User Logout

Secure session termination.

---

## Dashboard

Authenticated users can:

- Access personalized content
- View account information
- Access magazine categories
- Track platform activity

---

# 🏆 MVP Scope

The MVP includes the following core features:

### Must Have

- Homepage
- About Page
- User Registration
- User Login
- User Logout
- User Dashboard
- Magazine Page
- Calaméo Integration
- Donation Page
- Responsive Design
- French / English Support

### Should Have

- Profile Management
- Welcome Email Notification
- Enhanced Dashboard

### Could Have

- Newsletter Subscription
- Article Submission Form
- Podcast Integration

### Won't Have (MVP)

- Mobile Application
- Premium Membership
- Internal Magazine Reader
- AI Features
- Community Comments

---

# 🛠 Technologies Used

## Backend

- Python 3.12+
- Django 4.2

## Database

- SQLite3

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

## Authentication

- Django Authentication System

## External Services

### Calaméo

Used to host and display digital magazines.

### HelloAsso

Used to process donations securely.

## Version Control

- Git
- GitHub

---

# 🏗 Application Architecture

```text
┌──────────────────────┐
│      Browser         │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Django Views         │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Business Logic       │
│ (Apps)               │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ SQLite Database      │
└──────────────────────┘
```

---

# 🗄 Database Design

## User

Django built-in User model

| Field | Type |
|---------|---------|
| id | Integer |
| username | String |
| email | String |
| password | Hashed |
| first_name | String |
| last_name | String |

---

## Profile

| Field | Type |
|---------|---------|
| id | Integer |
| user | OneToOne |
| country | String |
| occupation | String |

Relationship:

```text
User
 │
 │ One-To-One
 ▼
Profile
```

---

## Future Models

### Article

| Field | Type |
|---------|---------|
| title | String |
| content | Text |
| category | String |
| language | String |
| author | ForeignKey |
| created_at | DateTime |

### MagazineIssue

| Field | Type |
|---------|---------|
| title | String |
| cover_image | Image |
| calaméo_url | URL |
| publication_date | Date |

---

# 📂 Project Structure

```text
lioness/
│
├── accounts/
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── core/
│
├── dashboard/
│
├── magazine/
│
├── donations/
│
├── templates/
│   ├── accounts/
│   ├── dashboard/
│   └── home.html
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

# ⚙ Installation Guide

## Clone Repository

```bash
git clone https://github.com/yourusername/lioness.git

cd lioness
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔧 Environment Configuration

Create a `.env` file:

```env
DEBUG=True

SECRET_KEY=your-secret-key

ALLOWED_HOSTS=127.0.0.1,localhost
```

---

# ▶ Running the Project

Apply migrations:

```bash
python manage.py migrate
```

Create superuser:

```bash
python manage.py createsuperuser
```

Run server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

# 🔐 Authentication System

LIONESS uses Django Authentication Framework.

Features:

- Registration
- Login
- Logout
- Session Management
- Password Hashing
- Form Validation

Password security is handled by Django's built-in hashing algorithms.

---

# 🌍 Internationalization (i18n)

Supported languages:

- French
- English

Configuration:

```python
LANGUAGE_CODE = "fr"

LANGUAGES = [
    ("fr", "French"),
    ("en", "English"),
]
```

Middleware:

```python
django.middleware.locale.LocaleMiddleware
```

---

# 🛡 Security Measures

Implemented security features:

- Password Hashing
- CSRF Protection
- Session Security
- Form Validation
- Authentication Decorators
- Django Security Middleware

Production recommendations:

- HTTPS
- Environment Variables
- PostgreSQL
- Secure Cookies

---

# 🧪 Testing Strategy

## Unit Tests

Test:

- User Registration
- Login
- Logout
- Profile Creation

Run:

```bash
python manage.py test
```

---

## Integration Tests

Validate:

- Dashboard Access
- Authentication Flow
- Database Interactions

---

## Manual Testing

Validated scenarios:

- Registration
- Login
- Logout
- Responsive Design
- Dashboard Navigation
- Magazine Access
- Donation Access

---

# 🔄 Git Workflow

Branching Strategy:

```text
main
│
develop
│
├── feature/authentication
├── feature/dashboard
├── feature/magazine
├── feature/donations
```

Workflow:

1. Create feature branch
2. Develop feature
3. Commit changes
4. Open Pull Request
5. Code Review
6. Merge into develop
7. Release to main

---

# 📝 Commit Convention

Examples:

```bash
feat: add user authentication system

feat: create dashboard page

fix: responsive navbar issue

refactor: improve registration form

docs: update README
```

---

# 📡 API Documentation (Planned)

## Authentication

### Register

```http
POST /api/register
```

### Login

```http
POST /api/login
```

---

## Magazine

```http
GET /api/magazines
```

---

## Donations

```http
GET /api/donations
```

Response:

```json
{
  "platform": "HelloAsso",
  "donation_url": "https://helloasso.com/example"
}
```

---

# 🚀 Future Improvements

Version 2:

- Newsletter
- User Profiles
- Notifications
- Enhanced Dashboard
- Article Submission

Version 3:

- Mobile Application
- Community Features
- Internal Reader
- Premium Membership
- AI Recommendations

---

# 📸 Screenshots

## Homepage

Insert screenshot here:

```text
docs/screenshots/homepage.png
```

---

## Registration

Insert screenshot here:

```text
docs/screenshots/register.png
```

---

## Dashboard

Insert screenshot here:

```text
docs/screenshots/dashboard.png
```

---

# 👥 Team Collaboration

Project developed following Agile methodology.

Activities:

- Sprint Planning
- Daily Stand-Ups
- Sprint Reviews
- Sprint Retrospectives
- Code Reviews
- QA Testing

Project Management Tools:

- GitHub Projects
- Trello
- GitHub Issues

---

# 📚 Technical Decisions

## Why Django?

- Built-in Authentication
- Strong Security
- Fast Development
- Admin Interface
- Scalability

## Why SQLite?

- Lightweight
- Easy Setup
- Perfect for MVP Development

Future production migration:

```text
SQLite → PostgreSQL
```

## Why Calaméo?

- Professional digital magazine reader
- Responsive
- Easy integration

## Why HelloAsso?

- Secure payments
- Trusted by associations
- Easy donation workflow

---

# 👨‍💻 Author

**LIONESS Project**

Portfolio Project

Developed with:

- Django
- HTML
- CSS
- Bootstrap
- JavaScript

---

# 📄 License

This project was created for educational and portfolio purposes.

All rights reserved © LIONESS.