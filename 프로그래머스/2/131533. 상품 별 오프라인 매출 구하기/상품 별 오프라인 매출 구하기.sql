-- 코드를 입력하세요
SELECT p.product_code, (p.price * a.amount) as sales
from product p join (SELECT product_id, sum(sales_amount) as amount
                    from offline_sale
                    group by product_id) a
                    on p.product_id = a.product_id
order by sales desc, product_code