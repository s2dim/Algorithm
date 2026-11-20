# Write your MySQL query statement below
select d.name as department, e.name as employee, e.salary
from employee e join department d on e.departmentid = d.id
where (e.departmentid, e.salary) in (select d.id as department, max(e.salary) as max
                                from employee e join department d on e.departmentid = d.id
                                group by d.id)