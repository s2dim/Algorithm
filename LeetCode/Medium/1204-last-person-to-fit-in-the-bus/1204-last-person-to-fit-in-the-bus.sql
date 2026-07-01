# Write your MySQL query statement below

with sort as(
    select person_name, weight, sum(weight) over (order by turn) as total_weight
    from queue
)

select person_name
from sort
where total_weight <= 1000
order by total_weight desc
limit 1