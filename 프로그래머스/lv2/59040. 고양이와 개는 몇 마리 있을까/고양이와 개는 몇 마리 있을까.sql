-- 코드를 입력하세요
select animal_type, count(animal_id) as count
from animal_ins
where animal_type in ('Cat', 'Dog')
group by animal_type
order by field(animal_type, 'Cat', 'Dog');