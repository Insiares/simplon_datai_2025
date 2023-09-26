-- https://www.programiz.com/sql/online-compiler/
-- Afficher tous les prénoms

SELECT first_name
FROM Customers;

-- Afficher tous les noms pour le pays UK (where)

SELECT first_name
FROM Customers;
WHERE country = 'UK';

-- Afficher l'âge des gens qui vivent aux USA et dont le prénom est robert (and)

SELECT age
FROM Customers
WHERE country = 'USA' AND first_name = 'Robert'

-- Afficher combien il y a de moniteur dans la table orders

SELECT amount
FROM Orders
WHERE item = 'Monitor' ;

-- Afficher le nombre de client (COUNT())
SELECT COUNT(customer_id)
FROM Customers;

-- Afficher l'âge moyen des clients (AVG())

SELECT AVG(age)
FROM Customers;


SELECT first_name as prenom 
FROM Customers;

SELECT last_name as Clients_UK from Customers as clients
WHERE country = 'UK';

-- sale
SELECT customers.last_name, Shippings.status FROM Customers, Shippings
-WHERE customers.customer_id = Shippings.customer

-- propre 
SELECT customers.first_name, customers.last_name, orders.amount, Shippings.status 
FROM Customers 
JOIN Shippings ON Customers.customer_id = Shippings.customer 
JOIN  Orders ON  orders.customer_id = customers.customer_id


---- Créer un schéma flocon comme il faut 
-- To create a Snowflake schema from your initial table, you'll need to create separate dimension tables for "country" and "currency," each with a unique ID for reference. Then, you can use these new dimension IDs in your fact table. Here's a step-by-step guide to achieving this:

-- Step 1: Create the "Country" Dimension Table
CREATE TABLE `dim_country` (
  `country_id` mediumint(8) unsigned NOT NULL auto_increment,
  `country_name` varchar(100) default NULL,
  PRIMARY KEY (`country_id`),
  UNIQUE KEY `country_name` (`country_name`)
);

--In this table, country_id is the unique identifier for each country, and country_name stores the country name.

--Step 2: Populate the "Country" Dimension Table

--You can populate this table with the distinct country names from your initial table table_ini. You can use the following SQL query to insert data into the dim_country table:
INSERT INTO `dim_country` (`country_name`)
SELECT DISTINCT `country` FROM `table_ini`;
--Step 3: Create the "Currency" Dimension Table
CREATE TABLE `dim_currency` (
  `currency_id` mediumint(8) unsigned NOT NULL auto_increment,
  `currency_name` varchar(255) default NULL,
  PRIMARY KEY (`currency_id`),
  UNIQUE KEY `currency_name` (`currency_name`)
);
--Step 4: Populate the "Currency" Dimension Table
INSERT INTO `dim_currency` (`currency_name`)
SELECT DISTINCT `currency` FROM `table_ini`;
--tep 5: Create the Fact Table
--Now, you can create the fact table that references the dimension tables using their respective IDs:
CREATE TABLE `fact_table` (
  `fact_id` mediumint(8) unsigned NOT NULL auto_increment,
  `country_id` mediumint(8) unsigned NOT NULL,
  `currency_id` mediumint(8) unsigned NOT NULL,
  PRIMARY KEY (`fact_id`),
  FOREIGN KEY (`country_id`) REFERENCES `dim_country`(`country_id`),
  FOREIGN KEY (`currency_id`) REFERENCES `dim_currency`(`currency_id`)
);
--n this fact_table, country_id and currency_id are foreign keys referencing the dim_country and dim_currency tables, respectively.

--Step 6: Populate the Fact Table

--You can now populate the fact_table using the original data from table_ini and joining it with the dimension tables to get the corresponding dimension IDs. Here's an example query for populating the fact_table:
INSERT INTO `fact_table` (`country_id`, `currency_id`)
SELECT c.`country_id`, cur.`currency_id`
FROM `table_ini` ti 
JOIN `dim_country` c ON ti.`country` = c.`country_name`
JOIN `dim_currency` cur ON ti.`currency` = cur.`currency_name`;
