DROP DATABASE IF EXISTS gift_contact;
CREATE DATABASE IF NOT EXISTS gift_contact;
USE gift_contact;

####################
###   Relation   ###
####################
SELECT 'relation';
DROP TABLE IF EXISTS relation;
CREATE TABLE IF NOT EXISTS relation(
	rel_id			INT(6)			NOT NULL AUTO_INCREMENT,
	rel_desc        VARCHAR(30)     NOT NULL UNIQUE,
	PRIMARY KEY(rel_id)
);
INSERT INTO relation VALUES
	(1, 'Parent'),
	(2, 'School Friends'),
	(3, 'College Friends'),
	(4, 'Professional Friends'),
	(5, 'Club Friends'),
	(6, 'Siblings'),
	(7, 'Neibour'),
	(8, 'Teacher');


####################
###   Location   ###
####################
SELECT 'location';
DROP TABLE IF EXISTS location;
CREATE TABLE IF NOT EXISTS location(
	loc_id			INT(6)			NOT NULL AUTO_INCREMENT,
	loc_name		VARCHAR(30)		NOT NULL UNIQUE,
	loc_abbr        VARCHAR(10)		DEFAULT NULL UNIQUE,
	PRIMARY KEY(loc_id)
);
INSERT INTO location VALUES
	(1, 'Bhubaneswar',	'BBSR'),
	(2, 'Cuttack',		'CTC'),
	(3, 'Berhampur',	'BAM'),
	(4, 'Puri',			'PUR'),
	(5, 'Punjab',		'PUN'),
	(6, 'US',			'US'),
	(7, 'Balasore',		'BLS'),
	(8, 'Malkangiri',	'MKG');


###################
###   Contact   ###
###################
SELECT 'contact';
DROP TABLE IF EXISTS contact;
CREATE TABLE IF NOT EXISTS contact(
	con_id			INT(6)				NOT NULL AUTO_INCREMENT,
	con_name        VARCHAR(30)			NOT NULL UNIQUE,
	con_sex         ENUM('F','M','O')	DEFAULT NULL,
	con_dob         DATE                DEFAULT NULL,
	con_email       VARCHAR(30)         DEFAULT NULL,
	con_mobile      VARCHAR(30)         NOT NULL,
	rel_id          INT(6)              NOT NULL REFERENCES relation(rel_id),
	loc_id          INT(6)              NOT NULL REFERENCES location(loc_id),
	PRIMARY KEY(con_id)
);
INSERT INTO contact VALUES
	(1, 'Milan Das', 'M', '1963-11-25', 'milandas63@gmail.com', '7978168568', 8, 2);



SELECT c.con_id,c.con_name,c.con_mobile,r.rel_desc,l.loc_name FROM contact AS c
LEFT JOIN relation AS r ON r.rel_id=c.rel_id
LEFT JOIN location AS l ON l.loc_id=c.loc_id;
