/*
Link: https://www.hackerrank.com/challenges/weather-observation-station-11/problem?isFullScreen=true
Difficulty: easy
Max score: 15
*/

-- with MySQL
SELECT DISTINCT city
FROM station
WHERE NOT (city LIKE 'A%' OR city LIKE 'E%' OR city LIKE 'I%' OR city LIKE 'O%' OR city LIKE 'U%')
OR 
NOT (city LIKE '%A' OR city LIKE '%E' OR city LIKE '%I' OR city LIKE '%O' OR city LIKE '%U');

-- or this (with MySQL)
SELECT DISTINCT city FROM station 
WHERE LEFT(city,1) NOT IN ('a','e','i','o','u') 
OR 
RIGHT(city,1) NOT IN ('a','e','i','o','u');


'''
right() : function extracts a number of characters from a string (starting from right)
left() : starting from right
Syntax: RIGHT(string, number_of_chars), LEFT(string, number_of_chars)
'''
