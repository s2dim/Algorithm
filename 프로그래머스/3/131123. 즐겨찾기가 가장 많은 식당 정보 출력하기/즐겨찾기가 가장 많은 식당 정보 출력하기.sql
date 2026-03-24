-- 코드를 입력하세요
SELECT i.food_type, i.rest_id, i.rest_name, i.favorites
from (SELECT food_type, max(favorites) mf
    from rest_info
    group by food_type) fv join rest_info i on fv.food_type = i.food_type and fv.mf = i.favorites
order by i.food_type desc