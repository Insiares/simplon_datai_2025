DROP DATABASE IF EXISTS commandes;

CREATE DATABASE commandes;
USE commandes;

CREATE TABLE `COMMANDES` (
  `id_commande` smallint,
  `date_commande` date,
  `montant_commande` int,
  `id_client` smallint,
  `id_magasin` tinyint,
  `id_produit` smallint,
  PRIMARY KEY (`id_commande`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `CATEGORIE` (
	`id` TINYINT AUTO_INCREMENT,
  `cat_produit` VARCHAR(15),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `CLIENTS` (
  `id` smallint,
  `nom_client` VARCHAR(20),
  `prénom_client` VARCHAR(20),
  `email_client` VARCHAR(40),
  `adresse_client` VARCHAR(40),
  `id_ville` smallint,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `PAYS` (
  `id` tinyint auto_increment,
  `pays` VARCHAR(20),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `PRODUITS` (
  `id` smallint,
  `nom_produit` VARCHAR(20),
  `id_cat` tinyint,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `VILLE` (
  `id` smallint auto_increment,
  `ville` VARCHAR(15),
  `id_pays` tinyint, 
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;


CREATE TABLE `MAGASIN` (
	`id` tinyint auto_increment,
    `adresse_magasin` varchar(40),
    `id_ville` smallint,
    PRIMARY KEY (`id`)
    );
    
ALTER TABLE `COMMANDES` ADD FOREIGN KEY (`id_produit`) REFERENCES `PRODUITS` (`id`);
ALTER TABLE `COMMANDES` ADD FOREIGN KEY (`id_client`) REFERENCES `CLIENTS` (`id`);
ALTER TABLE `COMMANDES` ADD FOREIGN KEY (`id_magasin`) REFERENCES `MAGASIN` (`id`);
ALTER TABLE `CLIENTS` ADD FOREIGN KEY (`id_ville`) REFERENCES `VILLE` (`id`);
ALTER TABLE `PRODUITS` ADD FOREIGN KEY (`id_cat`) REFERENCES `CATEGORIE` (`id`);
ALTER TABLE `VILLE` ADD FOREIGN KEY (`id_pays`) REFERENCES `PAYS` (`id`);
ALTER TABLE `MAGASIN` ADD FOREIGN KEY (`id_ville`) REFERENCES `VILLE` (`id`);