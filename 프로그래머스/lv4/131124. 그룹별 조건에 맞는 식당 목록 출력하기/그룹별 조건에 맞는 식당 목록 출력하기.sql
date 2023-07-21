-- 코드를 입력하세요
SELECT m.member_name, review_text, date_format(review_date, '%Y-%m-%d')
from member_profile m join (
    select member_id, review_text, review_date 
    from rest_review
    where member_id = (
        select member_id
        from rest_review
        group by member_id
        order by count(*) desc
        limit 1
    ) 
) r
on m.member_id = r.member_id
order by 3,2

