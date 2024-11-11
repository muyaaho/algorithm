-- 코드를 입력하세요
SELECT f.flavor
FROM FIRST_HALF as f inner join ICECREAM_INFO as i on i.flavor = f.flavor
WHERE total_order > 3000 and ingredient_type = 'fruit_based'
order by total_order desc