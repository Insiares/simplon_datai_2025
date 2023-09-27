-- on jete / on créé (en phase de developpement)
DROP DATABASE IF EXISTS Fooddistribution;
CREATE DATABASE FoodDistribution;

-- on active 
USE FoodDistribution;

-- Création des tables
CREATE TABLE Famille ( 
		ID SMALLINT UNSIGNED NOT NULL auto_increment,
		Famille VARCHAR(80),
        PRIMARY KEY (ID)
);

CREATE TABLE Cond ( 
		ID SMALLINT UNSIGNED NOT NULL auto_increment,
		Cond VARCHAR(80),
        PRIMARY KEY (ID)
);

CREATE TABLE Principale (
	ID SMALLINT UNSIGNED NOT NULL auto_increment,
    Code_article MEDIUMINT UNSIGNED,
    Libelle VARCHAR(80),
    Famille_id SMALLINT UNSIGNED,
    Cond_id SMALLINT UNSIGNED,
    PU_HT DEC,
    PRIMARY KEY (ID),
    FOREIGN KEY (Famille_id) REFERENCES Famille(ID),
    FOREIGN KEY (Cond_id) REFERENCES Cond(ID)
    );