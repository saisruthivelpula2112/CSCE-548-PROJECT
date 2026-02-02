# CSCE 548 – Project 1

## Project Overview
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
CSCE-548-PROJECT/
│
├── sql/
│ ├── schema.sql
│ └── seed.sql
│
├── src/
│ ├── init.py
│ ├── db.py
│ └── run_crud.py
│
├── .gitignore
└── README.md
