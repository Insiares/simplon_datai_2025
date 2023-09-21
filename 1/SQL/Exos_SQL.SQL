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

