-- 코드를 입력하세요
select distinct cart_id
from cart_products
where cart_id in (SELECT cart_id
                from CART_PRODUCTS
                where name in ('Milk')) and
    name in ('Yogurt')
order by cart_id