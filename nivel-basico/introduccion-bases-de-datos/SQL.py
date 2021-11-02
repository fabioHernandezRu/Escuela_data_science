"""
S - structured
Q - query
L - language

N - not
O - only
S - structured
Q - query
L - language

------------------------------------------------------------------------
DDL -> Data Definition Language (create,alter,drop): nos ayuda a definir
la estructura de la base de datos

**-create -> crear una schema o database, table, view  

CREATE TABLE 'people' (
    'person_id' int NOT NULL AUTO_INCREMENT,
    'last_name' varchar(255) NULL,
    'first_name' varchar(255) NULL,
    'address' varchar(255) NULL,
    'city' varchar(255) NULL,
    PRIMARY KEY ('person_id')    
    );

CREATE VIEW v_brasil_customers AS 
    SELECT customer_name, contact name
    FROM customers
    where country = "Brasil";

**-alter->modificar tablas

ALTER TABLE people
ADD date_of_birth date;

ALTER TABLE people
ALTER COLUMN date_of_birth year;

ALTER TABLE people
DROP COLUMN date_of_bith;

**-drop -> borrar tablas 
DROP TABLE people;
DROP DATABASE test_db;

------------------------------------------------------------------------
DML -> Data Manipulation Language

***- insert 
INSERT INTO people (last_name, first_name, address, city)
    VALUES ('Hernández', 'Laura', 'Calle 21','Monterrey');
    
**- update
UPDATE people
    SET last_name = 'chavez', city = 'Mérida'
    WHERE person_id = 1;

**- delete
DELETE FROM people
    where person_id = 1;

**- select
SELECT first_name, last_name FROM people;

------------------------------------------------------------------------
CONSULTAS O QUERYS

select * from posts where fecha_publicacion < '2024'
select titulo,fecha_publicacion, estatus from posts

para cambiar nombre de columna al momento de hacer select
------------------------------------------------------------------------
SELECT

select titulo AS encabezado,fecha_publicacion AS publicado en, estatus AS estado
FROM posts;

select count(*) as numero_posts from posts
-------------------------------------------------------------------------
FROM

Join une la llave primaria con la llave foranea que referencia 

Teoria de conjuntos 
- Diferencia lo que esta en un lado que no esta en el otro
    |Tabla A| Tabla B|
    * left join los datos de A que estan o no estan en B 
    * left join los datos de A que no estan en B
    * right join los datos de B que estan o no estan en A
    * right join los datos de B que no estan en A
- Intersección
    * inner join los valores que estan en A y B
- Union
    Outer Join
    * los valores que estan en A y en B trae todo
- Diferencia asimetrica
    Outer Join
    * los valores de A que no estan en B y los de B que no estan en A

Trae usuarios que tengan o no tengan posts
SELECT * 
    FROM usuarios
    LEFT JOIN posts ON usuarios.id = posts.usuario_id;

Trae usuarios que no tienen posts 
SELECT * 
    FROM usuarios
    LEFT JOIN posts ON usuarios.id = posts.usuario_id
    WHERE posts.usuario_id IS NULL;

Traes posts que tengan o no tengan usuario
SELECT * 
    FROM usuarios
    RIGHT JOIN posts ON usuarios.id = posts.usuario_id;

trae post que no tengan usuario
SELECT * 
    FROM usuarios
    RIGHT JOIN posts ON usuarios.id = posts.usuario_id
    WHERE posts.usuarios_id IS NULL;

trae posts que tienen usuario
SELECT * 
    FROM usuarios
    INNER JOIN posts ON usuarios.id = posts.usuario_id;

los post que no tienen usuario y los usuarios que no tienen post
-------------------------------------------------------------------------------
WHERE

SELECT * from posts
    WHERE id < 50;

SELECT * from posts
    WHERE estatus = 'activo';

SELECT * from posts
    WHERE estatus = 'activo';

SELECT * from posts
    WHERE titulo LIKE '%escandalo%'; -> que tengan la palabra escandalo


SELECT * from posts
    WHERE fecha_publicacion > '2025-01-01' ; -> con fechas

SELECT * from posts
    WHERE fecha_publicacion 
    BETWEEN '2025-01-01' AND '2025-12-31' ; -> con fechas

El valor nulo en una tabla generalmente es su valor por defecto 
cuando nadie le asignó algo diferente. La sintaxis para hacer
búsquedas de datos nulos es IS NULL. La sintaxis para buscar datos que
no son nulos es IS NOT NULL

-------------------------------------------------------------------------------
GROUP BY

agrupa resultados por categorias por ejemplo
muestra resultados para activos y para inactivos
en dos filas diferentes

SELECT estatus, SUM(id) suma_id
    FROM posts
    GROUP BY estatus;

SELECT YEAR(fecha_publicacion) AS post_year, count(*) AS post_quantity
    FROM posts
    group by post_year

se pueden agrupar por multiples criterios ejemplo
activos en marzo, inactivos en marzo etc

--------------------------------------------------------------------------------
ORDER BY y HAVING

SELECT * FROM POSTS
    ORDER BY id DESC;

SELECT * FROM POSTS
    ORDER BY fecha_publicacion DESC;

SELECT * FROM POSTS
    ORDER BY fecha_publicacion DESC
    LIMIT 5; -> los 5 primeros

HAVING es para where despues de group by

--------------------------------------------------------------------------------
Nested queries

hacer queries dentro de otras queries etc etc etc

SELECT new_table_projection.date, COUNT(*) AS posts_count
FROM(
    SELECT DATE (MIN(fecha_publicacion)) AS date, YEAR (fecha_publicacion)
    AS post_year FROM posts
    GROUP BY post_year    
) AS new_table_projection
GROUP BY new_table_projection.date
ORDER BY new_table_projection.date;

-----------------------------------------------------------------------------------
Convertir una pregunta en un query SQL

SELECT: lo que quieres mostrar
FROM: de dónde voy a tomar los datos
WHERE: los filtros de los datos que quieres mostrar
GROUP BY: los rubros que quiero organizar
ORDER BY: desc o asc
HAVING: los filtros que quiere para mis datos agrupados


"""