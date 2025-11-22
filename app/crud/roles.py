# app/crud/roles.py
from sqlalchemy.orm import Session
from app import models, schemas
from datetime import date

def list_roles_by_user(db: Session, userid: str):
    return db.query(models.Roles).filter(models.Roles.UserID == userid).all()

def add_role(db: Session, data: schemas.RoleCreate):
    new_role = models.Roles(
        UserID = data.UserID,
        FULLNAME = data.FULLNAME,
        PortalName = data.PortalName,
        Email = data.Email,
        Role = data.Role,
        AssignedTo = data.AssignedTo,
        IsSupervisor = data.IsSupervisor,
        SupervisorName = data.SupervisorName,
        GroupID = data.GroupID,
        AssignmentDate = data.AssignmentDate,
        IsActive = data.IsActive
    )
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role
