# Write your MySQL query statement below
SElECT class
From  Courses
GROUP BY class
HAVING count(*) >= 5;

