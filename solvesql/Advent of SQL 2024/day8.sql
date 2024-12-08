with a as (
  select strftime('%Y-%m', order_date) as order_month,
  sum(case when o.order_id not like 'C%' then price * quantity end) as ordered_amount,
  sum(case when o.order_id like 'C%' then price * quantity end) as canceled_amount
  from order_items as i, orders as o
  where i.order_id = o.order_id
  group by order_month
  order by order_month
)

SELECT  order_month, ordered_amount, canceled_amount, ordered_amount + canceled_amount as total_amount
from a

-- ordered_amount와 canceled_amount를 재사용하기 위해 with을 사용했다.
-- 취소되는 값의 quantity가 음수이기 때문에 따로 음수 처리를 하지 않아도 된다.
