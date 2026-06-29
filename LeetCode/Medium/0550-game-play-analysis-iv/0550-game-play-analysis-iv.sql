# Write your MySQL query statement below
WITH first_login AS (
    SELECT player_id, MIN(event_date) AS first
    FROM Activity
    GROUP BY player_id
),
all_player AS (
    SELECT COUNT(*) AS total
    FROM first_login
)

SELECT ROUND(COUNT(a.player_id) / ap.total, 2) AS fraction
FROM first_login f
LEFT JOIN Activity a 
ON f.player_id = a.player_id
AND a.event_date = DATE_ADD(f.first, INTERVAL 1 DAY)
CROSS JOIN all_player ap;

