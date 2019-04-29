from my_function import my_print

# Funciones - parte 2

def suma(valor_uno, valor_dos, valor_tres):
	return(valor_uno + valor_dos + valor_tres)


resultado = suma(1,20,30)
my_print(resultado)


def division(valor_1,valor_2):
	return(valor_1/valor_2)

resultado = division(100,10)
my_print(resultado)

# Es posible nombrar lo valores a asignar sin depender del orden de los parametros

def division2(valor_uno, valor_dos):
	return(valor_uno / valor_dos)

resultado = division2(valor_dos = 20, valor_uno = 100)
my_print(resultado)


# Se puede indicar un valor inicial para un parametro, si, solo si
# cuando se invoca la función, ésta no lleva el parámetro que contiene valor inicial

def multiplicar(valor_uno, valor_dos = 10):
	return(valor_uno*valor_dos)

resultado = multiplicar(8)
my_print(resultado)


# Es posible regresar más de un valor en una función

def multiples_valores():
	return "String", 1, True, 30.4

resultado = multiples_valores()
my_print(resultado)

cadena = resultado[0]
entero = resultado[1]
booleano = resultado[2]
floatante = resultado[3]

my_print(cadena)
my_print(entero)
my_print(booleano)
my_print(floatante)

# Se pueden asignar los valores indicando la variable en la posición
# a la cual hará referencia el resultado de la función, separando por comas

string2, entero2, booleano2, flotante2 = multiples_valores()

my_print(string2)
my_print(entero2)
my_print(booleano2)
my_print(flotante2)


# Asignar funciones a variables

mi_variable = multiplicar

# Luego ejecuto la funcion desde la variable
resultado = mi_variable(6,8)
my_print(resultado)


# Llamar funciones dentro de funciones

def mostrar_resultado(funcion):
	my_print(funcion)

# Invoco la funcion que recibe función como parámetro
mostrar_resultado(mi_variable(5,10))