/*
Link: https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true
Difficulty: easy
Max score: 30
Skills: SQL Intermediate
*/

SELECT city, LENGTH(city) FROM station
ORDER BY LENGTH(city), city
LIMIT 1;

SELECT city, LENGTH(city) FROM station
ORDER BY LENGTH(city) DESC, city
LIMIT 1;

/*
ORDER BY : to sort the result-set in ascending(ASC) or descending(DESC) order of columns
LIMIT : used to specify the number of records to return
*/
