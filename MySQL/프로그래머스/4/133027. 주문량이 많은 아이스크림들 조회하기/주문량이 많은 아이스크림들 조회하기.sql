-- 코드를 입력하세요
SELECT H.FLAVOR
FROM FIRST_HALF H
    JOIN (SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER1
          FROM JULY
          GROUP BY FLAVOR) J
    ON H.FLAVOR = J.FLAVOR
ORDER BY H.TOTAl_ORDER + J.TOTAL_ORDER1 DESC
LIMIT 3
