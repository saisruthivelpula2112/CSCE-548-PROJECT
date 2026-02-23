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
