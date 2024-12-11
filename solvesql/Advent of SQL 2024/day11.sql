-- https://solvesql.com/problems/weekday-stats-airpollution/
-- 서울숲 요일별 대기오염도 계산하기

select 
case strftime('%u', measured_at) 
when '1' then '월요일'
when '2' then '화요일'
when '3' then '수요일'
when '4' then '목요일'
when '5' then '금요일'
when '6' then '토요일'
when '7' then '일요일' end as weekday, 
round(avg(no2), 4) as no2,
round(avg(o3), 4) as o3,
round(avg(co), 4) as co,
round(avg(so2), 4) as so2,
round(avg(pm10), 4) as pm10,
round(avg(pm2_5), 4) as pm2_5
from measurements
group by weekday
order by strftime('%u', measured_at) 
