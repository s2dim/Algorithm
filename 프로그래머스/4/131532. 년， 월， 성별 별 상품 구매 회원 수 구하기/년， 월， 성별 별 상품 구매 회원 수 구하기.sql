-- 코드를 입력하세요
SELECT year(sales_date) as year, month(sales_date) as month, gender, count(distinct s.user_id) as users
from online_sale s join (select user_id, gender
                         from user_info
                         where gender is not null) i on s.user_id = i.user_id
group by year(sales_date), month(sales_date), gender
order by year, month, gender