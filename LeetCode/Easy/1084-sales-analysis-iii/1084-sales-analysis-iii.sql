# Write your MySQL query statement below

select distinct s.product_id, p.product_name
from sales s join product p on s.product_id = p.product_id
where s.product_id in (select product_id
                    from sales
                    where sale_date >= '2019-01-01' and sale_date <= '2019-03-31') and
    s.product_id not in (select product_id
                        from sales
                        where sale_date < '2019-01-01' or sale_date > '2019-03-31')
                    