-- 코드를 입력하세요
SELECT
    car_id,
    CASE
        WHEN SUM(CASE
                     WHEN '2022-10-16' BETWEEN start_date AND end_date THEN 1
                     ELSE 0
                 END) > 0 THEN '대여중'
        ELSE '대여 가능'
    END AS availability
FROM car_rental_company_rental_history
GROUP BY car_id
ORDER BY car_id DESC;