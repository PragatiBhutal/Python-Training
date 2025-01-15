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




----Promblems on the sqlbolt

-- Find the domestic and international sales for each movie 
select title, domestic_sales,international_sales
from movies
INNER join BoxOffice
ON BoxOffice.Movie_id = Movies.Id;

--Show the sales numbers for each movie that did better internationally rather than domestically 
SELECT title, domestic_sales, international_sales
FROM movies
INNER JOIN boxoffice
ON movies.id = boxoffice.movie_id
WHERE international_sales > domestic_sales;

--List all the movies by their ratings in descending order
SELECT title, rating
FROM movies
INNER  JOIN boxoffice
ON movies.id = boxoffice.movie_id
ORDER BY Rating DESC;

--Find the list of all buildings that have employees
SELECT DISTINCT building FROM employees;

--Find the list of all buildings and their capacity
select * from buildings

--List all buildings and the distinct employee roles in each building (including empty buildings)
SELECT DISTINCT building_name, role 
FROM buildings 
LEFT JOIN employees
ON building_name = building;

--Find the name and role of all employees who have not been assigned to a building 
SELECT name, role FROM employees
WHERE building IS NULL;

--Find the names of the buildings that hold no employees
SELECT DISTINCT building_name
FROM buildings 
LEFT JOIN employees
ON building_name = building
WHERE role IS NULL;

--List all movies and their combined sales in millions of dollars 
SELECT title, (domestic_sales + international_sales) / 1000000 AS gross_sales_millions FROM movies
INNER JOIN boxoffice ON movies.id = boxoffice.movie_id;

--List all movies and their ratings in percent 
SELECT title, rating * 10 AS rating_percent
FROM movies
INNER JOIN boxoffice
ON movies.id = boxoffice.movie_id;

--List all movies that were released on even number years
SELECT title, year
FROM movies
WHERE year % 2 = 0;

--Find the longest time that an employee has been at the studio
SELECT Role, MAX(years_employed) as longest_years_employed
FROM Employees;

--For each role, find the average number of years employed by employees in that role
SELECT Role, AVG(years_employed) as averrage_years_employed
FROM Employees
GROUP BY role;

--Find the total number of employee years worked in each building
SELECT building, SUM (years_employed) AS total
from Employees
GROUP BY building ;

--Find the number of Artists in the studio (without a HAVING clause) 
SELECT role, COUNT(*) as Number_of_artists
FROM employees
WHERE role = "Artist";

--Find the number of Employees of each role in the studio 
SELECT role, SUM(years_employed) AS total_years_employed
from employees
GROUP BY role
HAVING role = 'Engineer'

--Find the number of movies each director has directed 
SELECT director, COUNT(id) as total_movies_directed
FROM movies
GROUP BY director;

--Find the total domestic and international sales that can be attributed to each director
SELECT director, SUM(domestic_sales + international_sales) as total_sales
FROM movies
INNER JOIN boxoffice
ON movies.id = boxoffice.movie_id
GROUP BY director;

--Add a column named Aspect_ratio with a FLOAT data type to store the aspect-ratio each movie was released in.
ALTER TABLE Movies
ADD COLUMN Aspect_ratio FLOAT DEFAULT 1.78;

--Add another column named Language with a TEXT data type to store the language that the movie was released in. Ensure that the default for this language is English
ALTER TABLE Movies
ADD COLUMN Language text DEFAULT English;

--We've sadly reached the end of our lessons, lets clean up by removing the Movies table
DROP TABLE movies

--drop the BoxOffice table as well
DROP TABLE BoxOffice;