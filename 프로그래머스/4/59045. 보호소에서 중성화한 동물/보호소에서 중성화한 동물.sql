-- 코드를 입력하세요
SELECT animal_id, animal_type, name
from animal_outs
where animal_id in (SELECT ANIMAL_ID
                    from animal_ins
                    where sex_upon_intake like ('%Intact%')) and
    sex_upon_outcome regexp ('Spayed|Neutered')
order by animal_id