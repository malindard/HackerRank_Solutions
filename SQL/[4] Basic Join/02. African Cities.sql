/*
Link: https://www.hackerrank.com/challenges/african-cities/problem?isFullScreen=true
Difficulty: easy
Max score: 10
*/

-- with MySQL
SELECT city.name FROM city, country WHERE city.countrycode = country.code AND continent = 'Africa';
