"""
Notacion asintotica
No importan variaciones pequeñas
el enfoque se centra en lo que pasa conforme el tamaño 
se acerca al infinito
mejor de los casos, promedio, peor de los casos
Big O
nada mas importa el termino de mayor tamaño
"""
#ley de la suma
def f(n):
    for i in range(n):
        print(i)

    for i in range (n):
        print(i)

# O(n)+O(n) = O(n+n) = O(2n) = O(n)

def f2(n):
    for i in range(n):
        print(i)

    for i in range (n*n):
        print(i)

# o(n) + O(n*n) = O(n+n^2) = O(n^2)

#ley multiplicacion 

def f3(n):
    for i in range(n):
        for j in range (n):
            print(i,j)
#O(n)*O(n) = O(n*n) = O(n^2)

