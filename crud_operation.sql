USE OROMIYA_INVESTMENT_HRMS;


INSERT INTO Jobs (JobID, JobName, JobDescription, Salary, Rank) VALUES
('JOB001', 'Software Engineer', 'Develop software applications', 60000, 3),
('JOB002', 'Database Administrator', 'Manage and maintain databases', 65000, 2),
('JOB003', 'Network Administrator', 'Manage and maintain network infrastructure', 62000, 2),
('JOB004', 'System Analyst', 'Analyze and design information systems', 68000, 3),
('JOB005', 'Web Developer', 'Develop websites and web applications', 58000, 2),
('JOB006', 'Business Analyst', 'Analyze business processes and requirements', 70000, 3),
('JOB007', 'Project Manager', 'Manage projects and project teams', 75000, 4),
('JOB008', 'Quality Assurance Engineer', 'Test software for defects and quality', 62000, 2),
('JOB009', 'Technical Support Specialist', 'Provide technical support to end-users', 55000, 1),
('JOB010', 'Data Scientist', 'Analyze and interpret complex data sets', 72000, 3);


INSERT INTO Department (DepartmentID, DepartmentName) VALUES
('DEP001', 'Finance'),
('DEP002', 'Human Resources'),
('DEP003', 'Sales'),
('DEP004', 'Customer Service'),
('DEP005', 'Research and Development')


INSERT INTO Address (AddressID, City, Subcity, Woreda, Kebele) VALUES
('ADD001', 'Addis Ababa', 'Kirkos', 4, 12),
('ADD002', 'Addis Ababa', 'Bole', 3, 9),
('ADD003', 'Dire Dawa', 'Kezira', 2, 7),
('ADD004', 'Gondar', 'Janmeda', 5, 14),
('ADD005', 'Hawassa', 'Sidist Kilo', 3, 8),
('ADD006', 'Jimma', 'Limmu', 4, 11),
('ADD007', 'Mekelle', 'Semien', 6, 15),
('ADD008', 'Bahir Dar', 'Abay', 4, 10),
('ADD009', 'Adama', 'Kombolcha', 3, 9),
('ADD010', 'Axum', 'Yeha', 2, 6);

-- Sample data for Employee table
INSERT INTO Employee (EmployeeID, EmpName, Gender, DOB, DOE, Age, PhoneNo, Status, DepartmentID, JobID, AddressID, TaxPayerTinNo) VALUES
('EMP001', 'John Doe', 'M', '1990-05-15', '2022-01-01', 31, '1234567890', 'Available', 'DEP001', 'JOB001', 'ADD001', '1234567890A'),
('EMP002', 'Jane Smith', 'F', '1992-08-20', '2022-02-15', 29, '2345678901', 'Available', 'DEP002', 'JOB002', 'ADD002', '2345678901B'),
('EMP003', 'Michael Johnson', 'M', '1988-03-10', '2022-03-20', 33, '3456789012', 'Available', 'DEP003', 'JOB003', 'ADD003', '3456789012C'),
('EMP004', 'Emily Brown', 'F', '1995-11-25', '2022-04-25', 26, '4567890123', 'Available', 'DEP004', 'JOB004', 'ADD004', '4567890123D'),
('EMP005', 'David Williams', 'M', '1991-09-05', '2022-05-30', 30, '5678901234', 'Available', 'DEP005', 'JOB005', 'ADD005', '5678901234E'),
('EMP006', 'Sarah Davis', 'F', '1987-07-18', '2022-06-10', 34, '6789012345', 'Available', 'DEP001', 'JOB006', 'ADD006', '6789012345F'),
('EMP007', 'Matthew Wilson', 'M', '1993-02-28', '2022-07-15', 29, '7890123456', 'Available', 'DEP002', 'JOB007', 'ADD007', '7890123456G'),
('EMP008', 'Olivia Martinez', 'F', '1989-12-12', '2022-08-20', 32, '8901234567', 'Available', 'DEP003', 'JOB008', 'ADD008', '8901234567H'),
('EMP009', 'Daniel Anderson', 'M', '1994-04-08', '2022-09-25', 27, '9012345678', 'Available', 'DEP002', 'JOB009', 'ADD009', '9012345678I'),
('EMP010', 'Sophia Taylor', 'F', '1990-10-30', '2022-10-30', 31, '0123456789', 'Available', 'DEP001', 'JOB010', 'ADD010', '0123456789J');

-- Sample data for TerminatedEmployees table
INSERT INTO TerminatedEmployees (TerminationID, TerminationDate, TerminationReason, EmployeeID) VALUES
('TER001', '2022-05-31', 'Resigned', 'EMP001'),
('TER002', '2022-06-30', 'Laid Off', 'EMP002'),
('TER003', '2022-07-31', 'Contract Ended', 'EMP003'),
('TER009', '2023-01-31', 'Retired', 'EMP009'),
('TER010', '2023-02-28', 'Terminated', 'EMP010');

-- Sample data for AcademicStatus table
INSERT INTO AcademicStatus (EmployeeID, CertificationName, InstitutionName) VALUES
('EMP001', 'BS in Computer Science', 'University of XYZ'),
('EMP002', 'MBA', 'ABC University'),
('EMP003', 'Bachelor of Commerce', 'University of DEF'),
('EMP004', 'MS in Information Systems', 'GHI University'),
('EMP005', 'BA in Marketing', 'JKL University'),
('EMP006', 'MA in Industrial Engineering', 'MNO University'),
('EMP007', 'BS Project Management', 'PQR College'),
('EMP008', 'Bachelor of HRMt', 'STU University'),
('EMP009', 'MS in Chemistry', 'VWX University'),
('EMP010', 'BS in Biology', 'YZA University');

-- Sample data for Attendance table
INSERT INTO Attendance (EmployeeID, Month, totalDaysPresent, allowedBreaks, totalDaysAbsent) VALUES
('EMP001', 1, 20, 5, 2),
('EMP001', 2, 22, 6, 0),
('EMP002', 3, 18, 4, 4),
('EMP002', 4, 21, 5, 3),
('EMP004', 5, 20, 5, 2),
('EMP003', 6, 22, 6, 0),
('EMP004', 7, 18, 4, 4),
('EMP003', 8, 21, 5, 3),
('EMP001', 9, 20, 5, 2),
('EMP010', 10, 22, 6, 0);

-- Sample data for RehiredEmployee table
INSERT INTO RehiredEmployee (EmployeeID, RehiringDate, RehiringReason) VALUES
('EMP002', '2022-06-01', 'New Position'),
('EMP003', '2022-07-01', 'Contract Renewal'),
('EMP010', '2023-02-01', 'Rehired Again');

-- Sample data for PromotionDemotion table
INSERT INTO PromotionDemotion (PD_ID, EmployeeID, Date, JobFrom, JobTo, Type) VALUES
('PD001', 'EMP002', '2022-06-01', 'JOB002', 'JOB003', 'Promotion'),
('PD002', 'EMP003', '2022-07-01', 'JOB003', 'JOB004', 'Promotion'),
('PD004', 'EMP005', '2022-09-01', 'JOB005', 'JOB006', 'Promotion'),
('PD007', 'EMP008', '2022-12-01', 'JOB008', 'JOB009', 'Promotion'),
('PD008', 'EMP009', '2023-01-01', 'JOB009', 'JOB010', 'Promotion'),
('PD009', 'EMP010', '2023-02-01', 'JOB010', 'JOB001', 'Demotion');

-- Sample data for Transfer table
INSERT INTO Transfer (TransferID, EmployeeID, Date, DepartmentTo, DepartmentFrom) VALUES
('TR001', 'EMP002', '2022-06-01', 'DEP004', 'DEP002'),
('TR002', 'EMP003', '2022-07-01', 'DEP004', 'DEP003'),
('TR003', 'EMP005', '2022-09-01', 'DEP004', 'DEP005'),
('TR004', 'EMP010', '2023-02-01', 'DEP001', 'DEP005');

-- Sample data for Payroll table
INSERT INTO Payroll (PayrollID, EmployeeID, Salary, Month, OvertimePay, TaxDeduction, PenaltyDeduction, TotalSalary) VALUES
('PAY001', 'EMP002', 65000, 1, 1500, 5000, 0, 69000),
('PAY002', 'EMP003', 62000, 1, 1200, 4800, 0, 66000),
('PAY003', 'EMP004', 68000, 1, 1800, 5500, 0, 71300),
('PAY004', 'EMP005', 58000, 1, 1000, 4500, 0, 62500),
('PAY005', 'EMP006', 70000, 1, 2000, 6000, 0, 76000),
('PAY006', 'EMP007', 75000, 1, 2500, 6500, 0, 84000),
('PAY007', 'EMP008', 62000, 1, 1200, 4800, 0, 66000),
('PAY008', 'EMP009', 55000, 1, 800, 4000, 0, 58800),
('PAY009', 'EMP010', 72000, 1, 2200, 6200, 0, 78500);



SELECT JobName, Salary FROM Jobs;

SELECT * FROM Department;

SELECT * FROM Address;

SELECT Employee.*, Department.DepartmentName
FROM Employee
LEFT JOIN Department ON Employee.DepartmentID = Department.DepartmentID;

SELECT * FROM TerminatedEmployees;

SELECT * FROM AcademicStatus;

SELECT * FROM Attendance;

SELECT * FROM RehiredEmployee;

SELECT * FROM PromotionDemotion;

SELECT * FROM Transfer;

SELECT * FROM Payroll;

SELECT Employee.*, Jobs.JobName, Jobs.Salary
FROM Employee
LEFT JOIN Jobs ON Employee.JobID = Jobs.JobID;

/*Codes to demonstrate updating*/

UPDATE Jobs  SET Salary = 65000
WHERE JobID = 'JOB000001';

UPDATE Jobs  SET Rank = 4
WHERE JobID = 'JOB000002';

UPDATE Department
SET DepartmentName = 'Information Technology'
WHERE DepartmentID = 'DEP000001';

UPDATE Department
SET DepartmentName = 'Finance Department'
WHERE DepartmentID = 'DEP000002';

UPDATE Address
SET City = 'New York'
WHERE AddressID = 'ADD000001';

UPDATE Address
SET City = 'Los Angeles'
WHERE AddressID = 'ADD000002';

UPDATE Employee
SET Status = 'Terminated'
WHERE EmployeeID = 'EMP000001';

UPDATE Employee
SET Age = 30
WHERE EmployeeID = 'EMP000002';

UPDATE TerminatedEmployees
SET TerminationReason = 'End of Contract'
WHERE TerminationID = 'TERM000001';

UPDATE TerminatedEmployees
SET TerminationReason = 'Performance Issues'
WHERE TerminationID = 'TERM000002';


UPDATE AcademicStatus
SET InstitutionName = 'University of ABC'
WHERE EmployeeID = 'EMP000001' AND CertificationName = 'Bachelor of Science in Computer Science';

UPDATE AcademicStatus
SET CertificationName = 'Master of Business Administration'
WHERE EmployeeID = 'EMP000002';


UPDATE Attendance
SET totalDaysPresent = 25
WHERE EmployeeID = 'EMP000001' AND Month = 1;

UPDATE Attendance
SET totalDaysAbsent = 5
WHERE EmployeeID = 'EMP000002' AND Month = 1;

UPDATE RehiredEmployee
SET RehiringReason = 'New Project Assignment'
WHERE EmployeeID = 'EMP000001';

UPDATE RehiredEmployee
SET RehiringReason = 'Return from Sabbatical'
WHERE EmployeeID = 'EMP000002';
Update records in the PromotionDemotion table:

UPDATE PromotionDemotion  SET Type = 'Demotion'
WHERE PD_ID = 'PD000001';

UPDATE PromotionDemotion  SET Date = '2022-07-01'
WHERE PD_ID = 'PD000002';

UPDATE Transfer  SET DepartmentTo = 'DEP000002'
WHERE TransferID = 'TR000001';

UPDATE Transfer  SET DepartmentFrom = 'DEP000001'
WHERE TransferID = 'TR000002';

UPDATE Payroll  SET OvertimePay = 2000
WHERE PayrollID = 'PAY000001';

UPDATE Payroll
SET TotalSalary = 68000
WHERE PayrollID = 'PAY000002';

/*Code to demonstrate the deletion of some of the records*/
DELETE FROM Jobs WHERE JobID IN ('JOB001', 'JOB002', 'JOB003');
DELETE FROM Department WHERE DepartmentID IN ('DEP001', 'DEP002', 'DEP003');
DELETE FROM Address WHERE AddressID IN ('ADD001', 'ADD002', 'ADD003');
DELETE FROM Employee WHERE EmployeeID IN ('EMP001', 'EMP002', 'EMP003');
DELETE FROM TerminatedEmployees WHERE TerminationID IN ('TER001', 'TER002', 'TER003');
DELETE FROM AcademicStatus WHERE EmployeeID IN ('EMP001', 'EMP002', 'EMP003');
DELETE FROM Attendance WHERE EmployeeID IN ('EMP001', 'EMP002', 'EMP003');
DELETE FROM RehiredEmployee WHERE EmployeeID IN ('EMP001', 'EMP002', 'EMP003');
DELETE FROM PromotionDemotion WHERE PD_ID IN ('PD001', 'PD002', 'PD003');
DELETE FROM Transfer WHERE TransferID IN ('TR001', 'TR002', 'TR003');
DELETE FROM Payroll WHERE PayrollID IN ('PAY001', 'PAY002', 'PAY003');


