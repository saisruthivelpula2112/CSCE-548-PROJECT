# CSCE 548 – Project 1

This project demonstrates a PostgreSQL-backed application using Python.
It includes database schema creation, seed data insertion, and Python-based
CRUD operations on a `users` table.

The project shows how to:
- Design a relational database schema
- Load initial data into PostgreSQL
- Connect Python to PostgreSQL
- List users from the database
- Add new users via a command-line interface

---

## Technologies Used

- PostgreSQL 17
- pgAdmin 4
- Python 3.13
- psycopg2-binary
- GitHub
- Visual Studio Code

---
## Repository Structure

```text
CSCE-548-PROJECT/
│
├── sql/
│   ├── schema.sql
│   └── seed.sql
│
├── src/
│   ├── __init__.py
│   ├── db.py
│   └── run_crud.py
│
├── .gitignore
└── README.md
```


---

## Setup Instructions

### 1. Install Required Software
Make sure the following are installed on your system:
- PostgreSQL 17
- pgAdmin 4
- Python 3.13
- Visual Studio Code

---

### 2. Create the Database
1. Open **pgAdmin**
2. Create a new database named:
---

## Setup Instructions

### 1. Install Required Software
Make sure the following are installed on your system:
- PostgreSQL 17
- pgAdmin 4
- Python 3.13
- Visual Studio Code

---

### 2. Create the Database
1. Open **pgAdmin**
2. Create a new database named:csce548_project1
---

---

### 3. Create Tables
1. Open `sql/schema.sql`
2. Run the script in **pgAdmin → Query Tool**
3. This creates all required tables:
- users
- projects
- items
- tags
- item_tags

---

### 4. Insert Seed Data
1. Open `sql/seed.sql`
2. Run the script in **pgAdmin → Query Tool**
3. This inserts initial users and related data

---

### 5. Install Python Dependency
From the project root directory:
```bash
pip install psycopg2-binary
-----
---

## How to Run

All commands must be executed from the **project root directory** (CSCE-548-PROJECT).

### List users
```bash
python -m src.run_crud --list
```

### Add a user
```bash
python -m src.run_crud --add alice alice@uni.edu student
```

---

## Screenshots

The following screenshots demonstrate the working of the project:

- PostgreSQL database and tables created in **pgAdmin**
- Successful execution of `schema.sql`
- Successful execution of `seed.sql`
- Output of `--list` command showing users
- Output of `--add` command adding a new user

Screenshots were taken during execution and are included for verification.

---

## GitHub Repository

Project source code is available at:  
https://github.com/saisruthivelpula2112/CSCE-548-PROJECT

---
---

# **CSCE 548 – Project 2**

Business Layer + Service Layer + Console Client Implementation  

---

# **GitHub Repository**

Project source code is available at:  

https://github.com/saisruthivelpula2112/CSCE-548-PROJECT  

---

# **Project Overview**

CSCE 548 – Project 2  
Business Layer + Service Layer + Console Client Implementation  

This project extends Project 1 by introducing a structured, layered architecture that separates responsibilities across:

- Data Layer (PostgreSQL interaction)  
- Business Layer (validation and business logic)  
- Service Layer (REST API using FastAPI)  
- Console Client (service tester)  

The goal of this project is to model a professional-grade service-oriented architecture in which business logic and service endpoints invoke the database layer without directly exposing database access to clients.

This project demonstrates:

- Clean separation of concerns  
- Abstraction of business rules  
- Microservice-style REST API design  
- End-to-end CRUD testing  

---

# **System Architecture**

Console Client  
        ↓  
Service Layer (FastAPI)  
        ↓  
Business Layer (Validation + Logic)  
        ↓  
Data Layer (PostgreSQL via psycopg2)  

Each layer communicates only with the layer directly below it.

---

# **Project Structure**

CSCE-548-PROJECT/  
│  
├── src/  
│   ├── __init__.py  
│   ├── db.py  
│   ├── business.py  
│   ├── service.py  
│   ├── models.py  
│   └── run_crud.py  
│  
├── sql/  
│   ├── schema.sql  
│   └── seed.sql  
│  
├── .env  
├── requirements.txt  
└── README.md  

---

# **Database Setup**

## Users Table Schema

CREATE TABLE users (  
    id SERIAL PRIMARY KEY,  
    username TEXT UNIQUE NOT NULL,  
    email TEXT NOT NULL,  
    role TEXT NOT NULL  
);  

---

## Environment Configuration (.env)

Create a `.env` file in the project root:

DB_HOST=localhost  
DB_PORT=5432  
DB_NAME=csce548_project1  
DB_USER=postgres  
DB_PASS=postgres  

Ensure PostgreSQL is running and the database exists.

---

# **How To Run The Project**

## Step 1 – Activate Virtual Environment

cd C:\Users\saisr\Documents\CSCE-548-PROJECT  
.\.venv\Scripts\Activate.ps1  

---

## Step 2 – Start the Service Layer

uvicorn src.service:app --reload --host 127.0.0.1 --port 9000  

If successful, you will see:

Uvicorn running on http://127.0.0.1:9000  

Open API documentation at:

http://127.0.0.1:9000/docs  

---

## Step 3 – Run Console Client

Open a new terminal:

cd C:\Users\saisr\Documents\CSCE-548-PROJECT  
.\.venv\Scripts\Activate.ps1  
python -m src.run_crud  

---

# **API Endpoints**

GET /users — Get all users  
GET /users/{username} — Get single user  
POST /users — Create user  
PUT /users?username=...&new_email=... — Update email  
DELETE /users?username=... — Delete user  
GET /health — Health check  

---

# **What The Console Client Tests**

The console client performs a complete CRUD cycle:

1. GET all users  
2. POST create user  
3. GET single user  
4. PUT update email  
5. GET updated user  
6. DELETE user  
7. GET all users again  

This confirms full end-to-end integration.

---

# **AI Prompt Used**

Prompt provided to ChatGPT:

Generate a business layer in Python that wraps CRUD operations from a PostgreSQL data layer. Then generate a FastAPI service layer that exposes all business methods. Also generate a console-based client to test full CRUD functionality.

---

# **Modifications Made to AI-Generated Code**

After generation, I manually:

- Fixed naming mismatches between layers  
- Standardized function names  
- Corrected relative import issues  
- Ensured service runs using uvicorn src.service:app  
- Adjusted database return values  
- Added input validation in the business layer  
- Improved HTTP error handling  

---

# **Testing Performed**

The system was verified by:

- Running uvicorn service  
- Executing console client  
- Observing HTTP status codes (200, 201, 404)  
- Confirming database updates  
- Validating deletion and update operations  

Screenshots demonstrate:

- Server startup  
- Client CRUD execution  
- Database updates  
- API responses  

---

# **Troubleshooting**

ImportError: attempted relative import with no known parent package  

Run:  
uvicorn src.service:app  

Do NOT run:  
python src/service.py  

---

Connection refused (WinError 10061)  

The server is not running. Start uvicorn first.

---

# **Hosting Notes**

To deploy to platforms such as Render or Heroku:

uvicorn src.service:app --host 0.0.0.0 --port $PORT  

Set environment variables in the hosting dashboard.

---

# **Project Summary**

This project demonstrates:

- Proper layered architecture  
- Business rule abstraction  
- RESTful API design  
- PostgreSQL integration  
- Clean separation of concerns  
- End-to-end CRUD testing  

All layers integrate successfully and function correctly.

---
# CSCE 548 — Project 3 & 4: Full-Stack N-Tier Web Application

**Author:** Velpula Sai Sruthi  
**Course:** CSCE 548 — Software Security  
**Semester:** Spring 2026  
**GitHub:** https://github.com/saisruthivelpula2112/CSCE-548-PROJECT

---

# Project 3 — Frontend Client

## Overview

Project 3 implements a browser-based frontend client that communicates with the RESTful API service layer built in Project 2. The client was designed to be user-friendly so that even non-technical users can easily understand and interact with the application — no raw JSON or database notation is ever shown to the user.

The frontend displays all data in structured tables with labeled columns, color-coded badges, and tab-based navigation across all five database tables.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, Vanilla JavaScript (fetch API) |
| Service Layer | FastAPI + Uvicorn (port 8080) |
| Business Layer | Python (business.py) |
| Data Layer | PostgreSQL 17 + psycopg2 |
| Frontend Host | Python HTTP Server (port 8000) |

## Database Tables

- **users** — user_id, username, email, role
- **projects** — project_id, owner_id, title
- **items** — item_id, project_id, name
- **tags** — tag_id, tag_name
- **item_tags** — item_id, tag_id (junction table)

## API Endpoints

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /users | Get all users |
| GET | /users/{user_id} | Get single user |
| POST | /users | Create user |
| PUT | /users/{user_id} | Update user email |
| DELETE | /users/{user_id} | Delete user |

### Projects
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /projects | Get all projects |
| GET | /projects/{project_id} | Get single project |
| GET | /projects/owner/{owner_id} | Get projects by owner (subset) |
| POST | /projects | Create project |
| DELETE | /projects/{project_id} | Delete project |

### Items
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /items | Get all items |
| GET | /items/{item_id} | Get single item |
| GET | /items/project/{project_id} | Get items by project (subset) |
| POST | /items | Create item |
| DELETE | /items/{item_id} | Delete item |

### Tags
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tags | Get all tags |
| GET | /tags/{tag_id} | Get single tag |
| POST | /tags | Create tag |
| DELETE | /tags/{tag_id} | Delete tag |

### Item Tags
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /item_tags | Get all item-tag links |
| GET | /item_tags/{item_id} | Get tags for item (subset) |
| POST | /item_tags | Link item to tag |
| DELETE | /item_tags/{item_id}/{tag_id} | Unlink item from tag |

## Project Structure

```
CSCE-548-PROJECT/
├── frontend/
│   ├── index.html       # Single-page user-friendly frontend UI
│   └── script.js        # JavaScript fetch() API calls
├── src/
│   ├── service.py       # FastAPI endpoints (all 5 tables, 26 endpoints)
│   ├── business.py      # Business logic and input validation
│   ├── db.py            # PostgreSQL database queries
│   └── __init__.py
├── sql/
│   ├── schema.sql       # Database schema
│   └── seed.sql         # Seed data
├── requirements.txt
└── README.md
```

## Setup and Running

### Prerequisites
- Python 3.10+
- PostgreSQL 17
- pgAdmin 4
- Virtual environment

### Installation

```bash
# Clone the repository
git clone https://github.com/saisruthivelpula2112/CSCE-548-PROJECT.git
cd CSCE-548-PROJECT

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows
# source .venv/bin/activate       # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### Database Setup

1. Open pgAdmin 4 and create a database named `csce548_project1`
2. Open the Query Tool and run `sql/schema.sql` (creates all 5 tables)
3. Run `sql/seed.sql` (inserts sample data)

Create a `.env` file in the project root:

```
DB_HOST=localhost
DB_NAME=csce548_project1
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_PORT=5432
```

### Running the Application

```bash
# Terminal 1 — Start backend API
uvicorn src.service:app --reload --host 127.0.0.1 --port 8080

# Terminal 2 — Start frontend (run from inside frontend/ folder)
cd frontend
python -m http.server 8000
```

Open **http://127.0.0.1:8000** in your browser.

Note: The frontend server must be started from inside the `frontend/` folder. Running from the project root shows a directory listing instead of the app.

## Features

- GET all records for all 5 tables
- GET single record for all 5 tables
- GET subset of records (filter by owner / project / item)
- INSERT (POST) for all 5 tables
- UPDATE (PUT) for users, projects, and items
- DELETE for all 5 tables
- User-friendly tabbed navigation — Users, Projects, Items, Tags, Item Tags
- Structured data tables with labeled columns — no raw JSON shown to user
- Color-coded role badges, avatar initials for users, green project badges
- Inline success/error messages — no alert popups
- Auto-refresh lists after every create, update, or delete
- Confirmation dialogs before all DELETE operations
- CORS enabled for cross-origin frontend/backend communication

## AI Tool Usage — Project 3

Code was generated using **Claude (Anthropic)** with the following prompt:

"Generate a complete HTML and JavaScript frontend for a FastAPI backend running at http://127.0.0.1:9000 with users, projects, items, tags, and item_tags tables. Create a single-page web application with sections for each table to fetch, create, and delete records using vanilla JavaScript with fetch(), show success/error feedback without alert popups, and automatically refresh lists after each operation."

**Modifications made to AI-generated code:**

- Added CORSMiddleware to service.py — critical fix; browser blocked all cross-origin requests without this
- Extended service, business, and data layers from users-only to all 5 tables
- Added GET subset endpoints: /projects/owner/{id}, /items/project/{id}, /item_tags/{item_id}
- Replaced alert() popups with inline green/red feedback boxes
- Added loading state indicator and enhanced network error messages
- Added red Delete buttons with confirmation dialogs to prevent accidental deletion
- Switched backend port from 9000 to 8080 after Windows firewall blocked port 9000 (WinError 10013)
- Following instructor feedback, the frontend interface was redesigned to replace raw text and JSON-style output with structured tables, labeled forms, and tab navigation. The redesigned frontend emphasizes usability and readability so that even non-technical users can easily understand and interact with the application

---

---

# Project 4 — Full System Test & Deployment

## Overview

Project 4 completes the n-tier application by performing a full system test across all four layers and producing a deployment document. All CRUD operations were tested through the updated user-friendly frontend and verified in pgAdmin. The frontend displays data in clean structured tables with labeled columns and color-coded badges — no raw JSON is shown to the user at any point.

## Architecture

| Layer | Technology | Description |
|-------|-----------|-------------|
| Data Layer | PostgreSQL 17 | Relational database with 5 tables |
| Business Layer | Python (business.py) | Input validation and logic |
| Service Layer | FastAPI + Uvicorn | REST API on port 8080 (26 endpoints) |
| Client Layer | HTML5 + JavaScript | User-friendly browser frontend on port 8000 |

## Project Structure

```
CSCE-548-PROJECT/
├── src/
│   ├── __init__.py
│   ├── db.py              # Data layer — raw SQL via psycopg2
│   ├── business.py        # Business layer — input validation
│   └── service.py         # Service layer — FastAPI routes (26 endpoints)
├── frontend/
│   ├── index.html         # Single-page user-friendly frontend UI
│   └── script.js          # JavaScript fetch() API calls
├── sql/
│   ├── schema.sql         # CREATE TABLE statements for all 5 tables
│   └── seed.sql           # Sample data inserts
├── .env                   # Database credentials (not committed to git)
├── requirements.txt       # Python dependencies
├── CSCE548_Project4_Deployment_Document.pdf
└── README.md
```

## Prerequisites

| Software | Version | Download |
|----------|---------|----------|
| Python | 3.10+ | https://python.org |
| PostgreSQL | 17 | https://postgresql.org |
| pgAdmin 4 | Latest | https://pgadmin.org |
| Git | Latest | https://git-scm.com |
| VS Code | Latest | https://code.visualstudio.com (optional) |
| Web Browser | Any | Chrome / Firefox / Edge |

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/saisruthivelpula2112/CSCE-548-PROJECT.git
cd CSCE-548-PROJECT
```

### 2. Set Up the Database

1. Open pgAdmin 4 and connect to your PostgreSQL 17 server
2. Right-click Databases, select Create > Database, name it `csce548_project1`
3. Right-click `csce548_project1` and open the Query Tool
4. Open `sql/schema.sql`, paste contents and press F5 (creates all 5 tables)
5. Open `sql/seed.sql`, paste contents and press F5 (inserts sample data)

Note: Always run schema.sql before seed.sql.

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```
DB_HOST=localhost
DB_NAME=csce548_project1
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_PORT=5432
```

### 4. Set Up Python Environment

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows
# source .venv/bin/activate       # Mac/Linux
pip install -r requirements.txt
```

### 5. Start the Backend

```bash
uvicorn src.service:app --reload --host 127.0.0.1 --port 8080
```

Expected output: `INFO: Application startup complete.`

Swagger UI available at: http://127.0.0.1:8080/docs

### 6. Start the Frontend

Open a second terminal:

```bash
cd frontend
python -m http.server 8000
```

Expected output: `Serving HTTP on :: port 8000`

### 7. Open the App

Navigate to: **http://127.0.0.1:8000**

You will see five tabs: Users, Projects, Items, Tags, Item Tags — each with Refresh, Filter, Get Single, Create, Update, and Delete functionality.

## API Endpoints

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /users | Get all users |
| GET | /users/{id} | Get user by ID |
| POST | /users | Create new user |
| PUT | /users/{id} | Update user email |
| DELETE | /users/{id} | Delete user |

### Projects
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /projects | Get all projects |
| GET | /projects/{id} | Get project by ID |
| GET | /projects/owner/{id} | Get projects by owner (subset) |
| POST | /projects | Create new project |
| PUT | /projects/{id} | Update project title |
| DELETE | /projects/{id} | Delete project |

### Items
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /items | Get all items |
| GET | /items/{id} | Get item by ID |
| GET | /items/project/{id} | Get items by project (subset) |
| POST | /items | Create new item |
| PUT | /items/{id} | Update item name |
| DELETE | /items/{id} | Delete item |

### Tags
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tags | Get all tags |
| GET | /tags/{id} | Get tag by ID |
| POST | /tags | Create new tag |
| DELETE | /tags/{id} | Delete tag |

### Item Tags
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /item_tags | Get all item-tag links |
| GET | /item_tags/{id} | Get tags for a specific item (subset) |
| POST | /item_tags | Link tag to item |
| DELETE | /item_tags/{item_id}/{tag_id} | Remove tag from item |

## System Test Results

All CRUD operations were tested via the updated user-friendly frontend and verified in pgAdmin.

| Table | GET All | GET Single | GET Subset | POST | PUT | DELETE |
|-------|---------|-----------|-----------|------|-----|--------|
| Users | PASS | PASS | N/A | PASS | PASS | PASS |
| Projects | PASS | PASS | PASS | PASS | PASS | PASS |
| Items | PASS | PASS | PASS | PASS | PASS | PASS |
| Tags | PASS | PASS | N/A | PASS | N/A | PASS |
| Item Tags | PASS | PASS | PASS | PASS | N/A | PASS |

## Troubleshooting

| Problem | Solution |
|---------|----------|
| ModuleNotFoundError: No module named 'src' | Run uvicorn from project root, not inside src/ |
| Directory listing at port 8000 | Run python -m http.server 8000 from inside frontend/ folder |
| 500 Error on /tags or /item_tags | Tags table uses tag_name not name — fixed in db.py |
| Delete failed with red error | Delete child records first (e.g. items before their project) |
| CORS error in browser DevTools | Check service.py has CORSMiddleware with allow_origins=["*"] |
| Port blocked — WinError 10013 | Use port 8080 instead of 9000 for backend |
| Site can't be reached | Both servers must be running simultaneously — restart if stopped |

## AI Tool Usage — Project 4

This project was built with assistance from **Claude (Anthropic)** for code generation across all layers.

**Prompts used per layer:**

| Layer | Prompt | What Was Generated |
|-------|--------|-------------------|
| Data Layer (db.py) | Generate db.py for PostgreSQL with full CRUD for 5 tables using psycopg2 | Complete db.py with get, create, update, delete for all tables |
| Business Layer (business.py) | Generate business.py wrapping db.py with input validation for all 5 tables | Complete business.py with validation logic |
| Service Layer (service.py) | Generate FastAPI service.py with all CRUD endpoints including PUT for all tables | FastAPI app with 26 endpoints and CORSMiddleware |
| Frontend (index.html) | Generate HTML frontend with all 5 table sections with Load, Create, Update, Delete | Complete single-page HTML with all 5 table sections |
| Frontend (script.js) | Generate JavaScript using fetch() with async/await and Array.isArray() safety checks | Complete script.js with error handling |
| Frontend UI redesign | Redesign the frontend to replace raw text with structured tables, tab navigation, and badges | New user-friendly index.html with clean tables and color-coded badges |

**Changes made to AI-generated output:**

| File | Issue | Fix Applied |
|------|-------|------------|
| db.py | Tags table uses tag_name — AI assumed name | Fixed all SQL queries to use tag_name |
| db.py | item_tags JOIN used wrong column aliases | Corrected aliases in get_all_item_tags() and get_tags_for_item() |
| service.py | PUT endpoints for /projects and /items were missing | Added both PUT endpoints with Query parameters |
| service.py | Route ordering caused 404 errors | Reordered — specific paths before generic path parameters |
| service.py | Import names mismatched after business.py refactor | Updated all imports to match new function names |
| script.js | forEach is not a function crash on load | Added Array.isArray() safety checks in all load functions |
| Frontend | Raw text UI failed instructor usability review | Fully redesigned with structured tables, badges, and tab navigation |

**AI Effectiveness Analysis:**

What the AI did well:
- Generated complete, syntactically correct Python for all layers on the first attempt in most cases
- Correctly structured FastAPI with CORSMiddleware, Query parameters, and proper HTTP status codes
- Accurately diagnosed runtime errors from error descriptions and screenshots
- Generated professional documentation with structured tables and code blocks

Where the AI fell short:
- Assumed tags table used a name column — actually uses tag_name (schema not visible to AI)
- PUT endpoints for projects and items were omitted from initial generation
- Route ordering conflicts in FastAPI were not automatically handled
- Initial frontend UI was not user-friendly — required full redesign after instructor feedback

