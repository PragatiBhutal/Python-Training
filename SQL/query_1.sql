-- EMPLOYEE Table
--  ID   Name        Age  Department      Salary   CountryCode 
--  101  Alice       28   IT              60000    USA         
--  102  Bob         35   HR              50000    USA         
--  103  Charlie     40   IT              70000    UK          
--  104  Diana       30   Finance         55000    USA         
--  105  Ethan       45   IT              80000    JPN         
--  106  Fiona       25   HR              45000    USA         
--  107  George      29   Finance         58000    UK          
--  108  Helen       38   IT              75000    USA         
--  109  Ivan        32   IT              72000    JPN         
--  110  Julia       33   HR              52000    UK          

-- Select all columns for all employees in the table.
SELECT * 
FROM EMPLOYEE;

-- Select the `Name` and `Age` of all employees.
SELECT Name, Age 
FROM EMPLOYEE;

-- Select the details of employees who work in the HR department.
SELECT * 
FROM EMPLOYEE
WHERE Department = 'HR';

-- Select the names of employees whose salary is greater than 50,000.
SELECT Name 
FROM EMPLOYEE
WHERE Salary > 50000;

-- Select the `Name` and `Salary` of employees working in the Finance department and earning more than 55,000.
SELECT Name, Salary 
FROM EMPLOYEE
WHERE Department = 'Finance' AND Salary > 55000;

--Select all employees who work in either the IT or HR department.
SELECT * 
FROM EMPLOYEE
WHERE Department = 'IT' OR Department = 'HR';

--Select the distinct departments from the table.
SELECT DISTINCT Department 
FROM EMPLOYEE;

--Select the `Name` and `Age` of employees who are younger than 30.
SELECT Name, Age 
FROM EMPLOYEE
WHERE Age < 30;

-- Select all columns for employees whose name starts with the letter 'J'.
SELECT * 
FROM EMPLOYEE
WHERE Name LIKE 'J%';

-- Select the `Name`, `Department`, and `Salary` of employees who earn between 50,000 and 75,000.
SELECT Name, Department, Salary 
FROM EMPLOYEE
WHERE Salary BETWEEN 50000 AND 75000;

--all employees ordered by their Salary in descending order
SELECT * FROM EMPLOYEE
ORDER BY Salary DESC;

--To list unique departments from the EMPLOYEE table:
SELECT DISTINCT Department FROM EMPLOYEE;

--To get the top 3 highest-paid employees:
SELECT * FROM EMPLOYEE
ORDER BY Salary DESC
LIMIT 3;

--To get the next 3 highest-paid employees after skipping the top 3:
SELECT * FROM EMPLOYEE
ORDER BY Salary DESC
LIMIT 3 OFFSET 3;
