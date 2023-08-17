-- 코드를 입력하세요
select a.animal_id, a.animal_type, a.name
from animal_ins a join animal_outs b
on a.animal_id = b.animal_id
where (a.sex_upon_intake not like 'Spayed %' and
       a.sex_upon_intake not like 'Neutered %') and
      (b.sex_upon_outcome like 'Spayed %' or 
       b.sex_upon_outcome like 'Neutered%')
      

