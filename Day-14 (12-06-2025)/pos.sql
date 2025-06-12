#####################################################################
#####################################################################
#####                                                           #####
#####                                                           #####
#####                           P O S                           #####
#####                     (Point of Sales)                      #####
#####                                                           #####
#####                                                           #####
#####################################################################
#####################################################################

DROP DATABASE IF EXISTS pos;
CREATE DATABASE IF NOT EXISTS pos;
USE pos;

########################
###   Manufacturer   ###
########################
SELECT 'manufacturer';
DROP TABLE IF EXISTS mfr;
CREATE TABLE IF NOT EXISTS mfr(
	mfr_id			INT(6)				NOT NULL AUTO_INCREMENT,
	mfr_name		VARCHAR(30)			NOT NULL UNIQUE,
	mfr_abbr		VARCHAR(10)			UNIQUE,
	PRIMARY KEY(mfr_id)
);
INSERT INTO mfr VALUES
	(1, 'Pfizer Pharmaceuticals', 'PF'),
	(2, 'Dr. Reddy Pharmaceuticals', 'DR'),
	(3, 'Alkem Pharmaceuticals','ALK'),
	(4, 'Torrent Pharmaceuticals','TO'),
	(5, 'Utkal Pharmaceuticals','UP');


###################
###   Product   ###
###################
SELECT 'product';
DROP TABLE IF EXISTS prod;
CREATE TABLE IF NOT EXISTS prod(
	prod_id			INT(6)				NOT NULL AUTO_INCREMENT,
	prod_name		VARCHAR(30)			NOT NULL UNIQUE,
	mfr_id          INT(6)              NOT NULL REFERENCES mfr(mfr_id),
	opening_stk     INT(10)             DEFAULT 0,
	closing_stk     INT(10)             DEFAULT 0,
	PRIMARY KEY(prod_id)
);
INSERT INTO prod VALUES
	(1, 'Cetrizine',		1, 0, 0),
	(2, 'Ceprofloxasine',	1, 0, 0),
	(3, 'Levofloxasine',	1, 0, 0),
	(4, 'Vitamin C',		1, 0, 0),
	(5, 'Vitamin B2',		1, 0, 0);



###############
###   Tax   ###
###############



#######################
###   Transaction   ###
#######################
SELECT 'transaction';
DROP TABLE IF EXISTS trn;
CREATE TABLE IF NOT EXISTS trn(
	trn_id				INT(6)				NOT NULL AUTO_INCREMENT,
	trn_date            DATE                NOT NULL,
	trn_type			ENUM('O','P','S')	NOT NULL,
	prod_id             INT(6)				NOT NULL REFERENCES prod(prod_id),
	qty					INT(10)				NOT NULL,
	free				INT(10)				DEFAULT 0,
	rate				DOUBLE(12,2)		DEFAULT 0,
	tax					DOUBLE(10,2)		DEFAULT 0,
	discount			DOUBLE(10,2)		DEFAULT 0,
	amount				DOUBLE(12,2)		DEFAULT 0,
	PRIMARY KEY(trn_id)
);
INSERT INTO trn VALUES
	(1, '2025-06-12', 'S', 1, 25, 0, 55.75, 120.00, 250.00, 1263.75);


SELECT * FROM trn
LEFT JOIN prod ON prod.prod_id=trn.prod_id
LEFT JOIN mfr  ON mfr.mfr_id=prod.mfr_id;
