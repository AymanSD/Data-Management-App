CREATE TABLE IF NOT EXISTS employees."BasicInformation"
(
    "RER_ID" SERIAL PRIMARY KEY NOT NULL,
    "FULLNAME" TEXT NOT NULL,
    "FirstName" TEXT NOT NULL,
    "LastName" TEXT NOT NULL,
	"UserID" TEXT NOT NULL,
    "DoB" date NOT NULL,
    "National/IqamaID" TEXT NOT NULL,
    "PassportNo" TEXT NOT NULL,
    "Gender" TEXT NOT NULL,
    "Nationality" TEXT NOT NULL,
    "PhoneNo" TEXT NOT NULL,
    "AlternativePhoneNo" TEXT NOT NULL,
    "Email" TEXT NOT NULL,
    "EmergencyContact" TEXT NOT NULL,
    "EmergencyPhone" TEXT NOT NULL,
    "LastUpdated" date NOT NULL,
)

CREATE TABLE IF NOT EXISTS employees."ContractInfo"
(
    "ID" SERIAL PRIMARY KEY NOT NULL,
	"UserID" TEXT NOT NULL,
    "Company" TEXT NOT NULL,
    "JobTitle" TEXT NOT NULL,
    "ContractPeriod" TEXT NOT NULL,
	"Email" TEXT NOT NULL
    "StartDate" DATE NOT NULL,
    "IsActive" BOOLEAN NOT NULL,
	"EndDate" DATE,
)

CREATE TABLE IF NOT EXISTS employees."Roles" (
	"RoleID" SERIAL PRIMARY KEY,
	"UserID" TEXT NOT NULL,
	"FULLNAME" TEXT NOT NULL,
	"PortalName" TEXT NOT NULL,
	"Email" TEXT NOT NULL,
	"Role" TEXT NOT NULL,
	"AssignedTo" TEXT NOT NULL,
	"IsSupervisor" BOOLEAN NOT NULL,
	"SupervisorName" TEXT,
	"GroupID" TEXT,
	"AssignmentDate" DATE NOT NULL,
	"IsActive" BOOLEAN NOT NULL
)


CREATE TABLE IF NOT EXISTS employees."Accounts&Access" (
	"ID" SERIAL PRIMARY KEY,
	"UserID" TEXT NOT NULL,
	"RER_Email" BOOLEAN NOT NULL,
	"BiometricAccess" BOOLEAN NOT NULL,
	"CasePortalAccount" BOOLEAN NOT NULL,
	"CasePortalRole" BOOLEAN NOT NULL,
	"geoAccount" BOOLEAN NOT NULL,
	"geosAccount" BOOLEAN NOT NULL,
	"ArcGIS" BOOLEAN NOT NULL,
	"RiyadAmana" BOOLEAN NOT NULL,
	"EasternAmana" BOOLEAN NOT NULL,
	"MadinahAmana" BOOLEAN NOT NULL,
	"QasimAmana" BOOLEAN NOT NULL,
	"MakkaAmana" BOOLEAN NOT NULL,
	"AssignmentDate" DATE NOT NULL,
	"IsActive" BOOLEAN NOT NULL
)

CREATE TABLE IF NOT EXISTS employees."Leave&Absence" (
	"ID" SERIAL PRIMARY KEY,
	"UserID" TEXT NOT NULL,
	"LeaveType" TEXT NOT NULL,
	"StartDate" DATE NOT NULL,
	"EndDate" DATE NOT NULL,
	"TotalDays" INTEGER NOT NULL,
	"Notes" TEXT,
	"Status" TEXT NOT NULL,
	"AppliedOn" DATE NOT NULL,
	"IsApproved" BOOLEAN NOT NULL,
	"ApprovedBy" TEXT,
	"ApprovalDate" DATE NOT NULL
)
