# Tuplas
from my_function import my_print


# Tipos de dato que permiten almacenar diferentes tipos de datos, al igual que las listas.
# Las tuplas son inmutables, no se pueden agregar ni quitar elementos

# Creación de tupla
# Las tuplas se crean con (); las listas co []

mi_tupla = (1,"Dos",3,"Cuatro")
my_print(mi_tupla)

# Al igual que las listas, es posible acceder a cierto elemento según el índice.

# Impresión de elemento en x posición.
my_print(mi_tupla[2])

# Impresión desde x elemento hasta y elemento (no incluye el y elemento)
my_print(mi_tupla[1:3])

# Las tuplas se utilizan para mantener datos que sean constantes, que no deberán
# alterar sus valores durante la ejecución del programa

