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
