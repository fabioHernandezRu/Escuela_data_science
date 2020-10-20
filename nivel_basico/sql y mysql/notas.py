"""

- select database(); / para saber en qué db estoy


CREATE database platzi_operation;
CREATE database IF NOT EXISTS platzi_operation;
SHOW warnings;
use platzi_operation;

CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    author_id INTEGER UNSIGNED,
    title VARCHAR(100)  NOT NULL,
    year INTEGER UNSIGNED NOT NULL DEFAULT 1900,
    language VARCHAR(2) NOT NULL DEFAULT 'es' COMMENT 'ISO 639-1 Language',
    cover_url VARCHAR(500),
    price DOUBLE(6,2) NOT NULL DEFAULT 10.0,
    sellable TINYINT(1) DEFAULT 1,
    copies INTEGER NOT NULL DEFAULT 1,
    description TEXT
);

CREATE TABLE IF NOT EXISTS authors (
    author_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    nationality VARCHAR(3) 
);

drop tables authors; // elimna la tabla authors

describe authors; // explica la db
desc books; //explica la db
show full columns from bookx; // explica la db 

'year' INTEGER UNSIGNED NOT NULL DEFAULT 1900, // para palabras reservadas


CREATE TABLE clients(
    client_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    birthdate DATETIME,
    gender ENUM("M","F","ND") NOT NULL,
    active TINYINT(1) NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE operations(
    operations_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    book_id INTEGER UNSIGNED,
    client_id INTEGER UNSIGNED,     
    operation ENUM("vendido","prestado", "devuelto") NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    finished TINYINT(1) NOT NULL
);
===============================================================================

INSERT INTO tabla(COLUMNAS*) VALUES (VALORES)

INSERT INTO authors(  name,nationality) VALUES ( "Juan Rulfo","MEX");
INSERT INTO authors( name,nationality) VALUES ("Gabriel García Márquez","COL");
INSERT INTO authors ( name,nationality) VALUES ("Juan Gabriel Vasquez","COL");

INSERT INTO authors ( name,nationality) VALUES ("Julio Cortázar","ARG"),("Isabel Allende","CHI"),("Octavio Paz","MEX"), ("Juan Carlos Onetti","URU");

==================================================================================
Duplicate Key

ON DUPLICATE KEY IGNORE ALL // ignora todos los errores sin problema no recomendado

ON DUPLICATE KEY UPDATE active = VALUES(active)

\G presenta los datos más legibles

=====================================================================================

Insercion de datos usando queries anidados

INSERT INTO books(title, author_id) VALUES ('El Laberinto de la Soledad',6);


INSERT INTO books(title, author_id,year) VALUES ('El Laberinto de la Soledad',(SELECT author_id FROM
    authors where name = "Octavio Paz"
    LIMIT 1),1960);

=====================================================================================
Bash y archivos SQL

mysql -u root -p < all_squema.sql
mysql -u root -p -D cursoplatzi < all_data.sql

=========================================================================================
Su majestad el select

SELECT name,email,gender from clients where gender = 'F';

SELECT YEAR(birthdate) from clients where gender = 'F';
SELECT YEAR(NOW())-YEAR(birthdate) FROM clients;
SELECT * FROM clients where name like '%Saave%' ;
SELECT name,email, YEAR(NOW())-YEAR(birthdate),gender FROM clients where gender= 'F' and name like '%Lop%';

SELECT name,email, YEAR(NOW())-YEAR(birthdate) AS edad,gender FROM clients where gender= 'F' and name like '%Lop%';
=========================================================================================
Comando JOIN -> cruce de tablas

select count(*) from authors;

select b.book_id,a.author_id, a.name, b.title
from books as b
join  authors as a
    on a.author_id = b.author_id
where a.author_id between 1 and 5;

select c.name, b.title,a.name AS author, t.type
from transactions as t
join books as b
    on t.book_id = b.book_id
join clients as c
    on t.client_id = c.client_id
join authors as a
    on b.author_id = a.author_id
where c.gender = "M" and t.type IN ('sell','lend');

******* INNER JOIN ***********
SELECT <columna_1> , <columna_2>,  <columna_3> ... <columna_n> 
FROM Tabla_A A
INNER JOIN Tabla_B B
ON A.pk = B.pk

*******  Left Join ***********
SELECT <columna_1> , <columna_2>,  <columna_3> ... <columna_n> 
FROM Tabla_A A
LEFT JOIN Tabla_B B
ON A.pk = B.pk

*******  Right Join ***********
SELECT <columna_1> , <columna_2>,  <columna_3> ... <columna_n>
FROM Tabla_A A
RIGHT JOIN Tabla_B B
ON A.pk = B.pk

*******  Outer Join ***********
SELECT <columna_1> , <columna_2>,  <columna_3> ... <columna_n>
FROM Tabla_A A
FULL OUTER JOIN Tabla_B B
ON A.pk = B.pk

=========================================================================================
¿ Qué nacionalidades hay?
SELECT DISTINCT nationality FROM authors order by nationality;

¿cuántos escritores hay de cada nacionalidad?
SELECT nationality, COUNT(author_id) AS C_authors 
FROM authors
WHERE nationality IS NOT NULL AND nationality NOT IN ('RUS')
GROUP BY nationality
ORDER BY c_authors DESC, nationality ASC;

¿ cuál es el promedio y desviación standard de los precios   de los libros ?
SELECT nationality,
COUNT(book_id) as libros,
AVG(price) AS prom,
STDDEV(price)  AS std
FROM books as b
JOIN authors as a
ON a.author_id = b.author_id 
GROUP BY nationality
ORDER BY libros desc;

¿cuál es el precio máximo y minimo de un libro?
SELECT a.nationality,MAX(price), MIN(price)
FROM books as b
JOIN authors AS a
on a.author_id = b.author_id
GROUP BY nationality;

SELECT c.name,t.type, b.title, 
CONCAT (a.name,"(", a.nationality,")") AS author,
TO_DAYS(NOW())  - TO_DAYS(t.created_at) AS ago
FROM transactions AS t
LEFT JOIN clients AS c
ON c.client_id=t.client_id
LEFT JOIN books AS B
ON b.book_id = t.book_id
LEFT JOIN authors as a
ON b.author_id = a.author_id;

=========================================================================================
select count(book_id), sum(if(year<19580,1,0)) as '<1950' from books;

select count(book_id),
sum(if(year<19580,1,0)) as '<1950',
sum(if(year<19580,0,1)) as '>1950'
from books;

"""
