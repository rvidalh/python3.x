from my_function import my_print

# ARGUMENTOS


# Si no conocemos la cantida de argumentos que recibiremos como parámetros se hará lo siguiente
# al colocar un *nombre_argumento, indicamos que la funcion puede recibir N cantidad de argumentos
# se obtendran las N cantidad de argumentos y los convertira a una tupla de los argumentos

# Por convención en estos casos los argumentos se nombran como args
def suma(*args):
	resultado = 0
	for valor in args:
		resultado = resultado + valor
	return resultado

resultado = suma(5,6,7,8,9)

my_print(resultado)


# indicar valor de arguemnto según nombre
# Por convención en estos casos los argimentos se nombran kwargs

def suma2(**kwargs):
	valor = kwargs.get('cadena','No contiene valor')
	my_print(valor)

resultado = suma2(cadena = 'string', boleano = True, x = 10, y = 5+6)


# * --> Nos permitirá trabajar con N valores, interpretados como tuplas
# ** --> Nos permitirá trabajar con N valores, interpretados como un diccionario

