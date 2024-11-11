# -- 코드를 입력하세요
# SELECT USER_ID, PRODUCT_ID
# from online_sale
# where user_id in (
#     select user_id
#     from online_sale
#     group by user_id
#     having count(*) > 1
#     ) and 
#     sales_date > (
#     select min(sales_date)
#     from online_sale
#     group by user_id
#     )
# order by user_id asc, product_id desc

# SELECT *
# SELECT USER_ID, PRODUCT_ID
# FROM ONLINE_SALE
# WHERE USER_ID IN ( SELECT USER_ID
#                    FROM ONLINE_SALE
#                    GROUP BY USER_ID
#                    HAVING COUNT(*) > 1 AND MIN(SALES_DATE) < SALES_DATE)
                
# ORDER BY USER_ID ASC, PRODUCT_ID DESC;

SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(USER_ID) > 1
ORDER BY USER_ID, PRODUCT_ID DESC;



# SELECT USER_ID, PRODUCT_ID
# FROM ONLINE_SALE
# WHERE SALES_DATE IN (SELECT SALES_DATE
#                    FROM ONLINE_SALE
#                    GROUP BY USER_ID
#                     HAVING )
# ORDER BY USER_ID ASC, PRODUCT_ID DESC;


# select *
# from online_sale
# order by user_id, sales_date