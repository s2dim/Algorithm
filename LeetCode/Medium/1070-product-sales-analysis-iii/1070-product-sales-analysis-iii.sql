# Write your MySQL query statement below

select s.product_id, t.year as first_year, s.quantity as quantity, s.price as price
from sales s join (select product_id, min(year) as year
                    from sales
                    group by product_id) t on s.product_id = t.product_id and s.year = t.year
