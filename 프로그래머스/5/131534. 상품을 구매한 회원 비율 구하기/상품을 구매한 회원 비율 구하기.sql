-- 코드를 입력하세요
# 2021년에 가입한 회원

with join2021 as(
    select user_id
    from user_info
    where year(joined) = '2021'
    )
    
select year(sales_date) as year, month(sales_date) as month, count(distinct o.user_id) as purchased_users, round(count(distinct o.user_id) / (select count(*) from join2021), 1) as puchased_ratio
from online_sale o join join2021 j on o.user_id = j.user_id
group by year, month
order by year, month

