"""
Recorre una lista que necesita ordenarse
compara elementos adyacentes y los va intercambiando
se repite hasta que no se requieran mas cambios
"""
import random
def ordenamiento_de_burbuja(lista):
    n = len (lista)
    for i in range (n):
        for j in range (0, n-i-1):
            if(lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return  lista


if __name__ == '__main__':
    tamano_lista = int (input (' de que tamano sera la lista?'))
    lista = [random.randint(0,100) for i in range(tamano_lista)]
    print(lista)
    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)

