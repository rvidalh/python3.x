from my_function import my_print

# COMPREHENSION

# Comprehensions permitirá crear listas o tuplas de una forma más rápida

# lista1 = ['a','b','c']

# lista = [ valor for valor in lista1 ]

# ejemplo: lista = [ x for y in z ]
# x: valor a agregar
# y: elemento al que se le asigna cada elemnto de la lista y luego se agrega
# z: lista a iterar para obtener valores a agregar

"""
1- valor a agregar a lista
2- Un ciclo
"""

# se agregan números desde el 1 hasta el 100
lista = [ valor for valor in range(1,101) ]
my_print(lista)

# Condición al comprehension
# Se agregan solamente los números pares

lista2 = [ valor for valor in range(1,101) if valor % 2 == 0]
my_print(lista2)

# Creación de tuplas mediante comprehension
# para tupla, se debe hacer un cast --> tuple(comprehension)

tupla = tuple((valor for valor in range(1,101) if valor % 2 != 0))
my_print(tupla)


# Creación de diccionarios mediante comprehension
# diccionaro = { llave: valor for valor para llave, valor in enumerate(objeto iterable) }

diccionario = { indice: valor for indice, valor in enumerate(lista2) if indice <= 10 }
my_print(diccionario)