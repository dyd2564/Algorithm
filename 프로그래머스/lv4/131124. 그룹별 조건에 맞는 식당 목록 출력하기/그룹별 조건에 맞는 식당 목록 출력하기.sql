-- 코드를 입력하세요
# SELECT member_name, review_text, review_date
# from member_profile m 
# join
# (
#     select * from rest_review
#     group by member_id
# )

# ksjs1115@gmail.com, soso94@naver.com, minjea985@naver.com

select m.member_name, b.review_text, date_format(b.review_date, '%Y-%m-%d')
from member_profile m join 
(
select review_text, review_date, member_id
from rest_review
where member_id = (
select member_id
    from rest_review
    group by 1
    order by count(*) desc
    limit 1
)) b
on m.member_id = b.member_id

order by 3, 2
