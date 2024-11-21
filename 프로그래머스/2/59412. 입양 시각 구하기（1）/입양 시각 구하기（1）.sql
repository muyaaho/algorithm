-- 코드를 입력하세요
SELECT date_format(datetime, '%H') as hour, count(*) as count
from animal_outs
where date_format(datetime, '%H') >= '09' and date_format(datetime, '%H') <= '19'
group by hour
order by hour