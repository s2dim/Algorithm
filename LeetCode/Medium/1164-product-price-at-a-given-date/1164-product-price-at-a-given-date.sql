# Write your MySQL query statement below

-- select product_id, new_price as price, change_date
-- from products
-- where change_date < '2019-08-17'
-- group by product_id

with newest as (
    select product_id, new_price, row_number() over (partition by product_id order by change_date desc) as fast
    from products
    where change_date < '2019-08-17'
    order by fast desc

)

-- select p.product_id, ifnull(p.new_price, 10) as price
-- from products p left join newest n on p.product_id = n.product_id and p.new_price = n.new_price
-- where n.fast = 1 or n.fast is null

select p.product_id, ifnull(n.new_price, 10) as price
from (select product_id
        from products
        group by product_id) p left join newest n on p.product_id = n.product_id
where n.fast = 1 or n.fast is null