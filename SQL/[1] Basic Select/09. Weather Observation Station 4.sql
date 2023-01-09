/*
Link: https://www.hackerrank.com/challenges/weather-observation-station-4/problem?isFullScreen=true
Difficulty: easy
Max score: 10
*/

SELECT COUNT(city)-COUNT(DISTINCT city) FROM station;
