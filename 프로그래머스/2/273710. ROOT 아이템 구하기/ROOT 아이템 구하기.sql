-- 코드를 작성해주세요
select i.item_id, item_name
from item_info as i, item_tree as t
where i.item_id = t.item_id and parent_item_id is null