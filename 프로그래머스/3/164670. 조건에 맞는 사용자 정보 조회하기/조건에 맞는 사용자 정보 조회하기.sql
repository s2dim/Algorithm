-- 코드를 입력하세요
select u.user_id, u.nickname, concat_ws(' ',city, street_address1, street_address2) as 전체주소, 
        concat_ws('-',substr(tlno,1, 3),substr(tlno,4,4),substr(tlno,8,4)) as 전화번호
from used_goods_user u
join (SELECT *
    from used_goods_board
    group by writer_id
    having count(writer_id) >= 3) b
on u.user_id = b.writer_id
order by u.user_id desc