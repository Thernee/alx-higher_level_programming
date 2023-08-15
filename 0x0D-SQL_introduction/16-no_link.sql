-- lists all records of the table second_table
-- not listing  rows without a name value

SELECT name, score FROM `second_table`
WHERE name <> ''
ORDER BY score DESC;
