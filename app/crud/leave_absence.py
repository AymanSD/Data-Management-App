# app/crud/leave_absence.py
from sqlalchemy.orm import Session
from app import models, schemas
from datetime import date
from app.utils import calculate_total_days

def get_leaves_by_user(db: Session, userid: str):
    return db.query(models.LeaveAbsence).filter(models.LeaveAbsence.UserID == userid).order_by(models.LeaveAbsence.AppliedOn.desc()).all()

def create_leave_request(db: Session, data: schemas.LeaveAbsenceCreate):
    total_days = data.TotalDays or calculate_total_days(data.StartDate, data.EndDate)
    new_leave = models.LeaveAbsence(
        UserID = data.UserID,
        LeaveType = data.LeaveType,
        StartDate = data.StartDate,
        EndDate = data.EndDate,
        TotalDays = total_days,
        Notes = data.Notes,
        Status = data.Status,
        AppliedOn = data.AppliedOn,
        IsApproved = data.IsApproved,
        ApprovedBy = data.ApprovedBy,
        ApprovalDate = data.ApprovalDate
    )
    db.add(new_leave)
    db.commit()
    db.refresh(new_leave)
    return new_leave

def approve_leave(db: Session, leave_id: int, approved_by: str):
    rec = db.query(models.LeaveAbsence).filter(models.LeaveAbsence.ID == leave_id).first()
    if not rec:
        return None
    rec.IsApproved = True
    rec.Status = "Approved"
    rec.ApprovedBy = approved_by
    rec.ApprovalDate = date.today()
    db.add(rec)
    db.commit()
    db.refresh(rec)
    return rec
