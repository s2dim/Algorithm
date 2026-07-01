# Write your MySQL query statement below

with top as(
    select name, salary, departmentId, dense_rank() over(partition by departmentId order by salary desc) as ranks
    from employee
)

select d.name as Department, t.name as Employee, t.salary as Salary
from top t join department d on t.departmentId = d.id
where ranks <= 3
