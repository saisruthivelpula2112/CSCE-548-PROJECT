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
