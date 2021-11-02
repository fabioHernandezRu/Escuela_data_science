"""
probabilidad -> medida de certidumbre

"""
import random


def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []
    for _ in range(numero_de_tiros):
        tiro = random.choice([1,2,3,4,5,6])
        secuencia_de_tiros.append(tiro)
    return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
    tiros=[]
    for _ in range (numero_de_intentos): #cuantas veces corre la simulacion
        secuencia_de_tiros= tirar_dado(numero_de_tiros) # cuantas veces estoy tirando        
        tiros.append(secuencia_de_tiros) #tiros de tiros
        print(tiros)
    tiros_con_1=0
    for tiro in tiros:
        if(1 in tiro):
            tiros_con_1+=1
    probabilidad_tiros_con_1= tiros_con_1/numero_de_intentos #divide en número de intentos pero no en numero de tiros 
    print(probabilidad_tiros_con_1)
if __name__=='__main__':

    numero_de_tiros = int(input('cuantos tiros del dado: '))
    numero_de_intentos = int(input('cuantas corridas: '))
    main (numero_de_tiros, numero_de_intentos)