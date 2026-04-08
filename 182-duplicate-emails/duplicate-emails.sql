# Write your MySQL query statement below

select distinct email as Email 
from(
select id, 
email,
row_number () over(partition by email) as rn
from person
) as s
where
rn >1;