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
'''text
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
└── README.md '''



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

   




