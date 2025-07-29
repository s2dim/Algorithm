-- 코드를 작성해주세요

select t.item_id, i.item_name, i.rarity
from item_tree t
join item_info i
on t.item_id = i.item_id
where t.item_id not in (select parent_item_id
                    from item_tree
                    where parent_item_id is not null
                    group by parent_item_id)
order by item_id desc

# select parent_item_id
# from item_tree
# where parent_item_id is not null
# group by parent_item_id