CREATE DATABASE bakery;

use bakery;

--Users Table
CREATE TABLE users
(
  user_id INT NOT NULL AUTO_INCREMENT,
  firstName VARCHAR(240) NOT NULL,
  lastName VARCHAR(240) NOT NULL,
  email VARCHAR(240) NOT NULL,
  ieNumber VARCHAR(240) NOT NULL,
  password VARCHAR(240) NOT NUll,
  PRIMARY KEY(user_id)
);

--Goods table 
CREATE TABLE goods
(
  good_id INT NOT NULL AUTO_INCREMENT,
  good_name VARCHAR(240) NOT NULL,
  amount INT NOT NULL,
  date_stamp datetime NOT NULL,
  PRIMARY KEY(good_id)
);
-- May need to add a datetime stamp to table


Show databases;

DESCRIBE Goods;

DROP TABLE goods;

--Reference stuff: 

-- Inserting data 
INSERT INTO goods
(good_name, amount, date_stamp)
VALUES ('Blueberry Muffin', 3, curdate());
-- INSERT INTO actions
-- VALUES (1, 1, True, 'TST-TST-2023-0001', 101, 'BWA', 'ie7046', '2023-01-01', False, True, True);

DELETE FROM actions WHERE action_id = 1;

SELECT COUNT(NOA) FROM actions WHERE Processor_ieNumber = 'ie7001' AND
                NOA = 101;

--Online references 
Time Stamp information:
https://stackoverflow.com/questions/37616760/how-to-insert-timestamp-into-my-mysql-table
"INSERT INTO contactinfo 
(name, email, subject, date, comments)
VALUES 
('$name', '$email', '$subject', NOW(), '$comments')"

Another reference: 