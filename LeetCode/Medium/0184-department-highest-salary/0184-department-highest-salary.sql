# Write your MySQL query statement below
WITH temp AS (
    SELECT e.departmentId, d.name, MAX(e.salary) AS maxSalary
    FROM employee e join department d on e.departmentId = d.id
    GROUP BY e.departmentId
)

select t.name as department, e.name as employee, e.salary
from employee e join temp t on e.salary = t.maxSalary and e.departmentId = t.departmentId
