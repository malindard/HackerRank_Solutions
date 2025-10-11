/*
Link: https://www.hackerrank.com/challenges/weather-observation-station-8/problem?isFullScreen=true
Difficulty: easy
Max score: 15
*/

-- with MS SQL Server
SELECT DISTINCT city FROM station WHERE city LIKE '%[aiueo]' and city LIKE '[aiueo]%';

-- with MySQL
SELECT DISTINCT CITY FROM STATION 
WHERE (CITY LIKE 'a%' OR CITY LIKE 'e%' OR CITY LIKE 'i%' OR CITY LIKE 'o%' OR CITY LIKE 'u%') 
AND 
(CITY LIKE '%a' OR CITY LIKE '%e' OR CITY LIKE '%i' OR CITY LIKE '%o' OR CITY LIKE '%u');
