# app/crud/basic_info.py
from sqlalchemy.orm import Session
from app import models, schemas
from datetime import date

def get_by_userid(db: Session, userid: str):
    return db.query(models.BasicInformation).filter(models.BasicInformation.UserID == userid).first()

def upsert_basic_info(db: Session, data: schemas.BasicInfoCreate):
    # Append/Update rule: update existing if UserID exists, else insert
    user = db.query(models.BasicInformation).filter(models.BasicInformation.UserID == data.UserID).first()
    if user:
        # update fields
        user.FULLNAME = data.FULLNAME
        user.FirstName = data.FirstName
        user.LastName = data.LastName
        user.DoB = data.DoB
        user.National_IqamaID = data.National_IqamaID
        user.PassportNo = data.PassportNo
        user.Gender = data.Gender
        user.Nationality = data.Nationality
        user.PhoneNo = data.PhoneNo
        user.AlternativePhoneNo = data.AlternativePhoneNo
        user.Email = data.Email
        user.EmergencyContact = data.EmergencyContact
        user.EmergencyPhone = data.EmergencyPhone
        user.LastUpdated = data.LastUpdated or date.today()
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    else:
        new_user = models.BasicInformation(
            FULLNAME = data.FULLNAME,
            FirstName = data.FirstName,
            LastName = data.LastName,
            UserID = data.UserID,
            DoB = data.DoB,
            National_IqamaID = data.National_IqamaID,
            PassportNo = data.PassportNo,
            Gender = data.Gender,
            Nationality = data.Nationality,
            PhoneNo = data.PhoneNo,
            AlternativePhoneNo = data.AlternativePhoneNo,
            Email = data.Email,
            EmergencyContact = data.EmergencyContact,
            EmergencyPhone = data.EmergencyPhone,
            LastUpdated = data.LastUpdated or date.today()
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
