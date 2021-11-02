"""
============================
ARREGLOS o LISTAS
conjunto de datos ordenados
identifica por posicion
============================
"""
"""
# se definen con  [ ] 
variable1=[]
#Pueden ir incrementando su tamaño con append
for i in range (1,7):
    variable1.append(i)
print(variable1)
#Se puede acceder por posición
print(variable1[0])
print(variable1[1:])
print(variable1[:-1])
#se puede saber el tamaño con len(lista)
print(f"el tamaño es {len(variable1)}")
# se puede eliminar un elemento con .remove
variable1.remove(5)
# se puede insertar en cierta posición con .insert
variable1.insert(1,"hola")
print(variable1)
#se puede insertar una lista en una lista
variable1.insert(1,[1,2,3,4])
print(f"lista en lista {variable1}")
#acceder a la posicion 2 de la lista en lista
print(f"posicion 2 de lista en lista {variable1[1][2]}")
#acceder a la letra h de la palabra hola
print(f"la letra en palabra hola {variable1[2][0]}")
"""
"""
============================
Diccionarios
estructura de datos 
puede almacenar variables como
enteros cadenas listas y funciones
identifica por clave o key
============================

#definiendo un diccionario
diccionario = {"nombre": "carlos",
                "edad" : 22,
                "cursos": ['Python','C++','PHP']}
#se accede mediante la key 
print(f"el nombre es {diccionario['nombre']}")
#acceder a la lista del diccionario
print(f"el primer curso para {diccionario['nombre']} es {diccionario['cursos'][0]}")
#se puede recorrer el diccionario con for
for key in diccionario:
    print(f" {key} : {diccionario[key]}")

#obtener las llaves del diccionario
print(f"las llaves del diccionario {diccionario.keys()}")
#obtener los valores del diccionario
print(f"los valores de un diccionario {diccionario.values()} ")
"""
"""
=================================================
POO
Abstracción para todo lo que nos rodea
Ejemplo: Bicicleta, Perro, Gato, 
=================================================
"""

#================HERENCIA===============================
class Persona(object):
    """Clase que representa una Persona"""

    def __init__(self, cedula, nombre, apellido, sexo):
        """Constructor de clase Persona"""
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo

    def __str__(self):
        """Devuelve una cadena representativa de Persona"""
        return "%s: %s, %s %s, %s." % (
            self.__doc__[25:34], str(self.cedula), self.nombre, 
            self.apellido, self.getGenero(self.sexo))

    def hablar(self, mensaje):
        """Mostrar mensaje de saludo de Persona"""
        return mensaje

    def getGenero(self, sexo):
        """Mostrar el genero de la Persona"""
        genero = ('Masculino','Femenino')
        if sexo == "M":
            return genero[0]
        elif sexo == "F":
            return genero[1]
        else:
            return "Desconocido"

class Supervisor(Persona):
    """Clase que representa a un Supervisor"""

    def __init__(self, cedula, nombre, apellido, sexo, rol):
        """Constructor de clase Supervisor"""

        # Invoca al constructor de clase Persona
        Persona.__init__(self, cedula, nombre, apellido, sexo)

        # Nuevos atributos
        self.rol = rol
        self.tareas = ['10','11','12','13']

    def __str__(self):
        """Devuelve una cadena representativa al Supervisor"""
        return "%s: %s %s, rol: '%s', sus tareas: %s." % (
            self.__doc__[26:37], self.nombre, self.apellido, 
            self.rol, self.consulta_tareas())

    def consulta_tareas(self):
        """Mostrar las tareas del Supervisor"""
        return ', '.join(self.tareas)

supervisor1 = Supervisor("V-16987456", "Jen", "Paz", "D", "Chivo")
print(supervisor1.__str__())
#================== POLIFORMISMO ===================================
"""
tomar varias formars
permite cambiar el cmportamiento de una superclase para 
adaptarlo a la subclase
"""
"""
class Persona: 
    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print("Ando caminando")

class Ciclista(Persona):
    def __init__(self,nombre):
        
        super().__init__(nombre)
    
    def avanza(self):
        print("Ando moviendome en mi bicicleta")

def main():
    persona = Persona("David")
    persona.avanza()
    ciclista = Ciclista("Daniela")
    ciclista.avanza()
"""