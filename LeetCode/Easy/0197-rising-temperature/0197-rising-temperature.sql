# Write your MySQL query statement below

-- select w1.id
-- from weather w1 left join weather w2 on w1.recordDate = date_add(w2.recordDate, interval 1 day)
-- where w1.temperature > w2.temperature

with yesterday as(
    select id, recorddate, temperature, lag(temperature) over(order by recorddate) as temp2, lag(recorddate) over(order by recorddate) as date2
    from weather 
)

select id
from yesterday
where recorddate = date_add(date2, interval 1 day) and temperature > temp2