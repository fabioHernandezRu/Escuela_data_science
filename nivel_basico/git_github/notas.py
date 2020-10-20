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

*- git init /se empieza el repositorio 
*- git add %nombre_archivo% o git add . /para añadir archivos o . para todo
*- git commit -m "mensaje" /para enviar a la db de control de version 
*- git status /para ver el status
*- git show /para mostrar todo el historico   
*- git log biografia.txt /para ver historia de un archivo 
*- git push /para subir a servidor remoto 

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

*- git config --list --show origin /para ver las configuraciones 
*- git config --global user.name "Fabio Hernandez" /para configurar username 
*- git config user.email "f_a_b_io_@hotmail.com" /para configurar correo 
------------------------------------------------------------------------
analizar cambios

*- git show <archivo> /muestra los cambios del archivo
*- git diff <####> <###> /muestra los cambios entre versiones
------------------------------------------------------------------------
volver en el tiempo

*- git log /ver numeros de versiones <##>
*- git reset  <####> --hard /para volver a una version anterior de todo fuerte
*- git reset  <####> --soft /para volver a una version anterior de todo suave conserva staging
*- git log --stat /ver versiones con detalle
*- git checkout <#####> <archivo> /para volver a una version anterior de un archivo
*- git checkout <rama> <archivo> /para regresar a la version actual
----------------------------------------------------------------------------
git reset vs git rm

*- git rm /elimina archivos sin elminar su historial
*- git rm --cached /los mantiene en el disco duro elimina en el proximo commit
*- git rm --force /elimina del disco duro tambien

*- git reset /vuelve al pasado sin posiblidad de retorno
*- git reset HEAD /saca archivos del area de staging 
---------------------------------------------------------------------------------
Flujo de trabajo básico con un repositorio remoto

*- git clone url /copia el repo remoto en local
*- git push /se envia al repo remoto
*- git fetch /descarga la actualización de un repo remoto al repo local
*- git merge /para traer el directorio de trabajo
*- git pull /descarga al repositorio local y al directorio (fetch + merge)
---------------------------------------------------------------------------------
Introducción a las ramas o branches de Git

*- git branch <rama> /crea la rama
*- git checkout <rama> /se pasa a la rama
---------------------------------------------------------------------------------
Fusión de ramas con git merge

Si estando en rama hago un merge con master, lo que hago es que mando master hacia rama
por eso si lo que se  quiere es enviar master a rama se debe hacer un checkout de master
y en master invocar merge rama
*- git merge <rama> /para traer la rama hacia la rama actual
------------------------------------------------------------------------------------------
Solución de conflictos al hacer merge

cuando hay conflictos se entra en estado rama|merging 
allí se deben solucionar los conflictos (visual studio ayuda)

luego se debe hacer commit -am de los cambios
--------------------------------------------------------------------------------------------
- Uso de Github - 
Primero: Guardar la URL del repositorio de GitHub
con el nombre de origin
*- git remote add origin URL

Segundo: Verificar que la URL se haya guardado
correctamente:
*- git remote
*- git remote -v

Tercero: Traer la versión del repositorio remoto y
hacer merge para crear un commit con los archivos
de ambas partes. Podemos usar git fetch y git merge
o solo el git pull con el flag --allow-unrelated-histories:
*- git pull origin master --allow-unrelated-histories

Por último, ahora sí podemos hacer git push para guardar
los cambios de nuestro repositorio local en GitHub:
*- git push origin master
--------------------------------------------------------------------------------------------
- Como funcionan las llaves públicas -

generan dos llaves una pública y una privada, la privada la conservo yo para descifrar lo 
que se me envíe desde la llave pública y así en sentido contrario
--------------------------------------------------------------------------------------------
- Configura tus llaves SSH en local -

en el bash de git 
*- ssh-keygen -t rsa -b 4096 -C "f_a_b_io_@hotmail.com"
copiar y pegar la llave pública en git
añadir llave privada a variable de entorno 
*- eval $(ssh-agent -s)
*- ssh-add ~/.ssh/id_rsa  
*- git remote -v
*- git remote set-url origin git@github.com:fabioHernandezRu/Escuela_data_science.git
-----------------------------------------------------------------------------------------------------
- Tags y versiones en Git y GitHub -

*- git log --all --graph --decorate --oneline /* para ver el history más dinámico
*- alias arbolito = "git log --all --graph --decorate --oneline" \para comprimir el comando

para crear un tag Primero copias el hash
*- git tag -a v0.1 -m "Resultado de las primeras clases del curso"   98ffd01
*- git show-ref --tags \para ver tags
*- git push origin --tags \para enviar a github
*- git tag \ para ver los tags
*- git tag -d <tag> \ para eliminar un tag pero sigue en github
*- git push origin :refs/tags/dormido para eliminar tag en github tambien
-----------------------------------------------------------------------------------------------------
- Enviar ramas al servidor -

*- gitk \para ver hisotria de manera visual
*- git checkout <rama> \para moverse hacia la rama
*- git push origin <rama> \enviar a servidor de git
-----------------------------------------------------------------------------------------------------
-Configurar múltiples colaboradores en un repositorio de GitHub-

 -----------------------------------------------------------------------------------------------------
-Flujo de trabajo profesional: Haciendo merge de ramas de desarrollo a master-

*- los archivos binarios no se agregan a repositorios (buena práctica)

------------------------------------------------------------------------------------------------------
-Flujo de trabajo profesional con Pull requests -

*- pull requests es estado intermedio antes de hacer el merge 
*- pull requests es una característica de GitHub
*- En GitHub se hace el pull request comparando la rama master con la rama del fix.
*- Uno, o varios colaboradores revisan que el código sea correcto y dan feedback (en el chat del pull request)
*- El colaborador hace los cambios que desea en la rama y lo vuelve a subir al remoto
 (automáticamente jala la historia de los cambios que se hagan en la rama, en remoto)
*- Se aceptan los cambios en GitHub
*- Se hace merge a master desde GitHub
-----------------------------------------------------------------------------------------------------------
- Creando un Fork, contribuyendo a un repositorio -

*- Característica única de GitHub
*- primer paso para colaborar -> darle watch -> click en fork (copia del proyecto y hacerlo como mio)
*- para hacer cambios traerlo al disco git clone -  
*- git commit -am "" 
*- git push para subir a mi repo remoto (no oficial)
*- para subir al repo original ir al repo original en github y solicitar pull request
*- create pull request ->    
*- el dueño del repositorio original debe revisar el pull request
*- luego puede hacer el review y mirar que todo este bien y aprovar
*- para que el fork reciba los cambios del original debe crear otra fuente para hacer pull
*- git remote -v 
*- git remote add upstream <github original>
*- git remote -v para ver queh hay una nueva fuente de datos
*- git pull upstream master con esto se jala el original
-----------------------------------------------------------------------------------------------------------
- Haciendo deployment a un servidor -

*- 

-----------------------------------------------------------------------------------------------------------
- Ignorar archivos con .gitignore -

*- se crea un archivo .gitignore en la raiz del proyecto
*- *.jpg ignora todos los .jpg
-----------------------------------------------------------------------------------------------------------
- readme.md (markdown)  -

*- se puede incluir imagenes, links, etc
*- se puede editar en vscode, editor online -> editor.md
-----------------------------------------------------------------------------------------------------------
- GithubPages  -

*- pages.github.com
*- se crea un repositorio con el nombre de usuario
*- se cre el index.html
*-  en github -> settings -> github pages -> master branch
*- <user_name>.github.io/<user_name> es el link de la página
*- si se quiere que cargue en la raiz debe cambiar el nombre de repo a <user_name>.github.io
-----------------------------------------------------------------------------------------------------------
- Reorganizando el espacio de trabajo  -

*- rebase -> agarrar un rama y pegarla a la rama maestra
*- git rebase master 
*- 
-----------------------------------------------------------------------------------------------------------
- Git stash: guardar cambios en memoria y recuperarlos después  -

*- git stash
*- se cambia en la rama master un archivo se le da git stash
*- si se quiere poner ese stash en un ramaa
*- git stash branch english-version
*- despues de eso el master vuelve a la normalidad
*- git stash drop \ para borrar stash 
-----------------------------------------------------------------------------------------------------------
- Git clean: limpiar tu proyecto de archivos no deseados -

*- git clean --dry-run \ ver que archivos se van a borrar
*- git clean -f \ forza el borrado
-----------------------------------------------------------------------------------------------------------
- Git cherry-pick: traer commits viejos al head de un branch -

*- git cherry-pick <#commit>
-----------------------------------------------------------------------------------------------------------
-  Reconstruir commits en Git con amend

*- después de hacer el commit 
*- git commit --amend \ pega los ultimos cambios al ultimo commit
-----------------------------------------------------------------------------------------------------------
-  Git Reset y Reflog: usese en caso de emergencia

*- git reflog -> se ve todo incluso lo eliminado
*- git reset --hard <#commit> -> va a esa version del head
-----------------------------------------------------------------------------------------------------------
-  Buscar en archivos en commits de git con grep y log

*- git grep <palabra>
*- git grep -n <palabra> \ para ver la linea donde esta <palabra>
*- git -c <palabra> \ para contar cuantas veces se usa la palabra
*- git log -S "<plabra>" \ muestra <plaabra> en commits


-----------------------------------------------------------------------------------------------------------
-  BONUS

git shortlog -sn = muestra cuantos commit han hecho cada miembros del equipo.
git shortlog -sn --all = muestra cuantos commit han hecho cada miembros del equipo hasta los que han sido eliminado
git shortlog -sn --all --no-merge = muestra cuantos commit han hecho cada miembros quitando los eliminados sin los merges
git blame ARCHIVO = muestra quien hizo cada cosa linea por linea
git COMANDO --help = muestra como funciona el comando.
git blame ARCHIVO -Llinea_inicial,linea_final= muestra quien hizo cada cosa linea por linea indicándole desde que linea ver ejemplo -L35,50
**git branch -r **= se muestran todas las ramas remotas
git branch -a = se muestran todas las ramas tanto locales como remotas


*- git config --global alias.stats <comando>
*-  

"""
