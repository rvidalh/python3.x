from my_function import my_print

# VARIABLES GLOBALES
# Una variable local no puede modificar a una variable global
# La variable global puede ser declarada antes o despues de la función que la utiliza
# pero la función que la utiliza, no puede ser invocada antes de crear la variable



def palindromo(frase):
	frase = frase.replace(' ','') # Variable local. Solo existe en el contexto de la función
	return frase == frase[::-1]


frase = 'anita lava la tina' # Variable global
resultado = palindromo(frase)
my_print(resultado)


# Palindromo que lee como frase una variable global

def palindromo2():
	nuevo_valor = frase.replace(' ','') 
	return nuevo_valor == nuevo_valor[::-1]

resultado2 = palindromo2()
my_print(resultado2)


# Modificar una variable global dentro de una función

variable_global = "variable"

my_print(variable_global)


def modificar():
	# agrando global nombre_variable, podemos modificar el valor de una variable global
	global variable_global
	variable_global = "Valor modificado"

modificar()
my_print(variable_global)


# Creación de variables globales mediante funciones

def crear_variable_global():
	global nueva_variable
	nueva_variable = 'Variable global creada mediante función'

# Se debe invocar la función para hacer la creación de la variable global

crear_variable_global()
my_print(nueva_variable)