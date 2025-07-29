-- 코드를 입력하세요
SELECT user_id, nickname, total_sales
from USED_GOODS_USER u
inner join (SELECT writer_id, sum(price) as total_sales
            from USED_GOODS_BOARD 
            where status = 'done'
            group by writer_id
            having sum(price) >= 700000) b on u.user_id = b.writer_id
order by total_sales asc