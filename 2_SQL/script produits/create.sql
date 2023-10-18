-- on jete / on créé (en phase de developpement)
DROP DATABASE IF EXISTS FoodDistribution;
CREATE DATABASE FoodDistribution;

-- on active 
USE FoodDistribution;

-- Création des tables
CREATE TABLE Famille ( 
		ID SMALLINT UNSIGNED auto_increment,
		Famille VARCHAR(80) UNIQUE,
        PRIMARY KEY (ID)
);

CREATE TABLE Cond ( 
		ID SMALLINT UNSIGNED auto_increment,
		Cond VARCHAR(80) UNIQUE,
        PRIMARY KEY (ID)
);

CREATE TABLE Principale (
	ID SMALLINT UNSIGNED NOT NULL auto_increment,
    Code_article MEDIUMINT UNSIGNED,
    Libelle VARCHAR(80),
    Famille_id SMALLINT UNSIGNED DEFAULT "defaut",
    Cond_id SMALLINT UNSIGNED,
    PU_HT DEC(10,2),
    PRIMARY KEY (ID),
    FOREIGN KEY (Famille_id) REFERENCES Famille(ID) ON DELETE SET NULL,
    FOREIGN KEY (Cond_id) REFERENCES Cond(ID)
    );
    
    
-- Création d'une vue 
CREATE VIEW select_all AS
SELECT p.code_article as "code" , p.Libelle, f.famille, c.cond, p.PU_HT as "prix" from principale as p
JOIN Famille as f on p.Famille_id=f.ID
JOIN cond as c on p.Cond_id=c.ID;
