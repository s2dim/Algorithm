-- 코드를 입력하세요
SELECT j.flavor
from first_half h
left join july j on h.flavor = j.flavor
group by j.flavor
order by sum(h.total_order) + sum(j.total_order) desc
limit 3