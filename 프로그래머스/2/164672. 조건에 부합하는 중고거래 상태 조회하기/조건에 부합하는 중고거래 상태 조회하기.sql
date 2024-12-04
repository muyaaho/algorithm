-- 코드를 입력하세요
SELECT board_id, writer_id, title, price, case when status='SALE' then '판매중' when status='RESERVED' then '예약중' when status='DONE' then '거래완료' END AS STATUS
from USED_GOODS_BOARD
where date_format(created_date, '%y%m%d') = '221005'
order by board_id desc