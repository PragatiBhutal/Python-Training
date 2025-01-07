/* The CITY table is described as follows:
ID - NUMBER
NAME - VARCHAR(17)
COUNTRYCODE - VARCHAR(3)
DISTRICT - VARCHAR(20)
POPULATION -NUMBER */


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
