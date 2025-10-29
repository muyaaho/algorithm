-- 코드를 작성해주세요
/*
SELECT A.ITEM_ID
     , A.ITEM_NAME
     , A.RARITY
  FROM ITEM_INFO A
     , ITEM_TREE B
 WHERE A.ITEM_ID = B.ITEM_ID
   AND A.ITEM_ID NOT IN ( SELECT PARENT_ITEM_ID
                            FROM ITEM_TREE
                           WHERE PARENT_ITEM_ID IS NOT NULL
                        )
 ORDER BY B.ITEM_ID DESC
 */
 
select a.item_id, a.item_name, a.RARITY
from item_info a left join item_tree b
on a.item_id = b.parent_item_id
where b.item_id is null
order by item_id desc