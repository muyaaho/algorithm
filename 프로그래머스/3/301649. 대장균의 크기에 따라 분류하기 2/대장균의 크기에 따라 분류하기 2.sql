-- 코드를 작성해주세요

select id
, case when percent <= 0.25 then 'CRITICAL'
when percent <= 0.50 then 'HIGH'
when percent <= 0.75 then 'MEDIUM'
else  'LOW' 
end as colony_name
from (select id, size_of_colony, percent_rank() over (order by size_of_colony desc) percent
     from ecoli_data) a

order by id

/*
select id, size_of_colony
, percent_rank() over (order by size_of_colony desc) percent
, rank() over (order by size_of_colony desc) rk
, row_number() over (order by size_of_colony desc) rn
from ecoli_data
*/