DELETE FROM Person 
WHERE id NOT IN
  (SELECT id FROM (SELECT MIN(id) id FROM Person GROUP BY email) tmp);
