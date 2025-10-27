-- 코드를 입력하세요
SELECT B.ID
     , B.NAME
     , B.HOST_ID
  FROM ( SELECT HOST_ID
           FROM PLACES
          GROUP BY HOST_ID
         HAVING COUNT(*) >= 2 ) A
     , PLACES B
 WHERE A.HOST_ID = B.HOST_ID
 ORDER BY B.ID