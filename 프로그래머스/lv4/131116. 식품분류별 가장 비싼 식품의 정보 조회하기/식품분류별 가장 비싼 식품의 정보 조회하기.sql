-- 코드를 입력하세요
# SELECT category, price as max_price, product_name
# from food_product
# where (select price, product_name from food_product
#     where price = max(price) group by category

# )
# and category in ('과자', '국', '김치', '식용유')
# group by category

select category, price as max_price, product_name
from food_product
where (category, price) in 
(
    select category, max(price)
    from food_product 
    group by category
) and category in ('과자', '국', '김치', '식용유')
order by 2 desc
# group by category

# select *
# from food_product
