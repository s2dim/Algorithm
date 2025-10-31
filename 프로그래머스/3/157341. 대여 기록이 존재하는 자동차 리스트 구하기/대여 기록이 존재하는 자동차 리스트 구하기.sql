-- 코드를 입력하세요
SELECT distinct(c.car_id)
from car_rental_company_car c
left join car_rental_company_rental_history h on c.car_id = h.car_id
where c.car_type = '세단' and start_date >= "2022-10-01" and start_date <= "2022-10-30"
order by c.car_id desc