select * from user_logs ul order by random () limit 5;
select avg(s_all_avg) from user_logs ul;
UPDATE user_logs 
SET s_all_avg = REPLACE(s_all_avg, ',', '.') 
WHERE s_all_avg LIKE '%,%';
ALTER TABLE user_logs 
ALTER COLUMN s_all_avg TYPE REAL 
USING s_all_avg::REAL;
SELECT AVG(s_all_avg) FROM user_logs;