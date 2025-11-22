# app/crud/contract_info.py
from sqlalchemy.orm import Session
from app import models, schemas
from datetime import date

def get_by_userid(db: Session, userid: str):
    return db.query(models.ContractInfo).filter(models.ContractInfo.UserID == userid).first()

def upsert_contract_info(db: Session, data: schemas.ContractInfoCreate):
    rec = db.query(models.ContractInfo).filter(models.ContractInfo.UserID == data.UserID).first()
    if rec:
        rec.Company = data.Company
        rec.JobTitle = data.JobTitle
        rec.ContractPeriod = data.ContractPeriod
        rec.Email = data.Email
        rec.StartDate = data.StartDate
        rec.IsActive = data.IsActive
        rec.EndDate = data.EndDate
        db.add(rec)
        db.commit()
        db.refresh(rec)
        return rec
    else:
        new_rec = models.ContractInfo(
            UserID = data.UserID,
            Company = data.Company,
            JobTitle = data.JobTitle,
            ContractPeriod = data.ContractPeriod,
            Email = data.Email,
            StartDate = data.StartDate,
            IsActive = data.IsActive,
            EndDate = data.EndDate
        )
        db.add(new_rec)
        db.commit()
        db.refresh(new_rec)
        return new_rec
