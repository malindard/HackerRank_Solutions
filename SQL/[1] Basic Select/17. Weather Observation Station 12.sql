/*
Link: https://www.hackerrank.com/challenges/weather-observation-station-11/problem?isFullScreen=true
Difficulty: easy
Max score: 15
*/

-- with MySQL
SELECT DISTINCT city
FROM station
WHERE NOT (city LIKE 'A%' OR city LIKE 'E%' OR city LIKE 'I%' OR city LIKE 'O%' OR city LIKE 'U%')
AND 
NOT (city LIKE '%A' OR city LIKE '%E' OR city LIKE '%I' OR city LIKE '%O' OR city LIKE '%U');

-- or this (with MySQL)
SELECT DISTINCT city FROM station 
WHERE LEFT(city,1) NOT IN ('a','e','i','o','u') 
AND 
RIGHT(city,1) NOT IN ('a','e','i','o','u');
