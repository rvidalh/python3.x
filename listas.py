# Listas

from my_function import my_print

# Una lista puede ser cargada con distintos tipos de datos
# dentro de la misma

mi_lista = ["String", 1, 3.5, False, True]
my_print(mi_lista)

# Agregar elementos a una lista

# Método append inserta al final de la lista
mi_lista.append("nuevo elemento")
my_print(mi_lista)

# Método insert inserta un dato en la posición x indicada.
# lista.insert(x,elemento)

mi_lista.insert(0, 'Elemento agregado')
my_print(mi_lista)

# El acceso a los datos de la lista, son accesibles mediante indices

my_print(mi_lista[0])


# Método para remover un elemento de la lista

mi_lista.remove(False)
my_print(mi_lista)

# Método pop quita el último elemento de una lista, es posible asignar
# dicho elemento a una variable

ultimo_elemento = mi_lista.pop()
my_print(ultimo_elemento)


# Lista de números

lista_enteros = [9,1,5,3,23,87,2]
my_print(lista_enteros)

# Método para ordenar números de forma ascendente

lista_enteros.sort()
my_print(lista_enteros)

# Ingresando al metodo sort, el parámetro reverse = true
# podemos indicar que ordene la lista de forma descendente

lista_enteros.sort(reverse = True)
my_print(lista_enteros)

# Unión de listas
lista_uno = ["valor_uno","valor_dos","valor_tres"]
lista_dos = [1,2,3]

lista_uno.extend(lista_dos)
my_print(lista_uno)