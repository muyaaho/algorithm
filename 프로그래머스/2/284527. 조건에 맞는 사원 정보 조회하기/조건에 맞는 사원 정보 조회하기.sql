-- 코드를 작성해주세요
with a as 
(  
select sum(score) as score, emp_no, rank() over(order by sum(score) desc) as rk
from hr_grade
where year = 2022
group by emp_no
)


select score, e.emp_no, emp_name, position, email
from  a, hr_employees as e
where a.emp_no = e.emp_no
and rk=1