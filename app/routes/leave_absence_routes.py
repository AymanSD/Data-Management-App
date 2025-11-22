# app/routes/leave_absence_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, crud

router = APIRouter(prefix="/leave", tags=["Leave & Absence"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{userid}", response_model=list[schemas.LeaveAbsenceOut])
def get_user_leaves(userid: str, db: Session = Depends(get_db)):
    recs = crud.leave_absence.get_leaves_by_user(db, userid)
    return recs

@router.post("/apply", response_model=schemas.LeaveAbsenceOut)
def apply_for_leave(data: schemas.LeaveAbsenceCreate, db: Session = Depends(get_db)):
    rec = crud.leave_absence.create_leave_request(db, data)
    return rec

@router.post("/approve/{leave_id}", response_model=schemas.LeaveAbsenceOut)
def approve_leave(leave_id: int, approved_by: str, db: Session = Depends(get_db)):
    rec = crud.leave_absence.approve_leave(db, leave_id, approved_by)
    if rec is None:
        raise HTTPException(status_code=404, detail="Leave request not found")
    return rec
