-- 코드를 작성해주세요
SELECT A.ID
     , CASE WHEN B.CNT IS NULL THEN 0 
            ELSE B.CNT
       END AS CHILD_COUNT
  FROM ECOLI_DATA A
  LEFT JOIN ( SELECT PARENT_ID, COUNT(*) AS CNT
                FROM ECOLI_DATA
               WHERE PARENT_ID IS NOT NULL
               GROUP BY PARENT_ID
            ) B
          ON A.ID = B.PARENT_ID
 ORDER BY ID