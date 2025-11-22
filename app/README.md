# GSA HR Employee Management (FastAPI + SQLAlchemy)

## Overview
This project provides a REST API over a PostgreSQL DB (schema `employees`) using FastAPI and SQLAlchemy.
It implements CRUD and business rules for:
- BasicInformation (upsert by UserID)
- ContractInfo (upsert by UserID)
- Accounts&Access (upsert by UserID)
- Roles (append-only)
- Leave&Absence (append-only)

## Setup
1. Create PostgreSQL DB `GSA` and ensure user credentials are configured.
2. Export DATABASE_URL (optional) or edit `app/config.py`:
