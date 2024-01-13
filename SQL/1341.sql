WITH T1 AS (
    SELECT
        user_id,
        COUNT(*) AS rating_ttl
    FROM
        MovieRating
    GROUP BY
        user_id
),

T2 AS (
    SELECT
        movie_id,
        AVG(rating) AS rating_avg
    FROM
        MovieRating
    WHERE
        YEAR(created_at) = 2020 
        AND MONTH(created_at) = 2
    GROUP BY
        movie_id
)

(
    SELECT
        name AS results
    FROM
        T1
        LEFT JOIN Users U ON U.user_id = T1.user_id
    ORDER BY
        rating_ttl DESC,
        results
    LIMIT 1
)

UNION ALL

(
    SELECT
        title AS results
    FROM
        T2
        LEFT JOIN Movies M ON M.movie_id = T2.movie_id
    ORDER BY
        rating_avg DESC,
        results
    LIMIT 1
)