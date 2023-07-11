-- 코드를 입력하세요
SELECT a.id, a.name, a.host_id
from places a 
join 
(
    select id, name, host_id
    from places
    group by host_id
    having count(*) >= 2
) b
on a.host_id = b.host_id
