from my_function import my_print

# FUNCIONES ANIDADAS

def validacion(num_uno,num_dos):
	return num_uno > 0 and num_dos > 0

def division(num_uno, num_dos):
	if validacion(num_uno, num_dos): # Llamado de funciones
		return num_uno / num_dos

resultado = division(10, 0)
my_print(resultado)


# Funcion anidada 


def division2(num_uno, num_dos):
	def validacion():
		return num_uno > 0 and num_dos > 0 # utiliza variables del parámetro
	if validacion(): # Llamado de funcione dentro de otra
		return num_uno / num_dos # utiliza variables del parámetro también


resultado = division2(60,0)

my_print(resultado)


# Closure --> Funciones que crean funciones

def crea_funcion(num_uno, num_dos): # Ejemplo de Closure
	def validacion():
		my_print("se ejecuta validación")
		return num_uno > 0 and num_dos > 0
	return validacion

nueva_funcion = crea_funcion(10,5)

my_print(nueva_funcion())


# Función que recibe función como parámetro

def aplica_funcion(funcion):
	resultado = funcion()
	my_print(resultado)

aplica_funcion(nueva_funcion)


