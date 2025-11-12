-- 코드를 입력하세요
SELECT CART_ID
  FROM ( SELECT A.*
              , ROW_NUMBER() OVER(PARTITION BY CART_ID) ROW_NUM
           FROM ( SELECT DISTINCT
                         CART_ID
                       , NAME
                    FROM CART_PRODUCTS
                   WHERE NAME IN ('Yogurt', 'Milk') 
                   GROUP BY CART_ID, NAME 
                ) A
      ) B
 WHERE ROW_NUM = 2
 ORDER BY CART_ID