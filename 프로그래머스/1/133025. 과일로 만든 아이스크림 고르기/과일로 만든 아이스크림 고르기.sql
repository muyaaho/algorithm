SELECT F.FLAVOR
FROM FIRST_HALF AS F INNER JOIN ICECREAM_INFO AS I
WHERE I.FLAVOR = F.FLAVOR AND TOTAL_ORDER > 3000 AND INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER DESC