# Write your MySQL query statement below
SELECT 
customer_number
from Orders
Group by customer_number
order by count(*) Desc
limit 1;