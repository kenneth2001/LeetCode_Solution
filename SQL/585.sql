SELECT
    ROUND(SUM(TIV_2016), 2) tiv_2016
FROM
    insurance
WHERE
    TIV_2015 IN
    (
        SELECT TIV_2015 
        FROM insurance
        GROUP BY 1
        HAVING COUNT(*) > 1
    ) 
    AND CONCAT(LAT, LON) IN
    (
        SELECT CONCAT(LAT,LON) 
        FROM insurance
        GROUP BY LAT, LON
        HAVING COUNT(*) = 1
    )