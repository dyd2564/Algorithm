-- 코드를 입력하세요
SELECT MCDP_CD as'진료과코드', count(*) as '5월예약건수'
from appointment
where date_format(APNT_YMD, '%Y-%m') = '2022-05'
group by mcdp_cd
order by count(*), MCDP_CD

# select * from appointment
# where date_format(apnt_ymd, '%Y-%m') = '2022-05'and apnt_cncl_ymd is null

