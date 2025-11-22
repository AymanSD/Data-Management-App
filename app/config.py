# app/config.py
from os import getenv

# Example env var:
# export DATABASE_URL="postgresql://postgres:password@localhost:5432/GSA"
DATABASE_URL = getenv("DATABASE_URL", "postgresql://postgres:1234@localhost:5432/GSA")
SCHEMA_NAME = "employees"
