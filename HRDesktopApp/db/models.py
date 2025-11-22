from sqlalchemy import Column, Integer, String, Boolean, Date, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BasicInformation(Base):
    __tablename__ = 'BasicInfo'
    __table_args__ = {'schema': 'employees'}
    
    RER_ID = Column(Integer, primary_key=True)
    FULLNAME = Column(Text, nullable=False)
    FirstName = Column(Text, nullable=False)
    LastName = Column(Text, nullable=False)
    UserID = Column(Text, nullable=False)
    DoB = Column(Date, nullable=False)
    National_IqamaID = Column(Text, nullable=False)
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
    __tablename__ = 'ContractInfo'
    __table_args__ = {'schema': 'employees'}
    
    ID = Column(Integer, primary_key=True)
    UserID = Column(Text, nullable=False)
    Company = Column(Text, nullable=False)
    JobTitle = Column(Text, nullable=False)
    ContractPeriod = Column(Text, nullable=False)
    Email = Column(Text, nullable=False)
    StartDate = Column(Date, nullable=False)
    IsActive = Column(Boolean, nullable=False)
    EndDate = Column(Date)

class Roles(Base):
    __tablename__ = 'Roles'
    __table_args__ = {'schema': 'employees'}
    
    RoleID = Column(Integer, primary_key=True)
    UserID = Column(Text, nullable=False)
    FULLNAME = Column(Text, nullable=False)
    PortalName = Column(Text, nullable=False)
    Email = Column(Text, nullable=False)
    Role = Column(Text, nullable=False)
    AssignedTo = Column(Text, nullable=False)
    IsSupervisor = Column(Boolean, nullable=False)
    SupervisorName = Column(Text)
    GroupID = Column(Text)
    AssignmentDate = Column(Date, nullable=False)
    IsActive = Column(Boolean, nullable=False)

class AccountsAccess(Base):
    __tablename__ = 'Accounts&Access'
    __table_args__ = {'schema': 'employees'}
    
    ID = Column(Integer, primary_key=True)
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

class LeaveAbsence(Base):
    __tablename__ = 'Leave&Absence'
    __table_args__ = {'schema': 'employees'}
    
    ID = Column(Integer, primary_key=True)
    UserID = Column(Text, nullable=False)
    LeaveType = Column(Text, nullable=False)
    StartDate = Column(Date, nullable=False)
    EndDate = Column(Date, nullable=False)
    TotalDays = Column(Integer, nullable=False)
    Notes = Column(Text)
    Status = Column(Text, nullable=False)
    AppliedOn = Column(Date, nullable=False)
    IsApproved = Column(Boolean, nullable=False)
    ApprovedBy = Column(Text)
    ApprovalDate = Column(Date, nullable=False)
