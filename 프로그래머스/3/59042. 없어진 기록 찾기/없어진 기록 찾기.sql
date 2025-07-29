-- 코드를 입력하세요
SELECT o.animal_id, o.name
from ANIMAL_INS i
right join ANIMAL_OUTS o
on i.animal_id = o.animal_id
where o.datetime is not null and i.datetime is null