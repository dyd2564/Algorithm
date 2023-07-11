-- 코드를 입력하세요
# SELECT apnt_no, pt_name, pt_no, mcdp_cd, dr_name, apnt_ymd
# from patient a join appointment b
# on a.mcdp_cd = b.mcdp_cd

# order by apnt_ymd

select d.APNT_NO ,c.pt_name, d.PT_NO, d.MCDP_CD, d.DR_NAME, d.APNT_YMD
from patient c join (
select a.apnt_no, a.pt_no, a.MCDP_CD, b.dr_name, a.apnt_ymd 
from appointment a join doctor b
on a.MDDR_ID = b.DR_ID
where a.apnt_cncl_yn = 'N' and a.mcdp_cd = 'CS' and  date_format(a.apnt_ymd, '%Y-%m-%d') = '2022-04-13'
) d
on c.pt_no = d.pt_no
order by d.apnt_ymd