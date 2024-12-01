-- 코드를 입력하세요
SELECT mcdp_cd as '진료과코드', count(*) as 5월예약건수
-- select mcdp_cd, count(*)
from appointment
where date_format(apnt_ymd, '%y%m') = '2205'
group by mcdp_cd
order by 5월예약건수, mcdp_cd