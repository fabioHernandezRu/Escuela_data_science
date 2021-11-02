"""
tomar varias formars
permite cambiar el cmportamiento de una superclase para 
adaptarlo a la subclase
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


if __name__=="__main__":
    main()