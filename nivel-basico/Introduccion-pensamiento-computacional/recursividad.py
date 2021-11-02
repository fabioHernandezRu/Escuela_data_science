def factorial(n):
    """
    calcula el factorial de n
    n int > 0 
    regresa n!
    """
    if n == 1:
        return 1
    return n *factorial(n-1)

n = int(input('Escribe un entero: '))

print(f' el factorial de {n} es {factorial(n)}')