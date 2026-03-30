-- 코드를 입력하세요
with milk as (
select cart_id
from cart_products
where name = 'Milk'),

yogurt as (
select cart_id
from cart_products
where name = 'Yogurt')

select m.cart_id
from milk m join yogurt y on m.cart_id = y.cart_id
group by m.cart_id
order by m.cart_id