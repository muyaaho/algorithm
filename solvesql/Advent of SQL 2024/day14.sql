-- https://solvesql.com/problems/moving-average-of-power-consumption/
-- 전력 소비량 이동 평균 구하기

select strftime('%Y-%m-%d %H:%M:%S', measured_at, '+10 minutes') as end_at, 
round(avg(zone_quads) over(rows 5 PRECEDING), 2) as zone_quads,
round(avg(zone_smir) over(rows 5 PRECEDING), 2) as zone_smir,
round(avg(zone_boussafou) over(rows 5 PRECEDING), 2) as zone_boussafou
from power_consumptions
where strftime('%Y%m%d-%H:%M:%S', measured_at) BETWEEN '20170101-00:00:00' and '20170131-23:50:00'
