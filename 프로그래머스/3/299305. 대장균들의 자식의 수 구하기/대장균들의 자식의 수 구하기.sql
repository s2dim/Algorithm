-- 코드를 작성해주세요

select p.id as id, sum(case
                        when c.parent_id > 0 then 1
                        else 0
                      end) as child_count
from ecoli_data p left join ecoli_data c on p.id = c.parent_id
group by id
order by id

