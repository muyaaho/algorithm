-- https://solvesql.com/problems/film-ending-with-consonant/

select title
from film
where rating in ('R', 'NC-17') and 
upper(title) not like '%A' and 
upper(title) not like '%E' AND
upper(title) not like '%I' AND
upper(title) not like '%O' AND
upper(title) not like '%U'
