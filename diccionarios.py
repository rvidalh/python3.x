# DICCIONARIOS

from my_function import my_print

# Un diccionario, al igual que las listas o tuplas, tienen la capacidad de almacenar datos,
# inclusive, almacenar otros diccionarios.
# La diferencia entre el diccionario y las listas o tuplas, es que éste, no es posible de acceder
# mediante indices

# Para almacenar valores en un diccionario, cada valor almacenado debe poseer una "Llave" o "Clave"
# la cual nos permitirá acceder a dicho valor
# Las llaves pueden ser strings o números, pero deben ser inmutables

# Si en el diccionario existen 2 llaves iguales, se tomará el valor de la última llave o clave

diccionario = { 'key1' : "Primer valor", 'key2' : "Segundo valor", 8 : 123456, (1,2) : "Valor llave tupla", 'key2' : 5000 }
my_print(diccionario)

# Es posible agregar o quitar valores a un diccionario.
# diccionario[llave] = valor a agregar a la llave.

# Agregar
diccionario['key3'] = "Valor agregado"
my_print(diccionario)

# Reemplazar el valor de una clave. Si no encuentra la llave, creará una nueva.
diccionario['key3'] = "Valor reemplazado"
my_print(diccionario)


# Obtención de datos de un diccionario

valor_1 = diccionario['key3']
my_print(valor_1)

# Si no encuentra la clave, devolverá error, se puede utilizar método get() para
# en caso de no encontrar la llave, devolver un valor X.

valor_2 = diccionario.get('key4', 'No existe')
my_print(valor_2)


# Eliminar valores de un diccionario

del diccionario['key1']
my_print(diccionario)

# Método que nos retornará un objeto iterable, en donde se contienen todas las llaves de un
# diccionario

llaves = diccionario.keys()
my_print(llaves)

# Utilizar lo devuelto por lo anterior, como una lista

llaves_lista = list(diccionario.keys())
my_print(llaves_lista)

# Método que nos retornará un objeto iterable, en donde se contienen todas los valores de un
# diccionario

valores = diccionario.values()
my_print(valores)

# Utilizar lo devuelto por lo anterior, como una lista

valores_lista = list(diccionario.values())
my_print(valores_lista)

# Valores a tupla

valores_tupla = tuple(diccionario.values())
my_print(valores_tupla)

# Extender un diccionario desde otro diccionario

diccionario_2 = { 'x': 5, 'y' : 6, 'z' : 7}
diccionario['x'] = diccionario_2['x']
diccionario['y'] = diccionario_2['y']
diccionario['z'] = diccionario_2['z']

my_print(diccionario)

# Método más optimo de extender un diccionario

diccionario.update(diccionario_2)
my_print(diccionario)
