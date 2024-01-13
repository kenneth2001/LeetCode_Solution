SELECT
    CASE
        WHEN id%2 != 0 AND id != counts THEN id+1
        WHEN id%2 != 0 AND id = counts THEN id
        ELSE id-1
    END AS id
    , student
FROM
    seat, 
    (SELECT COUNT(*) AS counts FROM seat) T
ORDER BY
    id