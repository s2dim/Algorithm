-- 코드를 작성해주세요

# select id, ntile(4) over (order by size_of_colony) as class
# from ecoli_data

# case class
# when 1 then 'LOW'
# when 2 then 'MEDIUM'
# when 3 then 'HIGH'
# when 4 then 'CRITICAL'
# end

select d.id, case c.class
                when 1 then 'LOW'
                when 2 then 'MEDIUM'
                when 3 then 'HIGH'
                when 4 then 'CRITICAL'
                end as colony_name
from ecoli_data d
join (select id, ntile(4) over (order by size_of_colony) as class
      from ecoli_data) c
on d.id = c.id
order by id