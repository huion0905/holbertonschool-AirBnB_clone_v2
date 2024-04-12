-- Create the database hbnb_test_db if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create user hbnb_test with access from localhost if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges on the hbnb_test_db database to user hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant SELECT privilege on performance_schema database to user hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Apply privilege changes
FLUSH PRIVILEGES;
