-- 코드를 입력하세요
SELECT r.food_type, rest_id, rest_name, favorites
from rest_info r
join (select food_type, max(favorites) as max
      from rest_info
      group by food_type) fv
on    r.food_type = fv.food_type and r.favorites = fv.max
group by food_type
order by food_type desc



