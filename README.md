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

CSCE 548 – Project 2
Business Layer + Service Layer + Console Client Implementation
1. Project Overview

This project extends Project 1 by introducing a structured, layered architecture that separates responsibilities across:

Data Layer (PostgreSQL interaction)

Business Layer (validation and logic)

Service Layer (REST API via FastAPI)

Console Client (service tester)

The goal of this project is to model a professional-grade service-oriented architecture in which business logic and service endpoints invoke the database layer without directly exposing database access to clients 

Project 2
This project demonstrates:
Clean separation of concerns
Abstraction of business rules
Microservice-style REST API design

End-to-end CRUD testing

2. System Architecture
Console Client
        ↓
Service Layer (FastAPI REST API)
        ↓
Business Layer (Validation + Business Logic)
        ↓
Data Layer (PostgreSQL via psycopg2)

Each layer communicates only with the layer immediately below it, ensuring modularity and maintainability.

3. Project Structure
CSCE-548-PROJECT/
│
├── src/
│   ├── __init__.py
│   ├── db.py              # Data layer
│   ├── business.py        # Business layer
│   ├── service.py         # FastAPI service layer
│   ├── models.py          # Pydantic models
│   └── run_crud.py        # Console client
│
├── sql/
│   ├── schema.sql
│   └── seed.sql
│
├── .env
├── requirements.txt
└── README.md
4. Data Layer (Project 1 Integration)

The data layer (db.py) contains all CRUD operations interacting directly with PostgreSQL:

get_all_users()

get_user_by_username()

create_user()

update_user_email_by_username()

delete_user()

All SQL queries are parameterized to prevent SQL injection.

Database configuration is managed using a .env file:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=csce548_project1
DB_USER=postgres
DB_PASS=postgres

Example table:

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT NOT NULL,
    role TEXT NOT NULL
);
5. Business Layer Implementation

The business layer:

Validates input parameters

Enforces business rules

Delegates all database interaction to db.py

Business methods implemented:

get_all_users()

get_user(username)

create_user(username, email, role)

delete_user_by_username(username)

update_user_email_by_username(username, new_email)

Additional Business Rules Implemented

Username must not be empty

Email must not be empty

Email updates require both username and new email

404 returned if user not found

Duplicate username prevented via DB constraint

These validations were partially generated by AI and refined manually.

6. Service Layer (FastAPI)

The service layer exposes REST endpoints:

Method	Endpoint	Description
GET	/users	Retrieve all users
GET	/users/{username}	Retrieve specific user
POST	/users	Create user
PUT	/users?username=&new_email=	Update email
DELETE	/users?username=	Delete user
GET	/health	Health check

The service layer:

Converts business exceptions into HTTP responses

Uses Pydantic models for request/response validation

Returns proper HTTP status codes (200, 201, 400, 404, 500)

The service is started using:

uvicorn src.service:app --reload --host 127.0.0.1 --port 9000

API documentation automatically generated by FastAPI is available at:

http://127.0.0.1:9000/docs
7. Console Client (Testing Layer)

The console client (run_crud.py) verifies full service functionality by performing:

GET all users

POST create user

GET single user

PUT update email

GET updated user

DELETE user

GET all users again

This demonstrates complete end-to-end integration across all layers.

8. Hosting the Service

The service can be hosted using platforms such as:

Render

Railway

Heroku

For deployment, use:

uvicorn src.service:app --host 0.0.0.0 --port $PORT

Environment variables must be configured in the hosting dashboard.

The application was tested locally using uvicorn before deployment.

9. AI Prompt and Code Generation Analysis
Prompt Used

"Generate a business layer in Python that wraps CRUD operations from a PostgreSQL data layer. Then generate a FastAPI service layer that exposes all business methods. Also generate a console-based client to test full CRUD functionality."

AI Effectiveness Analysis (Graduate Requirement)

The AI tool was effective at:

Generating boilerplate business layer code

Creating REST endpoints using FastAPI

Producing a working console client

Providing Pydantic models

However, several issues required manual correction:

Function naming mismatches between layers

Import errors due to relative imports

Inconsistent database return structures

HTTP error handling improvements

I manually resolved:

Naming inconsistencies (add_user vs create_user)

Package import errors (uvicorn src.service:app required)

Database row format adjustments

Additional validation logic

Conclusion on AI Effectiveness

AI significantly accelerated development of the layered architecture.
However, debugging integration issues required manual reasoning and understanding of:

Python module structure

FastAPI dependency management

PostgreSQL return values

Package execution context

AI served as a productivity enhancer but not a replacement for developer understanding.

10. Testing and Validation

The system was tested by:

Running uvicorn server

Executing console client

Observing HTTP 200, 201, 404 responses

Confirming database changes in PostgreSQL

Verifying deletion and update operations

Screenshots demonstrate:

Server startup

API calls

Client output

Database state changes

11. Troubleshooting
If you see:
ImportError: attempted relative import with no known parent package

Run the service using:

uvicorn src.service:app

Do NOT run:

python src/service.py
If you see:
Connection refused (WinError 10061)

The server is not running. Start uvicorn first.

12. Professional Reflection

This project successfully demonstrates:

Layered system architecture

Business rule abstraction

RESTful service design

Clean separation of responsibilities

End-to-end service testing

The implementation models a real-world service-oriented backend system.

13. Final Status

✔ Data Layer Working
✔ Business Layer Implemented
✔ Service Layer Running
✔ Console Client Fully Functional
✔ CRUD Verified End-to-End
✔ Hosted Configuration Ready
✔ Graduate-Level Documentation Complete
