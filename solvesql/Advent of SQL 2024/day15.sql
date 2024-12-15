-- https://solvesql.com/problems/find-unnecessary-station-2/
-- 폐쇄할 따릉이 정류소 찾기 2

with rent as (
  select rent_station_id as station_id
  , count(case when strftime('%Y%m', rent_at) = '201810' then 1 end) as cnt18
  , count(case when strftime('%Y%m', rent_at) = '201910' then 1 end) as cnt19
  from rental_history
  where strftime('%Y%m', rent_at) in ('201810', '201910')
  group by rent_station_id
)
,return as (
  select return_station_id as station_id
  , count(case when strftime('%Y%m', rent_at) = '201810' then 1 end) as cnt18
  , count(case when strftime('%Y%m', rent_at) = '201910' then 1 end) as cnt19
  from rental_history
  where strftime('%Y%m', rent_at) in ('201810', '201910')
  group by return_station_id
)

,sum_cnt as (
  select rent.station_id
  , rent.cnt18 + return.cnt18 as cnt18
  , rent.cnt19 + return.cnt19 as cnt19
  from rent join return on rent.station_id = return.station_id
