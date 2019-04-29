from my_function import my_print
# Funciones - Parte 1

# Creando función factorial de número 5

def factorial():
	numero = 5
	factorial = 1
	while numero > 0:
		factorial =  factorial * numero
		numero -= 1
	my_print(factorial)

# invocar función
factorial()


# Creando función factorial, recibiendo argumentos para cualquier número

def factorial2(numero):
	factorial = 1
	while numero > 0:
		factorial =  factorial * numero
		numero -= 1
	my_print(factorial)

factorial2(5)
factorial2(6)
factorial2(7)

# Retornar valores desde una funcion

def factorial3(numero):
	factorial = 1
	while numero > 0:
		factorial =  factorial * numero
		numero -= 1
	return factorial

my_print(factorial3(10))



