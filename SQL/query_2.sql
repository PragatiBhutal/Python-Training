-- Table 1: Employees
-- emp_no	emp_name	    dept_no
-- E1	    Varun Singhal	D1
-- E2	    Amrita Aggarwal	D2
-- E3	    Ravi Anand	    D3
-- E4	    Akas Das	    D5
-- E5	    Neha Sharma	    D4
-- E6	    Arun Kumar	    D1


-- Table 2: Departments
-- dept_no	d_name	    location
-- D1	    IT	        Delhi
-- D2	    HR	        Hyderabad
-- D3	    Finance	    Pune
-- D4	    Testing	    Noida
-- D5	    Marketing	Delhi

-- List the employee number, name, department name, and location for all employees.
SELECT emp_no, emp_name, d_name, location
FROM Employees
INNER JOIN Departments
ON Employees.dept_no = Departments.dept_no;

-- List all employees working in the IT department, showing their names and employee numbers.
SELECT emp_no, emp_name
FROM Employees
INNER JOIN Departments
ON Employees.dept_no = Departments.dept_no
WHERE d_name = 'IT';

-- Find all employees who are not assigned to any department.
SELECT emp_no, emp_name
FROM Employees
LEFT JOIN Departments
ON Employees.dept_no = Departments.dept_no
WHERE d_name IS NULL;

-- Show all departments that do not have any employees assigned to them.
SELECT d_name, location
FROM Departments
LEFT JOIN Employees
ON Departments.dept_no = Employees.dept_no
WHERE emp_no IS NULL;

-- List all departments along with their employees, even if there are no employees in some departments.
SELECT d_name, emp_name
FROM Departments
LEFT JOIN Employees
ON Departments.dept_no = Employees.dept_no;

--List all employees ordered by their names in ascending order.
SELECT emp_no, emp_name
FROM Employees
ORDER BY emp_name ASC;

-- List all unique department names.
SELECT DISTINCT d_name
FROM Departments;

-- Count how many employees are in each department.
SELECT dept_no, COUNT(emp_no) AS employee_count
FROM Employees
GROUP BY dept_no;


-- Find the employee number, name, and department location for employees who work in departments located in Delhi.
SELECT emp_no , emp_name, location
FROM Employees
INNER JOIN  Departments
ON Employees.dept_no = Departments.dept_no
where location = 'Delhi';

--Add a new employee to the Employees table
INSERT INTO Employees (emp_no, emp_name, dept_no)
VALUES ('E7', 'Rajesh Mehta', 'D3');

--Add a new department to the Departments table
INSERT INTO Departments (dept_no, d_name, location)
VALUES ('D6', 'Operations', 'Mumbai');

--Remove an employee from the Employees table based on their employee number
DELETE FROM Employees
WHERE emp_no = 'E4';

-- Delete a department from the Departments table
DELETE FROM Departments
WHERE dept_no = 'D5';

--Update the department of an employee in the Employees table.
UPDATE Employees
SET dept_no = 'D2'
WHERE emp_no = 'E3';

--Change the location of a department in the Departments table.
UPDATE Departments
SET location = 'Chennai'
WHERE dept_no = 'D1';

--Drop table Employees
DROP Table Employees

--Drop table Departments
DROP Table Departments



