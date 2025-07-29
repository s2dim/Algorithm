-- 코드를 작성해주세요
select d.dept_id, d.dept_name_en, e.avg as avg_sal
from hr_department d
join (select dept_id, round(avg(sal), 0) as avg
    from hr_employees
    group by dept_id) e
on d.dept_id = e.dept_id
order by avg_sal desc
