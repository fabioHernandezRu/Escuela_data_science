"""
optimizar es encoontrar el minimo o el maximo de una funcion 
el problema del morral

se tiene una mochila para cargar cosas, cuales articulos te da el
mayor valor posible?
"""

def morral(tamano_morral, pesos, valores, n):
    if n==0 or tamano_morral ==0:
        return 0
    if pesos[n-1] > tamano_morral:
        return morral(tamano_morral,pesos,valores, n-1)
    return max(valores[n-1]+ morral(tamano_morral - pesos[n-1],pesos,valores, n-1), 
                morral(tamano_morral,pesos,valores,n-1))



if __name__=='__main__':
    valores = [60,100,120]
    pesos = [10,20,30]
    tamano_morral = 60
    n = len(valores)
    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)

