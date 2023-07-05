-- 코드를 입력하세요
# SELECT food_type, rest_id, rest_name, max(favorites)
# from rest_info
# where favorites = max(favorites)
# group by 1
# order by 1 desc

select food_type, rest_id, rest_name, favorites 
from rest_info
where (food_type, favorites) in (
    (select food_type, max(favorites) from rest_info
    group by food_type)
)
group by 1
order by 1 desc