WITH Confirm AS (
    SELECT
        user_id,
        COUNT(*) AS confirm_time
    FROM
        Confirmations
    WHERE
        action = 'confirmed'
    GROUP BY
        user_id
),

Timeout AS (
    SELECT
        user_id,
        COUNT(*) AS timeout_time
    FROM
        Confirmations
    WHERE
        action = 'timeout'
    GROUP BY
        user_id
)

SELECT
    user_id,
    ROUND(IFNULL(IFNULL(confirm_time, 0) / (IFNULL(timeout_time, 0) + IFNULL(confirm_time, 0)), 0), 2) AS confirmation_rate
FROM
    Signups
    LEFT JOIN Confirm USING (user_id)
    LEFT JOIN Timeout USING (user_id)
