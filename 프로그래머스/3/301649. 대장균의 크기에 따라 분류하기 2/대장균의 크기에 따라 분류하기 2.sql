-- 코드를 작성해주세요
select a.id, (case
              when b.per <= 0.25 then 'CRITICAL'
              when b.per <= 0.50 then 'HIGH'
              when b.per <= 0.75 then 'MEDIUM'
              else 'LOW'
          end) as colony_name
from ecoli_data a join (select id, percent_rank() over (order by size_of_colony desc) as per
                        from ECOLI_DATA ) b on a.id = b.id
order by id