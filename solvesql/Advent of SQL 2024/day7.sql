-- https://solvesql.com/problems/ratio-of-gifts/

select round(count(*) * 100.0 / (select count(*) from artworks), 3) as ratio
from artworks
where upper(credit) like '%GIFT%'

-- 100.0을 마지막에 곱해주면 0이 나온다. count가 float형이 아닌 int로 계산되기 때문이다.
-- 전체 값은 서브쿼리로 구했다.
