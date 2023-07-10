-- 코드를 입력하세요
SELECT date_format(sales_date, '%Y') as year, date_format(sales_date, '%m') as month, gender, count(distinct b.user_id) as users
from user_info a join online_sale b
on a.user_id = b.user_id
where gender is not null
group by 1, 2, 3
order by 1, 2, 3

# 61 51 8

# select count(*)
# from user_info a join online_sale b
# on a.user_id = b.user_id
# where substr(date_format(sales_date, '%m'), 2) = 4
# where gender is null