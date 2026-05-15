# portfolioLionessMagazine
Projet pour mon portfolio Holberton school

flowchart TD

U[Utilisateur]

FE[Front-end\nHTML / CSS / JavaScript]

BE[Back-end\nDjango (Python)]

DB[(Base de données\nSQLite / PostgreSQL)]

CAL[Calaméo\nMagazines PDF]

STRIPE[Stripe\nPaiement dons]

EMAIL[Service Email\nNotifications]

U --> FE
FE -->|HTTP Requests| BE

BE -->|CRUD Users & Articles| DB
DB --> BE
BE --> FE

BE --> CAL
BE --> STRIPE
BE --> EMAIL
