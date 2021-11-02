import random
import math
import statistics
def aventar_agujas(numero_de_agujas):
    adentro_del_circulo = 0
    for _ in range(numero_de_agujas):
        x = random.random() * random.choice([-1,1])
        y = random.random() * random.choice([-1,1])
        distancia_desde_el_centro = math.sqrt(x**2 + y**2)
        if(distancia_desde_el_centro<=1):
            adentro_del_circulo +=1
    return (4*adentro_del_circulo)/ numero_de_agujas

def estimacion(numero_de_agujas, numero_de_intentos):
    estimados = []
    for _ in range(numero_de_intentos):
        estimacion_pi = aventar_agujas(numero_de_agujas)
        estimados.append((estimacion_pi))
    return statistics.mean(estimados),   statistics.stdev(estimados)

def estimar_pi(precision, numero_de_intentos):
    numero_de_agujas = 1000
    sigma = precision
    while sigma>= precision / 1.96:
        media , sigma = estimacion(numero_de_agujas,numero_de_intentos)
        print(f'con {numero_de_agujas} estima {media}, std{sigma}')
        numero_de_agujas*=2
    return media

if __name__ == "__main__":
    estimar_pi(0.01,1000)