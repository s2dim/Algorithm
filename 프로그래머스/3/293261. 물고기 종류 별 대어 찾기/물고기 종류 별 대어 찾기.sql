-- 코드를 작성해주세요

# select fish_type, max(length)
# from fish_info
# group by fish_type

# select id, mx.fish_type, length
# from fish_info i
# join (select fish_type, max(length) as max
#     from fish_info
#     group by fish_type) mx
# on i.fish_type = mx.fish_type and i.length = mx.max

select ifo.id, n.fish_name, ifo.length
from fish_name_info n
join (select id, mx.fish_type, length
        from fish_info i
        join (select fish_type, max(length) as max
            from fish_info
            group by fish_type) mx
        on i.fish_type = mx.fish_type and i.length = mx.max) ifo
on n.fish_type = ifo.fish_type
order by id