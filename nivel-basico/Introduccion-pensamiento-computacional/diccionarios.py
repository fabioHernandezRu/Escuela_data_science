"""
los diccionarios son como listas
utilizan llaves no indices
no tienen orden interno
pueden iterarse
"""

my_dict= {
    'David':35,
    'Erika': 32,
    'Jaime': 50,
}

print(my_dict['David'])
""" queremos el valor juan y si no existe juan
regresa el valor 30"""
print(my_dict.get('Juan', 30))
#reasignar valor
my_dict['Jaime'] = 28
my_dict['Pedro'] = 10
print(my_dict)
#borrar valor
del my_dict['Jaime']
print(my_dict)
#iterar
for llave in my_dict.keys():
    print(llave)
for valor in my_dict.values():
    print(valor)
for llave, valor in my_dict.items():
    print(llave, valor)

#saber si hay una llave en un diccionario
print('David' in my_dict)
print('Tom' in my_dict)