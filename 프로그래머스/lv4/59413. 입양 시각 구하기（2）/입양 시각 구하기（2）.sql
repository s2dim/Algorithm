-- 코드를 입력하세요
set @hour := -1;

select @hour := @hour + 1 as hour,
(   select count((datetime))
    from animal_outs
    where @hour = hour(datetime)) as hour
from animal_outs
where @hour < 23
