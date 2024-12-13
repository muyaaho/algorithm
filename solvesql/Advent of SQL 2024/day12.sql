-- https://solvesql.com/problems/summary-of-artworks-in-3-years/
-- 3년간 들어온 소장품 집계하기

select classification,
count(case when strftime('%Y', acquisition_date) = '2014' then 1 end) as '2014',
count(case when strftime('%Y', acquisition_date) = '2015' then 1 end) as '2015',
count(case when strftime('%Y', acquisition_date) = '2016' then 1 end) as '2016'
from artworks
group by classification
