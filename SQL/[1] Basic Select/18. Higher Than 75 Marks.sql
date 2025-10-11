/*
Link: https://www.hackerrank.com/challenges/more-than-75-marks/problem?isFullScreen=true
Difficulty: easy
Max score: 15
*/

-- with MySQL
SELECT name FROM students WHERE marks > 75 ORDER BY RIGHT(name, 3), ID;
