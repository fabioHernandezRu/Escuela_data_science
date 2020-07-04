"""
son secuencias de objetos que se pueden modificar
efecto secundario -> side effects
es posible iterar con ellas
acepta append, pop, remove, insert, remove 
"""

my_list = [1 , 2, "hola"]
for i in my_list:
    print(f'valor {i} tipo {type(i)}')
print(my_list[1:])

#añadir 
my_list.append(4)
print(my_list)
my_list[0] = "a"
print(my_list)
my_list.pop()
print(my_list)
a = [1, 2, 3]
b = a
print ( a , b)
print( id(a), id(b))
a.append('a')
print(a)
print(b)

"""
CLONACION
como las listas a y b se modifican igualmente lo que se haga en a sucedera
en b y eso es un problema se utiliza el concepto de clonación
siempre es mejor clonar una lista que mutarla
para clonar una lista podemos usar la funcion list 
"""
a = [1,2,3]
b = a
c = list(a)
print(a, b, c)
a.append(3)
print(a,b,c)

"""
LIST COMPREHENSION
forma de aplicar operaciones a los valores de una secuencia
se pueden aplicar condiciones para filtrar
"""
my_list = list(range(100))
print(my_list)
double = [i*2 for i in my_list]
print(double)
pares = [i for i in my_list if i % 2 ==0 ]
print(pares)