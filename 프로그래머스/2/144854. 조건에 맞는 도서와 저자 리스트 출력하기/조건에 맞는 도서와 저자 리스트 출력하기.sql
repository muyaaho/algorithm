-- 코드를 입력하세요
SELECT book_id, author_name, date_format(published_date, '%Y-%m-%d') as published_date
from book as b, author as a
where b.author_id = a.author_id and category = "경제"
order by published_date