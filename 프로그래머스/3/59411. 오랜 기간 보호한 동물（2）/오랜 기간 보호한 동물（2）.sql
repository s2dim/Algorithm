-- 코드를 입력하세요
SELECT i.animal_id, i.name
from animal_ins i right join (SELECT i.animal_id, o.datetime - i.datetime as period
                            from animal_ins i join animal_outs o on i.animal_id = o.animal_id
                            order by period desc
                            limit 2) p on i.animal_id = p.animal_id
order by p.period desc