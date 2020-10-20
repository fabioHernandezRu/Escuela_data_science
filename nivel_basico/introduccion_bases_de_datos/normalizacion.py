"""
-------------------------------------------------------------------------
tipos de datos y constraints

Tipos de dato:
-Texto: CHAR(n), VARCHAR(n), TEXT
-Números: INTEGER, BIGINT, SMALLINT, DECIMAL(n,s), NUMERIC(n,s)
-Fecha/hora: DATE, TIME, DATETIME, TIMESTAMP
-Lógicos: BOOLEAN

Constraints (Restricciones)
-NOT NULL: Se asegura que la columna no tenga valores nulos
-UNIQUE: Se asegura que cada valor en la columna no se repita
-PRIMARY KEY: Es una combinación de NOT NULL y UNIQUE
-FOREIGN KEY: Identifica de manera única una tupla en otra tabla
-CHECK: Se asegura que el valor en la columna cumpla una condición dada
-DEFAULT: Coloca un valor por defecto cuando no hay un valor especificado
-INDEX: Se crea por columna para permitir búsquedas más rápidas
-------------------------------------------------------------------------
normalización

12 mandamientos de Edgar Codd

ejemplo:
sin normalizar
_________________________________________________________________
Alumno | nivel_curso   | nombre_curso  | materia_1  | materia_2 |
Juanito| Maestria      | data engineer | mySQL      | Python    |  
Pepito | Licenciatura  |  Programación | MySQL      | Python    |
_______|_______________|_______________|____________|___________|

- Primera forma normal (1FN) atributos atómicos (sin campos repetidos)
En este caso ambas columnas (materia_1 y materia_2) son materias
por lo que al normalizar quedaría
_______________________________________________________________
Alumno_ID|Alumno | nivel_curso   | nombre_curso  | materia    |
1        |Juanito| Maestria      | data engineer | mySQL      |  
1        |Juanito| Maestria      | data engineer | Python     |  
2        |Pepito | Licenciatura  |  Programación | MySQL      |
2        |Pepito | Licenciatura  |  Programación | Python     |
_________|_______|_______________|_______________|____________|

- Segunda forma normal (2FN) Cumple 1FN y cada campo de la tabla
debe depender de una clave única, para esto se separa el contenido
en dos tablas

__________________________________________________
                    Tabla Alumnos                |
_________________________________________________|
Alumno_ID|Alumno | nivel_curso   | nombre_curso  |
1        |Juanito| Maestria      | data engineer |
2        |Pepito | Licenciatura  |  Programación |
_________|_______|_______________|_______________|

______________________________
        Tabla Materias       |
_____________________________|
Materia_ID|AlumnoID| Materia |
1         |1       | MySQL   |
2         |1       | Python  |
3         |2       | MySQL   |
4         |2       | Python  |
__________|________|_________|

- Tercera forma normal (3FN) cumple 1FN y 2FN y los campos que NO son
clave NO deben tener dependencias

__________________________________ 
          Tabla Alumnos          |
_________________________________| 
Alumno_ID|Alumno | curso_id      | 
1        |Juanito| 1             | 
2        |Pepito | 2             | 
_________|_______|_______________| 
______________________________________
        Tabla cursos                  |
______________________________________|
curso_id  |Nivel_curso | Nombre curso |
1         |Maestría    | data engineer|
2         |Licenciatura| Programación |
__________|____________|______________|
______________________________
        Tabla Materias       |
_____________________________|
Materia_ID|AlumnoID| Materia |
1         |1       | MySQL   |
2         |1       | Python  |
3         |2       | MySQL   |
4         |2       | Python  |
__________|________|_________|

- Cuarta forma normal (4FN) cumple 1FN, 2FN, 3FN y los campos
multivaluados son de clave única

__________________________________ 
          Tabla Alumnos          |
_________________________________| 
Alumno_ID|Alumno | curso_id      | 
1        |Juanito| 1             | 
2        |Pepito | 2             | 
_________|_______|_______________| 
______________________________________
        Tabla cursos                  |
______________________________________|
curso_id  |Nivel_curso | Nombre curso |
1         |Maestría    | data engineer|
2         |Licenciatura| Programación |
__________|____________|______________|

______________________________________
       Materias por alumno            |
______________________________________|
mpa_id    |Materia_id  | Alumno_id    |
1         |1           |  1           |
2         |2           |  1           |
3         |1           |  2           |
4         |2           |  2           |
__________|____________|______________|
______________________________
        Tabla Materias       |
_____________________________|
Materia_ID|AlumnoID| Materia |
1         |1       | MySQL   |
2         |1       | Python  |
3         |2       | MySQL   |
4         |2       | Python  |
__________|________|_________|


"""