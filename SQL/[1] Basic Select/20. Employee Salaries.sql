/*
Link: https://www.hackerrank.com/challenges/salary-of-employees/problem?isFullScreen=true
Difficulty: easy
Max score: 10
*/

-- with MySQL
SELECT name FROM employee 
WHERE salary > 2000 AND months < 10 
ORDER BY employee_id;
