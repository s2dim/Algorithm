-- 코드를 작성해주세요
with max_colony as (
    select max(size_of_colony) as max, year(DIFFERENTIATION_DATE) as year
    from ecoli_data
    group by year(DIFFERENTIATION_DATE)
)

select year(e.DIFFERENTIATION_DATE) year, m.max - e.SIZE_OF_COLONY year_dev, e.id
from ecoli_data e join max_colony m on year(e.DIFFERENTIATION_DATE) = m.year
order by year, year_dev