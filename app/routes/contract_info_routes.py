# app/routes/contract_info_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, crud

router = APIRouter(prefix="/contract", tags=["Contract Info"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{userid}", response_model=schemas.ContractInfoOut)
def read_contract(userid: str, db: Session = Depends(get_db)):
    rec = crud.contract_info.get_by_userid(db, userid)
    if not rec:
        raise HTTPException(status_code=404, detail="Contract not found")
    return rec

@router.post("/", response_model=schemas.ContractInfoOut)
def upsert_contract(data: schemas.ContractInfoCreate, db: Session = Depends(get_db)):
    rec = crud.contract_info.upsert_contract_info(db, data)
    return rec
