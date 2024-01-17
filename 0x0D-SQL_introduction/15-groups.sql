-- This script performs distinct count query search.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC, score;
