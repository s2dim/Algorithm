-- 코드를 입력하세요
SELECT *
from food_product
where price in (SELECT max(price)
                from food_product) 