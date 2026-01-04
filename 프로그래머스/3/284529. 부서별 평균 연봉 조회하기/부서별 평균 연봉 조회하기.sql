-- 코드를 작성해주세요
select d.DEPT_ID, d.DEPT_NAME_EN, round(avg(SAL)) as AVG_SAL
from hr_employees e join hr_department d on e.dept_id = d.dept_id
group by d.DEPT_ID
order by AVG_SAL desc