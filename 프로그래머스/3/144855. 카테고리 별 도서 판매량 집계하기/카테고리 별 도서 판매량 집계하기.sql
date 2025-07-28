-- 코드를 입력하세요
SELECT category, sum(sales) as total_sales
from book as b inner join book_sales as s on b.book_id = s.book_id
where year(sales_date) = '2022' and month(sales_date) = '01'
group by category
order by category