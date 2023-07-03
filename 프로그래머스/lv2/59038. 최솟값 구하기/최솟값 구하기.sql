-- 코드를 입력하세요
-- SELECT datetime as 시간
-- from (select * from animal_ins where rownum=1 order by datetime)


select datetime as 시간 from animal_ins order by datetime limit 1;
