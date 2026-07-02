# Write your MySQL query statement below

select id, (case 
            when id % 2 = 0 then la
            else ifnull(le, student)
            end) as student
from (select *, lag(student) over(order by id) as la, lead(student) over (order by id) as le
        from seat
        ) as t

