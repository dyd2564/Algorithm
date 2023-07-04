-- 코드를 입력하세요
# SELECT a.product_code, sum(b.sales_amount) * a.price as sales
# from product a right outer join offline_sale b
# on a.product_id = b.product_id
# order by sales desc, product_code


select a.product_code, sum(b.sales_amount) * a.price as sales
# select *
from product a right outer join offline_sale b 
on a.product_id = b.product_id
group by a.product_id
order by sales desc, product_code

# select * from offline_sale
# order by product_id