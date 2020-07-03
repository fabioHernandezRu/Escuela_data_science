"""
permite comparar la eficiencia de un algoritmo
complejidad temporal vs complejidad espacial
podemos definirla como T(n)
Aproximaciones
tiempo en que corre un algoritmo
pasos del algoritmo
pasos conforme nos aproximamos al infinito
"""
import time

def factorial(n):
    respuesta = 1
    while (n>1):
        respuesta *= n
        n -= 1
    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    return n * factorial (n-1)


if __name__=="__main__":
    n =200000
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final-comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final-comienzo)
