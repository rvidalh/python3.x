# Módulo

# Se verá la forma de utilizar archivos que contienen funciones,
# y como importar sus funciones desde otros archivos


# De ésta forma tambié se puede utilizar funciones de un módulo,
# este módulo y funcionalidad de creó para imprimir

from my_function import my_print

# Se utilizará el código del archivo calculadora para este ejemplo
# Este archivo funcionará como main

# Para utilizar calculadora se llama de la siguiente manera
# import nombre_archivo_sin_extension 

import calculadora


# Estamos utilizando la función suma del módulo calculadora
resultado = calculadora.suma(10, 21)

my_print(resultado)


"""
Cuando se realiza un import de un módulo, python crea un una carpeta llamda
_pycache_ la cual contiene un compilado del archivo al cual estamos
llamado, en caso éste no exista.
"""

# Importando funciones con un alias de la funcion

from calculadora import resta as sustracion

resultado = sustracion(10,5)
my_print(resultado) 


# se pueden importar multiples funciones
# from (nombre archivo con funciones, sin extensión) import (funcion_1, funcion_2, funcion_n)

from calculadora import multiplicacion, division

resultado = multiplicacion(10,5)
my_print(resultado) 

resultado = division(10,5)
my_print(resultado) 



# Importar TODO
# import nombre_archivo_sin_extension *
