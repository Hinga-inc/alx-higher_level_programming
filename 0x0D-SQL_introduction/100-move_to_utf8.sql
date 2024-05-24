-- this is a sql script that converts hbtn_0c_0 database to utf8 coollate utf8mb4_unicode_ci
-- Converts database to UTF8
ALTER DATABASE hbtn_0c_0
CHARACTER SET = utf8mb4 
COLLATE = utf8mb4_unicode_ci;

-- Converts table to UTF8
USE hbtn_0c_0;
ALTER TABLE hbtn_0c_0.first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Converts record name to UTF8
USE hbtn_0c_0;
ALTER TABLE first_table
CHANGE `name` name VARCHAR(256) CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;