# Write your MySQL query statement below

with first as(
    select product_id, year, rank() over (partition by product_id order by year) as row_year, quantity, price
    from sales
)

select product_id, year as first_year, quantity, price
from first
where row_year = 1
