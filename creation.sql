CREATE DATABASE OROMIYA_INVESTMENT_HRMS;

USE DATABASE_OROMIYA_INVESTMENT_HRMS;


-- Create table for Jobs
CREATE TABLE Jobs(
    JobID VARCHAR(7) NOT NULL,
    JobName VARCHAR(50) NOT NULL,
    JobDescription VARCHAR(60) NOT NULL,
    Salary MONEY NOT NULL,
    Rank INT,
    PRIMARY KEY (JobID)
);
-- Create table for Department
CREATE TABLE Department (
    DepartmentID VARCHAR(7) NOT NULL,
    DepartmentName VARCHAR(30) NOT NULL,
    PRIMARY KEY (DepartmentID)
);
-- Create table for Address
CREATE TABLE Address(
    AddressID VARCHAR(7) NOT NULL,
    City VARCHAR(30) NOT NULL,
    Subcity VARCHAR(30) NOT NULL,
    Woreda INT NOT NULL,
    Kebele INT NOT NULL,
    PRIMARY KEY (AddressID)
);
CREATE TABLE Employee(
    EmployeeID VARCHAR(7) NOT NULL,
    EmpName VARCHAR(50) NOT NULL,
    Gender CHAR(1) NOT NULL CHECK(Gender IN ('M', 'F')),
    DOB DATETIME NOT NULL,
    DOE DATETIME DEFAULT CURRENT_TIMESTAMP,
    Age INT,
    PhoneNo VARCHAR(11) NOT NULL,
    Status VARCHAR(15) DEFAULT 'Available' CHECK(Status IN ('Available', 'Terminated')),
    DepartmentID VARCHAR(7), 
    JobID VARCHAR(7), 
    AddressID VARCHAR(7),
    TaxPayerTinNo VARCHAR(12),
    PRIMARY KEY (EmployeeID),
    FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID) ON UPDATE CASCADE ON DELETE SET NULL, 
    FOREIGN KEY (JobID) REFERENCES Jobs(JobID) ON UPDATE CASCADE ON DELETE SET NULL, 
    FOREIGN KEY (AddressID) REFERENCES Address(AddressID) ON UPDATE CASCADE ON DELETE SET NULL
);
-- Create table for TerminatedEmployees
CREATE TABLE TerminatedEmployees (
    TerminationID VARCHAR(10) NOT NULL PRIMARY KEY,
    TerminationDate DATE NOT NULL,
    TerminationReason VARCHAR(25) NOT NULL,
    EmployeeID VARCHAR(7) NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID) ON UPDATE CASCADE ON DELETE NO ACTION
);
-- Create table for AcademicStatus
CREATE TABLE AcademicStatus(
    EmployeeID VARCHAR(7) NOT NULL,
    CertificationName VARCHAR(30) NOT NULL,
    InstitutionName VARCHAR(30),
    PRIMARY KEY (EmployeeID, CertificationName),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID) ON UPDATE CASCADE ON DELETE CASCADE
);
-- Create table for Attendance
CREATE TABLE Attendance (
    EmployeeID VARCHAR(7) NOT NULL,
    Month INT NOT NULL CHECK(Month > 0 and Month < 13),
    totalDaysPresent INT NOT NULL,
    allowedBreaks INT NOT NULL,
    totalDaysAbsent INT NOT NULL,
    PRIMARY KEY (EmployeeID, Month),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID) ON UPDATE CASCADE ON DELETE NO ACTION
);
-- Create table for RehiredEmployee
CREATE TABLE RehiredEmployee (
    EmployeeID VARCHAR(7) NOT NULL,
    RehiringDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    RehiringReason VARCHAR(20),
    PRIMARY KEY (EmployeeID, RehiringDate),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID) ON UPDATE CASCADE ON DELETE CASCADE
);
-- Create table for PromotionDemotion
CREATE TABLE PromotionDemotion (
    PD_ID VARCHAR(7) NOT NULL,
    EmployeeID VARCHAR(7) NOT NULL,
    Date DATETIME DEFAULT CURRENT_TIMESTAMP,
    JobFrom VARCHAR(7),
    JobTo VARCHAR(7),
    Type VARCHAR(20) NOT NULL CHECK (Type IN ('Promotion', 'Demotion')),
    PRIMARY KEY (PD_ID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID) ON UPDATE CASCADE ON DELETE NO ACTION,
    FOREIGN KEY (JobFrom) REFERENCES Jobs(JobID) ON UPDATE CASCADE ON DELETE NO ACTION,
    FOREIGN KEY (JobTo) REFERENCES Jobs(JobID) ON UPDATE CASCADE ON DELETE NO ACTION
);
-- Create table for Transfer
CREATE TABLE Transfer (
    TransferID VARCHAR(7) NOT NULL PRIMARY KEY,
    EmployeeID VARCHAR(7) NOT NULL,
    Date DATETIME DEFAULT CURRENT_TIMESTAMP,
    DepartmentTo VARCHAR(7) NOT NULL,
    DepartmentFrom VARCHAR(7) NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (DepartmentTo) REFERENCES Department(DepartmentID) ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY (DepartmentFrom) REFERENCES Department(DepartmentID) ON UPDATE NO ACTION ON DELETE NO ACTION
);
-- Create table for Payroll
CREATE TABLE Payroll (
    PayrollID VARCHAR(7) NOT NULL,
    EmployeeID VARCHAR(7) NOT NULL,
    Salary DECIMAL(10,2) NOT NULL,
    Month INT NOT NULL CHECK (Month BETWEEN 1 AND 12),
    OvertimePay DECIMAL(10,2) NOT NULL,
    TaxDeduction DECIMAL(10,2) NOT NULL,
    PenaltyDeduction DECIMAL(10,2) NOT NULL,
    TotalSalary DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (PayrollID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID) ON UPDATE CASCADE ON DELETE NO ACTION
);

-- Index for Employee table
CREATE INDEX idx_Employee_DepartmentID ON Employee(DepartmentID);
CREATE INDEX idx_Employee_JobID ON Employee(JobID);
CREATE INDEX idx_Employee_AddressID ON Employee(AddressID);

-- Index for TerminatedEmployees table
CREATE INDEX idx_TerminatedEmployees_EmployeeID ON TerminatedEmployees(EmployeeID);
-- Index for AcademicStatus table
CREATE INDEX idx_AcademicStatus_EmployeeID ON AcademicStatus(EmployeeID);
-- Index for Attendance table
CREATE INDEX idx_Attendance_EmployeeID ON Attendance(EmployeeID);
-- Index for PromotionDemotion table
CREATE INDEX idx_PromotionDemotion_EmployeeID ON PromotionDemotion(EmployeeID);
CREATE INDEX idx_PromotionDemotion_JobFrom ON PromotionDemotion(JobFrom);
CREATE INDEX idx_PromotionDemotion_JobTo ON PromotionDemotion(JobTo);
-- Index for Transfer table
CREATE INDEX idx_Transfer_EmployeeID ON Transfer(EmployeeID);
CREATE INDEX idx_Transfer_DepartmentTo ON Transfer(DepartmentTo);
CREATE INDEX idx_Transfer_DepartmentFrom ON Transfer(DepartmentFrom);
-- Index for Payroll table
CREATE INDEX idx_Payroll_EmployeeID ON Payroll(EmployeeID);


