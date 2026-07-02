# Write your MySQL query statement below
with cnt as (
select *, lag(people) over(order by id) as la1, lag(people, 2) over(order by id) as la2, lead(people) over(order by id) as le1, lead(people, 2) over(order by id) as le2
from stadium
)

select id, visit_date, people
from cnt
where (la1 >= 100 and la2 >= 100 and people >= 100) or
    (la1 >= 100 and people >= 100 and le1 >= 100) or
    (people >= 100 and le1 >= 100 and le2 >= 100)
