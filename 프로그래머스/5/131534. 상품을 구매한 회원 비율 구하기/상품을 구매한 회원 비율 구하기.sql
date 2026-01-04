# -- 코드를 입력하세요


select year(o.sales_date) year, month(o.sales_date) month, count(distinct o.user_id) as purchased_users,
    round(count(distinct o.user_id) / (select count(*)
                                        from user_info
                                        where joined >= '2021-01-01' 
                                            and joined < '2022-01-01'), 1) as purchased_ratio
from online_sale o join (
                        select user_id, joined 
                        from user_info
                        where joined >= '2021-01-01' and joined < '2022-01-01') u 
                    on o.user_id = u.user_id
group by year(o.sales_date), month(o.sales_date)
order by year, month

                                                            
