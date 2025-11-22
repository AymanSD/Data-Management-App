# app/schemas.py
from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

# ---------------- Basic Info ----------------
class BasicInfoBase(BaseModel):
    FULLNAME: str
    FirstName: str
    LastName: str
    UserID: str
    DoB: date
    National_IqamaID: str = Field(..., alias="National/IqamaID")
    PassportNo: str
    Gender: str
    Nationality: str
    PhoneNo: str
    AlternativePhoneNo: str
    Email: str
    EmergencyContact: str
    EmergencyPhone: str
    LastUpdated: date

class BasicInfoCreate(BasicInfoBase):
    pass

class BasicInfoOut(BasicInfoBase):
    RER_ID: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

# ---------------- Contract Info ----------------
class ContractInfoBase(BaseModel):
    UserID: str
    Company: str
    JobTitle: str
    ContractPeriod: str
    Email: str
    StartDate: date
    IsActive: bool
    EndDate: Optional[date] = None

class ContractInfoCreate(ContractInfoBase):
    pass

class ContractInfoOut(ContractInfoBase):
    ID: int

    class Config:
        orm_mode = True

# ---------------- Accounts & Access ----------------
class AccountsAccessBase(BaseModel):
    UserID: str
    RER_Email: bool
    BiometricAccess: bool
    CasePortalAccount: bool
    CasePortalRole: bool
    geoAccount: bool
    geosAccount: bool
    ArcGIS: bool
    RiyadAmana: bool
    EasternAmana: bool
    MadinahAmana: bool
    QasimAmana: bool
    MakkaAmana: bool
    AssignmentDate: date
    IsActive: bool

class AccountsAccessCreate(AccountsAccessBase):
    pass

class AccountsAccessOut(AccountsAccessBase):
    ID: int

    class Config:
        orm_mode = True

# ---------------- Roles ----------------
class RoleBase(BaseModel):
    UserID: str
    FULLNAME: str
    PortalName: str
    Email: str
    Role: str
    AssignedTo: str
    IsSupervisor: bool
    SupervisorName: Optional[str] = None
    GroupID: Optional[str] = None
    AssignmentDate: date
    IsActive: bool

class RoleCreate(RoleBase):
    pass

class RoleOut(RoleBase):
    RoleID: int

    class Config:
        orm_mode = True

# ---------------- Leave & Absence ----------------
class LeaveAbsenceBase(BaseModel):
    UserID: str
    LeaveType: str
    StartDate: date
    EndDate: date
    TotalDays: int
    Notes: Optional[str] = None
    Status: str
    AppliedOn: date
    IsApproved: bool
    ApprovedBy: Optional[str] = None
    ApprovalDate: Optional[date] = None

class LeaveAbsenceCreate(LeaveAbsenceBase):
    pass

class LeaveAbsenceOut(LeaveAbsenceBase):
    ID: int

    class Config:
        orm_mode = True
