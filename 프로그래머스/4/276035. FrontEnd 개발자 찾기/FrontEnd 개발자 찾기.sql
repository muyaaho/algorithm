-- 코드를 작성해주세요
SELECT B.ID
     , B.EMAIL
     , B.FIRST_NAME
     , B.LAST_NAME
  FROM ( SELECT SUM(CODE) CODE
           FROM SKILLCODES
          WHERE CATEGORY = "Front End"
          GROUP BY CATEGORY 
       ) A
     , DEVELOPERS B
 WHERE B.SKILL_CODE & A.CODE > 0
 ORDER BY ID