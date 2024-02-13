-- USE DATBASE OROMIYA_INVESTMENT_HRMS;

--EmployeeDetailsView
CREATE VIEW EmployeeDetailsView AS
SELECT 
    e.EmployeeID, 
    e.EmpName, 
    e.Gender, 
    e.DOB, 
    e.Age, 
    e.PhoneNo, 
    d.DepartmentName, 
    j.JobName, 
    j.Salary,
    a.City,
    a.Subcity,
    a.Woreda,
    a.Kebele
FROM 
    Employee e
    LEFT JOIN Department d ON e.DepartmentID = d.DepartmentID
    LEFT JOIN Jobs j ON e.JobID = j.JobID
    LEFT JOIN Address a ON e.AddressID = a.AddressID;
GO

--TerminatedEmployeesView
CREATE VIEW TerminatedEmployeesView AS
SELECT 
    t.TerminationID,
    t.TerminationDate,
    t.TerminationReason,
    e.EmployeeID,
    e.EmpName,
    e.Gender,
    e.DOB,
    e.Age,
    e.PhoneNo
FROM 
    TerminatedEmployees t
    INNER JOIN Employee e ON t.EmployeeID = e.EmployeeID;
GO

--PayrollSummaryView
CREATE VIEW PayrollSummaryView AS
SELECT 
    p.EmployeeID,
    e.EmpName,
    p.TotalSalary,
    p.Month
FROM 
    Payroll p
    INNER JOIN Employee e ON p.EmployeeID = e.EmployeeID;
GO

--EmployeeAttendanceView
CREATE VIEW EmployeeAttendanceView AS
SELECT 
    a.EmployeeID,
    a.Month,
    a.totalDaysPresent,
    a.allowedBreaks,
    a.totalDaysAbsent,
    e.EmpName
FROM 
    Attendance a
    INNER JOIN Employee e ON a.EmployeeID = e.EmployeeID;
GO

