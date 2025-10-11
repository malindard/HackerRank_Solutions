/*
Link: https://www.hackerrank.com/challenges/weather-observation-station-9/problem?isFullScreen=true
Difficulty: easy
Max score: 10
*/

-- with MySQL
SELECT DISTINCT city
FROM station
WHERE NOT (city LIKE 'A%' OR city LIKE 'E%' OR city LIKE 'I%' OR city LIKE 'O%' OR city LIKE 'U%');
