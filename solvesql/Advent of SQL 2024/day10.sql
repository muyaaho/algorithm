-- https://solvesql.com/problems/max-row/
-- 최댓값을 가진 행 찾기

select id
from points
where x = (select max(x) from points) or y = (select max(y) from points)
order by id
