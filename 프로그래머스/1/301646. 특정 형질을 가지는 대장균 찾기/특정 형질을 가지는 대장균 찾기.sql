-- 코드를 작성해주세요
select count(*) as count
from ecoli_data
where (not genotype&2) and (genotype&1 or genotype&4)