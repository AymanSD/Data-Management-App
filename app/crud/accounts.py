# app/crud/accounts.py
from sqlalchemy.orm import Session
from app import models, schemas
from datetime import date

def get_by_userid(db: Session, userid: str):
    return db.query(models.AccountsAccess).filter(models.AccountsAccess.UserID == userid).first()

def upsert_accounts(db: Session, data: schemas.AccountsAccessCreate):
    rec = db.query(models.AccountsAccess).filter(models.AccountsAccess.UserID == data.UserID).first()
    if rec:
        rec.RER_Email = data.RER_Email
        rec.BiometricAccess = data.BiometricAccess
        rec.CasePortalAccount = data.CasePortalAccount
        rec.CasePortalRole = data.CasePortalRole
        rec.geoAccount = data.geoAccount
        rec.geosAccount = data.geosAccount
        rec.ArcGIS = data.ArcGIS
        rec.RiyadAmana = data.RiyadAmana
        rec.EasternAmana = data.EasternAmana
        rec.MadinahAmana = data.MadinahAmana
        rec.QasimAmana = data.QasimAmana
        rec.MakkaAmana = data.MakkaAmana
        rec.AssignmentDate = data.AssignmentDate or date.today()
        rec.IsActive = data.IsActive
        db.add(rec)
        db.commit()
        db.refresh(rec)
        return rec
    else:
        new_rec = models.AccountsAccess(
            UserID = data.UserID,
            RER_Email = data.RER_Email,
            BiometricAccess = data.BiometricAccess,
            CasePortalAccount = data.CasePortalAccount,
            CasePortalRole = data.CasePortalRole,
            geoAccount = data.geoAccount,
            geosAccount = data.geosAccount,
            ArcGIS = data.ArcGIS,
            RiyadAmana = data.RiyadAmana,
            EasternAmana = data.EasternAmana,
            MadinahAmana = data.MadinahAmana,
            QasimAmana = data.QasimAmana,
            MakkaAmana = data.MakkaAmana,
            AssignmentDate = data.AssignmentDate or date.today(),
            IsActive = data.IsActive
        )
        db.add(new_rec)
        db.commit()
        db.refresh(new_rec)
        return new_rec
