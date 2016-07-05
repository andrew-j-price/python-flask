SET GLOBAL general_log_file = '/var/lib/mysql/general_log_file.log';
SET GLOBAL general_log = 'ON';

USE api;

CREATE TABLE IF NOT EXISTS `users` (
  id INT NOT NULL auto_increment PRIMARY KEY,
  name VARCHAR(25),
  city VARCHAR(25),
  state VARCHAR(25),
  country VARCHAR(25)
  );

INSERT INTO 
  users (name, city, state, country)
VALUES 
  ('Lucas','Holly Springs','NC','USA'),
  ('Franklin','Morrisville','NC','USA'),
  ('Tigger','Hundred Acre Wood','FL','USA'),
  ('Pooh','Hundred Acre Wood','CA','USA'); 


CREATE TABLE `api`.`names` (
  `id` INT NOT NULL AUTO_INCREMENT, 
  `firstname` VARCHAR(45) NULL, 
  `lastname` VARCHAR(45) NULL, 
  PRIMARY KEY (`id`)
  );

INSERT INTO 
  `api`.`names`(`firstname`,`lastname`)
  VALUES
  ("Kevin","Minion"),
  ("Stuart","Minion"),
  ("Bob","Minion");
