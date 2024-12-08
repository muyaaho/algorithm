-- https://solvesql.com/problems/publisher-with-many-games/

select c.name
from companies as c join games as g on c.company_id = g.publisher_id
group by publisher_id
having count(*) >= 10
