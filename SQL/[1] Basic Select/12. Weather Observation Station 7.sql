/*
Link: https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true
Difficulty: easy
Max score: 10
*/

-- with MS SQL Server
SELECT DISTINCT city FROM station WHERE city LIKE '%[aiueo]';

-- with MySQL
SELECT DISTINCT city FROM station
WHERE city LIKE '%a' or city LIKE '%i' or city LIKE '%u' or city LIKE '%e' or city LIKE '%o';
