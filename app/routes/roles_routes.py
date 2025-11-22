# app/routes/roles_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, crud

router = APIRouter(prefix="/roles", tags=["Roles"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{userid}", response_model=list[schemas.RoleOut])
def list_roles(userid: str, db: Session = Depends(get_db)):
    recs = crud.roles.list_roles_by_user(db, userid)
    return recs

@router.post("/", response_model=schemas.RoleOut)
def add_role(data: schemas.RoleCreate, db: Session = Depends(get_db)):
    rec = crud.roles.add_role(db, data)
    return rec
