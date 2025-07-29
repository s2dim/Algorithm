-- 코드를 입력하세요
select month(start_date) as month, car_id, count(car_id) as records
from car_rental_company_rental_history
where car_id in (SELECT car_id
                from car_rental_company_rental_history
                where (start_date) between '2022-08-01' and '2022-10-31'
                group by car_id
                having count(car_id) >= 5) and (start_date) between '2022-08-01' and '2022-10-31'
group by month(start_date), car_id
order by month, car_id desc

# SELECT car_id
# from car_rental_company_rental_history
# where (start_date) between '2022-08-01' and '2022-10-31'
# group by car_id
# having count(car_id) >= 5