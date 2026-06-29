# Write your MySQL query statement below

select customer_number from orders group by customer_number having count(customer_number) = (select max(cnt) from (select count(customer_number) as cnt, customer_number from orders group by customer_number) as t)

