-- 16. List all records with non-empty names, showing score and name, ordered by score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
