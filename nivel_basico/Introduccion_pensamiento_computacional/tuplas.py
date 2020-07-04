"""
las tuplas son lista de valores que no se pueden modificar 
pueden contener cualquier tipo de objeto
se utiliza para devolver varios valores en una función
se definen con parentesis
"""
my_tuple = ()
print(f'el tipo de objeto es {type(my_tuple)}')
my_tuple = (1, 'dos', True)
print(f' los valores de la tupla son:')
for x in range(len(my_tuple)):
    print(f'{my_tuple[x]} de tipo {type(my_tuple[x])}')

#re asignación de variables
x , y , z = my_tuple
print(x , y, z)

def coordenadas():
    return (5,4)

a, b = coordenadas()
print(a,b)