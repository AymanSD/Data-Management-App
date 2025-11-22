# app/models.py
from sqlalchemy import Column, Integer, Text, Boolean, Date
from app.database import Base

# NOTE:
# We keep the exact table names you provided (including &). SQLAlchemy will quote them.
# For special column names like "National/IqamaID", we provide an explicit column name.

class BasicInformation(Base):
    __tablename__ = "BasicInfo"
    __table_args__ = {"schema": "employees"}

    RER_ID = Column(Integer, primary_key=True, autoincrement=True)
    FULLNAME = Column(Text, nullable=False)
    FirstName = Column(Text, nullable=False)
    LastName = Column(Text, nullable=False)
    UserID = Column(Text, nullable=False, unique=True)
    DoB = Column(Date, nullable=False)
    National_IqamaID = Column("National/IqamaID", Text, nullable=False)
    PassportNo = Column(Text, nullable=False)
    Gender = Column(Text, nullable=False)
    Nationality = Column(Text, nullable=False)
    PhoneNo = Column(Text, nullable=False)
    AlternativePhoneNo = Column(Text, nullable=False)
    Email = Column(Text, nullable=False)
    EmergencyContact = Column(Text, nullable=False)
    EmergencyPhone = Column(Text, nullable=False)
    LastUpdated = Column(Date, nullable=False)


class ContractInfo(Base):
    __tablename__ = "ContractInfo"
    __table_args__ = {"schema": "employees"}

    ID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Text, nullable=False)
    Company = Column(Text, nullable=False)
    JobTitle = Column(Text, nullable=False)
    ContractPeriod = Column(Text, nullable=False)
    Email = Column(Text, nullable=False)
    StartDate = Column(Date, nullable=False)
    IsActive = Column(Boolean, nullable=False)
    EndDate = Column(Date, nullable=True)


class AccountsAccess(Base):
    __tablename__ = "Accounts&Access"
    __table_args__ = {"schema": "employees"}

    ID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Text, nullable=False)
    RER_Email = Column(Boolean, nullable=False)
    BiometricAccess = Column(Boolean, nullable=False)
    CasePortalAccount = Column(Boolean, nullable=False)
    CasePortalRole = Column(Boolean, nullable=False)
    geoAccount = Column(Boolean, nullable=False)
    geosAccount = Column(Boolean, nullable=False)
    ArcGIS = Column(Boolean, nullable=False)
    RiyadAmana = Column(Boolean, nullable=False)
    EasternAmana = Column(Boolean, nullable=False)
    MadinahAmana = Column(Boolean, nullable=False)
    QasimAmana = Column(Boolean, nullable=False)
    MakkaAmana = Column(Boolean, nullable=False)
    AssignmentDate = Column(Date, nullable=False)
    IsActive = Column(Boolean, nullable=False)


class Roles(Base):
    __tablename__ = "Roles"
    __table_args__ = {"schema": "employees"}

    RoleID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Text, nullable=False)
    FULLNAME = Column(Text, nullable=False)
    PortalName = Column(Text, nullable=False)
    Email = Column(Text, nullable=False)
    Role = Column(Text, nullable=False)
    AssignedTo = Column(Text, nullable=False)
    IsSupervisor = Column(Boolean, nullable=False)
    SupervisorName = Column(Text, nullable=True)
    GroupID = Column(Text, nullable=True)
    AssignmentDate = Column(Date, nullable=False)
    IsActive = Column(Boolean, nullable=False)


class LeaveAbsence(Base):
    __tablename__ = "Leave&Absence"
    __table_args__ = {"schema": "employees"}

    ID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Text, nullable=False)
    LeaveType = Column(Text, nullable=False)
    StartDate = Column(Date, nullable=False)
    EndDate = Column(Date, nullable=False)
    TotalDays = Column(Integer, nullable=False)
    Notes = Column(Text, nullable=True)
    Status = Column(Text, nullable=False)
    AppliedOn = Column(Date, nullable=False)
    IsApproved = Column(Boolean, nullable=False)
    ApprovedBy = Column(Text, nullable=True)
    ApprovalDate = Column(Date, nullable=True)
