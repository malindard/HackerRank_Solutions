/*
Link: https://www.hackerrank.com/challenges/weather-observation-station-3/problem?isFullScreen=true
Difficulty: easy
Max score: 10
*/

SELECT DISTINCT city FROM station 
WHERE mod(id, 2) = 0;
