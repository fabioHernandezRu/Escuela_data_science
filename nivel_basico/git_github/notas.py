"""
Git es un software de control de versiones diseñado por Linus Torvalds, pensando 
en la eficiencia y la confiabilidad del mantenimiento de versiones de aplicaciones cuando estas
tienen un gran número de archivos de código fuente. 
En su lugar GitHub es una forja para alojar proyectos utilizando el sistema de control de versiones Git.
GitHub sería la red social de código para los programadores, tu propio curriculum vitae.

Apuntes:

- No guardar todo el archivo nuevo para versionar
- Control de versiones-> solo guarda cambios y deja claro:
                    * donde, cuando y quien

--------------------------------------------------------------------
Importancia

*- git init se empieza el repositorio 
*- git add %nombre_archivo% o git add . para añadir archivos o . para todo
*- git commit -m "mensaje" para enviar a la db de control de version 
*- git status para ver el status
*- git show para mostrar todo el historico   
*- git log biografia.txt para ver historia de un archivo 
*- git push para subir a servidor remoto 

--------------------------------------------------------------------
Instalacion

buscar git en google

--------------------------------------------------------------------
Staging Area

Cuando se hace git add, se agregan los cambios a la memoria ram (staging Area)
git commit -m "" -> el archivo se va al repositorio (defecto Master)
estados de archivo:
*- sin git add es untracked
*- con git add estado tracked hace parte de staging
*- con git commit pasan a repositorio 
*- con git checkout envia los cambios de rama a la carpeta
+- con git log <archivo> para ver el history del archivo
------------------------------------------------------------------------
Branch & Merge

Master           -> v1 -> v2 -> v3 .... v_Actual  |  -> endVersion
Experimentos        | -> v2 -> v3 rama      |     | Merge  
bugFixing                                   | ->  |   

--------------------------------------------------------------------------
configuración

*- git config --list --show origin para ver las configuraciones 
*- git config --global user.name "Fabio Hernandez" para configurar username 
*- git config user.email "f_a_b_io_@hotmail.com" para configurar correo 
------------------------------------------------------------------------
analizar cambios

*- git show <archivo> muestra los cambios del archivo
*- git diff <####> <###> muestra los cambios entre versiones
------------------------------------------------------------------------
volver en el tiempo

*- git log ver numeros de versiones <##>
*- git reset  <####> --hard para volver a una version anterior de todo fuerte
*- git reset  <####> --soft para volver a una version anterior de todo suave conserva staging
*- git log --stat ver versiones con detalle
*- git checkout <#####> <archivo> para volver a una version anterior de un archivo
*- git checkout <rama> <archivo> para regresar a la version actual
----------------------------------------------------------------------------
git reset vs git rm

*- git rm elimina archivos sin elminar su historial
*- git rm --cached los mantiene en el disco duro elimina en el proximo commit
*- git rm --force elimina del disco duro tambien

*- git reset vuelve al pasado sin posiblidad de retorno
*- git reset HEAD saca archivos del area de staging 
---------------------------------------------------------------------------------
Flujo de trabajo básico con un repositorio remoto

*- git clone url copia el repo remoto en local
*- git push se envia al repo remoto
*- git fetch descarga la actualización de un repo remoto al repo local
*- git merge para traer el directorio de trabajo
*- git pull descarga al repositorio local y al directorio (fetch + merge)
---------------------------------------------------------------------------------
Introducción a las ramas o branches de Git

*- git branch <rama> crea la rama
*- git checkout <rama> se pasa a la rama
---------------------------------------------------------------------------------
Fusión de ramas con git merge

Si estando en rama hago un merge con master, lo que hago es que mando master hacia rama
por eso si lo que se  quiere es enviar master a rama se debe hacer un checkout de master
y en master invocar merge rama
*- git merge <rama> para traer la rama hacia la rama actual
------------------------------------------------------------------------------------------
Solución de conflictos al hacer merge

cuando hay conflictos se entra en estado rama|merging 
allí se deben solucionar los conflictos (visual studio ayuda)

luego se debe hacer commit -am de los cambios
--------------------------------------------------------------------------------------------
- Uso de Github - 
# Primero: Guardar la URL del repositorio de GitHub
# con el nombre de origin
git remote add origin URL

# Segundo: Verificar que la URL se haya guardado
# correctamente:
git remote
git remote -v

# Tercero: Traer la versión del repositorio remoto y
# hacer merge para crear un commit con los archivos
# de ambas partes. Podemos usar git fetch y git merge
# o solo el git pull con el flag --allow-unrelated-histories:
git pull origin master --allow-unrelated-histories

# Por último, ahora sí podemos hacer git push para guardar
# los cambios de nuestro repositorio local en GitHub:
git push origin master
--------------------------------------------------------------------------------------------
- Como funcionan las llaves públicas -

generan dos llaves una pública y una privada, la privada la conservo yo para descifrar lo 
que se me envíe desde la llave pública y así en sentido contrario
--------------------------------------------------------------------------------------------
- Configura tus llaves SSH en local -
en el bash de git 
"""
