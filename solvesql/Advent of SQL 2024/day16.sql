-- https://solvesql.com/problems/find-steadyseller-writers/
-- 스테디셀러 작가 찾기

select author, max(year) as year, count(*) as depth
from (
  select author, year, genre
  , year - row_number() over(PARTITION by author order by author, year) grp
  from (
    select DISTINCT author, year, genre
    from books)
) 
where genre = 'Fiction'
group by author, grp
having count(*) >= 5
order by author, year
