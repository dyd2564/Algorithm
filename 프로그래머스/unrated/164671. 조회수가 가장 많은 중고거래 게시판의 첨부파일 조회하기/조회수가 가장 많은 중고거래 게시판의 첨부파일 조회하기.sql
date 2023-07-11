-- 코드를 입력하세요
SELECT concat('/home/grep/src/', a.board_id, '/', a.file_id, a.file_name, a.file_ext) as file_path
from used_goods_file a join 
(
    select board_id, views from
    used_goods_board
    order by views desc
    limit 1
) b
on a.board_id = b.board_id
order by a.file_id desc

# select * from used_goods_board
# order by views desc

# select * from used_goods_file
# where board_id = 'B0008'
