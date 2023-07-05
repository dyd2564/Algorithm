-- 코드를 입력하세요
# SELECT b.user_id, b.nickname, a.price as total_sales
# from used_goods_board a join USED_GOODS_USER b
# on a.WRITER_ID = b.user_id
# group by b.user_id
# where a.price >= 700000 and a.status = 'DONE'
# order by a.price

SELECT b.user_id, b.nickname, sum(a.price) as total_sales
from used_goods_board a join USED_GOODS_USER b
on a.WRITER_ID = b.user_id
where a.status = 'DONE'
group by b.user_id
having sum(a.price) >= 700000
order by total_sales

