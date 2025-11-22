# app/routes/basic_info_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, crud

router = APIRouter(prefix="/basic-info", tags=["Basic Information"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{userid}", response_model=schemas.BasicInformationOut)
def read_basic_info(userid: str, db: Session = Depends(get_db)):
    rec = crud.basic_info.get_by_userid(db, userid)
    if not rec:
        raise HTTPException(status_code=404, detail="User not found")
    return rec

@router.post("/", response_model=schemas.BasicInformationOut)
def upsert_basic_info(data: schemas.BasicInformationCreate, db: Session = Depends(get_db)):
    rec = crud.basic_info.upsert_basic_info(db, data)
    return rec
