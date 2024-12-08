-- https://solvesql.com/problems/count-stations/

SELECT local, count(*) as num_stations
FROM station
group by local
order by num_stations
