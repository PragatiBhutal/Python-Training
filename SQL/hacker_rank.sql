-- Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.
SELECT * 
FROM CITY
WHERE CountryCode = 'USA' AND Population > 100000;

-- Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA
SELECT NAME
FROM CITY
WHERE CountryCode = 'USA' AND Population > 120000;

-- Query all columns (attributes) for every row in the CITY table.
SELECT * 
FROM CITY;

-- Query all columns for a city in CITY with the ID 1661.
select * 
from CITY
where ID = 1661;

-- Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
SELECT Name
FROM CITY
WHERE CountryCode = 'JPN';

--Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.
select sum(CITY.population) AS populations
from CITY
INNER JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
where COUNTRY.CONTINENT = 'Asia'

--Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.
select CITY.NAME from CITY
INNER JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
where COUNTRY.CONTINENT = 'Africa'

--Query a count of the number of cities in CITY having a Population larger than 100000.
SELECT COUNT(*) AS NumberOfCities
FROM CITY
WHERE Population > 100000;

--Query the total population of all cities in CITY where District is California.
SELECT SUM(Population) AS TotalPopulation
FROM CITY
WHERE District = 'California';

--Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. Ketty doesn't want the NAMES of those students who received a grade lower than 8. The report must be in descending order by grade -- i.e. higher grades are entered first. If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.

SELECT 
    IF(g.Grade >= 8, s.Name, 'NULL') AS Name,
    g.Grade,
    s.Marks
FROM Students s
INNER JOIN Grades g
ON s.Marks BETWEEN g.Min_Mark AND g.Max_Mark
ORDER BY 
    g.Grade DESC, 
    (g.Grade >= 8) DESC,  
    Name ASC,             
    Marks ASC;  

--Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

-- Equilateral: It's a triangle with  sides of equal length.
-- Isosceles: It's a triangle with  sides of equal length.
-- Scalene: It's a triangle with  sides of differing lengths.
-- Not A Triangle: The given values of A, B, and C don't form a triangle.
-- Input Format

-- The TRIANGLES table is described as follows:

SELECT 
    CASE 
        WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
        WHEN A = B AND B = C THEN 'Equilateral'
        WHEN A = B OR A = C OR B = C THEN 'Isosceles'
        ELSE 'Scalene'
    END AS TriangleType
FROM TRIANGLES;


--Query the average population of all cities in CITY where District is California.

-- Input Format

-- The CITY table is described as follows: CITY.jpg
SELECT AVG(Population) AS AveragePopulation
FROM CITY
WHERE District = 'California';

-- Query the average population for all cities in CITY, rounded down to the nearest integer.
SELECT FLOOR(AVG(city.population)) FROM city;

--Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.
SELECT SUM(Population) AS TotalPopulation
FROM CITY
WHERE CountryCode = 'JPN';

--Query the difference between the maximum and minimum populations in CITY.
SELECT MAX(Population) - MIN(Population) AS PopulationDifference
FROM CITY;

--We define an employee's total earnings to be their monthly salary * months  worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as  space-separated integers.
SELECT 
    MAX(months * salary) AS MaxEarnings,
    COUNT(*) AS EmployeeCount
FROM Employee
WHERE months * salary = (SELECT MAX(months * salary) FROM Employee);

--Query the following two values from the STATION table:

-- The sum of all values in LAT_N rounded to a scale of  decimal places.
-- The sum of all values in LONG_W rounded to a scale of  decimal places.
SELECT 
    ROUND(SUM(LAT_N), 2) AS SumLatitude,
    ROUND(SUM(LONG_W), 2) AS SumLongitude
FROM STATION;

--Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345 . Truncate your answer to 4  decimal places.
SELECT TRUNCATE(MAX(LAT_N), 4) AS Greatest_Latitude
FROM STATION
WHERE LAT_N < 137.2345;

--Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137.2345 . Round your answer to 4  decimal places.
SELECT ROUND(LONG_W, 4) AS Longitude_for_Largest_Latitude
FROM STATION
WHERE LAT_N = (SELECT MAX(LAT_N) 
               FROM STATION 
               WHERE LAT_N < 137.2345);


--Query the smallest Northern Latitude (LAT_N) from STATION that is greater than 38.7780 . Round your answer to  4 decimal places.
SELECT ROUND(MIN(LAT_N), 4) AS Smallest_Latitude
FROM STATION
WHERE LAT_N > 38.7780;

--Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than 38.7780 . Round your answer to 4 decimal places
SELECT ROUND(LONG_W, 4) AS Longitude_for_Smallest_Latitude
FROM STATION
WHERE LAT_N = (SELECT MIN(LAT_N) 
               FROM STATION 
               WHERE LAT_N > 38.7780);



--P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

-- * * * * * 
-- * * * * 
-- * * * 
-- * * 
-- *
-- Write a query to print the pattern P(20).

DELIMITER $$
CREATE PROCEDURE print_reverse_pattern()
BEGIN
    DECLARE i INT DEFAULT 20;
        WHILE i >= 1 DO
        SELECT REPEAT('* ', i); 
        SET i = i - 1; 
    END WHILE;
END $$

DELIMITER ;
CALL print_reverse_pattern();
 


--P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

-- * 
-- * * 
-- * * * 
-- * * * * 
-- * * * * *
-- Write a query to print the pattern P(20).

DELIMITER $$
CREATE PROCEDURE print_pattern()
BEGIN
    DECLARE i INT DEFAULT 1;
        WHILE i <= 20 DO
        SELECT REPEAT('* ', i);
        SET i = i + 1;
    END WHILE;
END $$

DELIMITER ;
CALL print_pattern();
