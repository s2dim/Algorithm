-- 코드를 입력하세요
SELECT year, month, gender, count(users) as users
from (SELECT distinct s.user_id as users, year(sales_date) as year, month(sales_date) as month, gender
        from online_sale s join user_info i on s.user_id = i.user_id
        where gender is not null) as t
group by year, month, gender
order by year, month, gender




