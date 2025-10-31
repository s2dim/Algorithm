select d3.id
from ecoli_data d3
join (select d2.id
      from ecoli_data d2
      join (select *
          from ecoli_data
          where parent_id is null) d1 
      on d2.parent_id = d1.id) d12
on d3.parent_id = d12.id
order by d3.id asc