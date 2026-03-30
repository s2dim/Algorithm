-- 코드를 입력하세요
with recursive hours as(
    select 0 as hour
    union all
    select hour + 1
    from hours
    where hour < 23
)
select h.hour, count(o.hour) as count
from hours h left join (select hour(datetime) as hour
                 from animal_outs) o on h.hour = o.hour
group by h.hour
order by h.hour