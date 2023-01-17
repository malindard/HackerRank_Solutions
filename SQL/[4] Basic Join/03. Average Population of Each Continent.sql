/*
Link: https://www.hackerrank.com/challenges/average-population-of-each-continent/problem?isFullScreen=true
Difficulty: easy
Max score: 10
*/

-- with MySQL
SELECT COUNTRY.continent, FLOOR(AVG(CITY.population)) FROM CITY, COUNTRY WHERE CITY.countrycode = COUNTRY.code GROUP BY COUNTRY.continent;
