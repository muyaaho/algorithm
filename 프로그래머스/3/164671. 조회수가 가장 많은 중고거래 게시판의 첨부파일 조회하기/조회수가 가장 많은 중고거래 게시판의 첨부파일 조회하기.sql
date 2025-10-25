-- 코드를 입력하세요
SELECT CONCAT ('/home/grep/src/'
               , A.BOARD_ID
               , '/'
               , B.FILE_ID
               , B.FILE_NAME
               , B.FILE_EXT) AS FILE_PATH
  FROM ( SELECT ROW_NUMBER() OVER(ORDER BY VIEWS DESC) AS SEQ
              , BOARD_ID
           FROM USED_GOODS_BOARD
       )               A
     , USED_GOODS_FILE B
 WHERE A.SEQ = 1
   AND A.BOARD_ID = B.BOARD_ID
 ORDER BY B.FILE_ID DESC