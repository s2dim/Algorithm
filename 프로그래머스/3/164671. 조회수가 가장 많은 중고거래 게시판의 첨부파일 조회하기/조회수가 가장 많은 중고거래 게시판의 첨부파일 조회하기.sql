-- 코드를 입력하세요
select concat('/home/grep/src/', f.board_id,'/', file_id, file_name, file_ext) as file_path
from used_goods_file f
join (SELECT board_id
      from USED_GOODS_BOARD
      order by views desc limit 1) v
on f.board_id = v.board_id
order by file_id desc