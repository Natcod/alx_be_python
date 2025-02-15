--Retrieve the full description of the 'books; table 
SELECT COLUMN_NAME,
       DATA_TYPE,
       CHARACTER_MAXIMUM_LENGTH,
       NUMERIC_PRECISION,
       NUMERIC_SCALE,
       COLUMN_TYPE,
       IS_NULLABLE,
       COLUMN_KEY,
       COLUMN_DEFAULT,
       EXTRA
 FROM INFORMATION_SCHEMA.COLUMNS
 WHERE TABLE_SCHEMA = DATABASE()   
   AND TABLE_NAME = 'books';