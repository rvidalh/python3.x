from my_function import my_print

# Docstring
# Documentación de código
# La documentación se coloca sobre la primera línea de la función


def generador(*args):
	"""Recibe N cantidad de números y regres el número, ademas
	regresa True si el número es mayor a 5, de lo contrario,
	retorna False.
	"""
	for valor in args:
		yield valor, True if valor > 5 else False

# funcion.__name__ nos retorna el nombre de la función

nombre = generador.__name__

# funcion.__doc__ nos trae los comentarios o ducumentación que
# indicamos dentro de la función documentada.

documentacion = generador.__doc__
print(nombre, " : ")
my_print(documentacion)


"""
Para obtener la documentación desde el interprete de python
se debe escribir python3, en la consola de comandos, luego
importar la función desde la cual se desea recibir la documentacion,
se importa con "from (nombre archivo sin extensión) import (nombre de la función)"
luego se escribe "help(nombre de función)", lo que retorna los datos
asociados a dicha función.
"""


