-- Create database hbnb_dev_db if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create user hbnb_dev with access from localhost if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges on the hbnb_dev_db database to the user hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant SELECT privilege in the performance_schema database to the user hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Apply privilege changes
FLUSH PRIVILEGES;
