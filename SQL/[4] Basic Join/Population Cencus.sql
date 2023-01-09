/*
Link: https://www.hackerrank.com/challenges/asian-population/problem?isFullScreen=true
Difficulty: easy
Max score: 10
*/

-- with MySQL
SELECT SUM(CITY.population) FROM CITY 
JOIN COUNTRY ON CITY.countrycode = COUNTRY.code 
WHERE COUNTRY.continent = 'Asia';

-- or this (with MySQL)
SELECT SUM(CITY.population) FROM CITY, COUNTRY
WHERE CITY.countrycode = COUNTRY.code AND COUNTRY.continent = 'Asia';
