-- 코드를 입력하세요
SELECT left(product_code, 2) as category, count(left(product_code, 2)) as products
from product
group by category
order by product_code