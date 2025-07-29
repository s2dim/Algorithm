-- 코드를 작성해주세요
select d.id, ifnull(c.count, 0) as child_count
from ecoli_data d
left join (select parent_id, count(parent_id) as count
        from ecoli_data
        where parent_id is not null
        group by parent_id) c
on d.id = c.parent_id




# select parent_id, count(parent_id) as count
# from ecoli_data
# where parent_id is not null
# group by parent_id
