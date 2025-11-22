# app/routes/accounts_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, crud

router = APIRouter(prefix="/accounts", tags=["Accounts & Access"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{userid}", response_model=schemas.AccountsAccessOut)
def read_accounts(userid: str, db: Session = Depends(get_db)):
    rec = crud.accounts.get_by_userid(db, userid)
    if not rec:
        raise HTTPException(status_code=404, detail="Accounts record not found")
    return rec

@router.post("/", response_model=schemas.AccountsAccessOut)
def upsert_accounts(data: schemas.AccountsAccessCreate, db: Session = Depends(get_db)):
    rec = crud.accounts.upsert_accounts(db, data)
    return rec
