# app/utils.py
from datetime import date
from typing import Optional

def today_date() -> date:
    return date.today()

def safe_int(value, default=0):
    try:
        return int(value)
    except Exception:
        return default

def calculate_total_days(start_date, end_date):
    if start_date and end_date:
        return (end_date - start_date).days + 1
    return 0
