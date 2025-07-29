-- 코드를 입력하세요
# select year(sales_date) as year, month(sales_date) as month, user_id
# from online_sale
# group by year(sales_date), month(sales_date), user_id

# select s.year, s.month, count(i.gender) as gender, count(i.user_id) as users
select year, month, gender, count(i.user_id) as users
from user_info i
join (select year(sales_date) as year, month(sales_date) as month, user_id
      from online_sale
      group by year(sales_date), month(sales_date), user_id) s
on i.user_id = s.user_id
where i.gender is not null
group by year, month, gender
order by year, month, gender