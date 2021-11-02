"""
elegir decisiones en cada  momento
de manera aleatoria.
--- camino de borrachos ---
se comienza en (0,0) se puede caminar a cualquier lado
con probabilidad = 25% 
"""
import random
from bokeh.plotting import figure, show 

class Borracho:
    def __init__(self, nombre):
        self.nombre = nombre


class BorrachoTradicional(Borracho):
    def __init__ (self, nombre):
        super().__init__(nombre)
    def camina(self):
        return random.choice([(0,1),(0,-1),(1,0),(-1,0)])

class   Coordenada:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def mover(self, delta_x, delta_y):
        return (Coordenada(self.x + delta_x, self.y + delta_y))
    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y
        return ((delta_x**2 + delta_y**2)**0.5)

class Campo:
    def __init__(self):
        self.coordenadas_de_borrachos = {}
    
    def anadir_borracho(self,borracho, coordenada):
        self.coordenadas_de_borrachos[borracho] = coordenada
    def mover_borracho (self, borracho):
        delta_x,delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)
        self.coordenadas_de_borrachos[borracho] = nueva_coordenada
    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho]


def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)
    for _ in range (pasos):
        campo.mover_borracho(borracho)
    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho
    origen = Coordenada(0,0)
    distancias = []
    for _ in range (numero_de_intentos):
        campo= Campo()
        campo.anadir_borracho(borracho,origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata))
    return distancias

def graficar(x,y):
    grafica = figure(title = 'Camino aleatorioa',x_axis_label = 'pasos', y_axis_label='distancia')
    grafica.line(x,y, legend = 'distancia media')
    show(grafica)

def main(distancias_de_caminata, numero_de_intentos,tipo_de_borracho):
    distancias_media_por_caminata = []
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias),4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.nombre} caminata aleatoria de {pasos}')
        print(f'distancia media {distancia_media}, distancia maxima {distancia_maxima}')
        print(f'distancia minima {distancia_minima}')
    graficar(distancias_de_caminata,distancias_media_por_caminata)
if __name__ == '__main__':
    distancias_de_caminata = [10, 100 , 10000]
    numero_de_intentos =  100
    borracho = BorrachoTradicional("fabio")
    main(distancias_de_caminata, numero_de_intentos,borracho)