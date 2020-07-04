"""
defensive programming - errores de semantica
se pueden crear excepciones propias
try, except, finally
no deben manejarse de manera silenciosa - no solo imprimir y ya
para aventar tu propia exepción utiliza el keyword raise
"""

def divide_elementos_de_lista(lista,divisor):
    try:
        return [ i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista,divisor))