CREATE DATABASE todolistdb;

USE todolistdb;

CREATE TABLE todo (
	id INT NOT NULL AUTO_INCREMENT,
    content VARCHAR(200) NOT NULL,
    completed INT(1) DEFAULT 0,
    date_created DATETIME,
    
    PRIMARY KEY (id)
);