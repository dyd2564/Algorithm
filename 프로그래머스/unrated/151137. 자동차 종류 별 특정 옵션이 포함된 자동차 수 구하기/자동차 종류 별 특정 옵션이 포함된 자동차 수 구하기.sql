-- 코드를 입력하세요
SELECT car_type, count(*) as cars
from car_rental_company_car
where options like '%통풍%'
    or options like '%열선%'
    or options like '%가죽%'
group by car_type
order by car_type