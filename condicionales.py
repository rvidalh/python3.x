# Condicionales

from my_function import my_print

# Condicional IF

# Para decirle que acción debe tomar una condición, debe ir el bloque a ejecutar
# abajo de la condición, con un tab (identado).
# Python no trabaja con llaves {}

valor1 = "mivalor"

# if condicion : 
#	bloque a ejecutar

if valor1 == "mivalor":
	my_print("El valor cumple la condición")
else:
	my_print("El valor no cumple la condición")

# IF reducido a una línea

valor2 = "mivalor1"

mensaje = "El valor es igual" if valor2 == "mivalor1" else "El valor no es igual"
my_print(mensaje)


# IF con multiples condiciones

valor3 = "mivalor2"

if valor3 == "mivalor":
	my_print("El valor cumple la primera condición")
elif valor3 == "mivalor2":
	my_print("El valor cumple la segúnda condición")
else:
	my_print("El valor no cumple las condiciones")

# Si queremos declarar una condición, pero aún no tenemos conocimiento
# de lo que se relizará si se cumple la condición, podemos agregar el bloque
# "pass", para que el código no presente errores.

valor4 = True

if valor4 == True:
	pass	
else:
	my_print("El valor no es True")


# Tipos de condicionales
# > (mayor que); < (Menor que); >= (Mayor o igual que); <= (Menor o igual que)
# != (Distinto que); == (Igual que)

valor5 = 10

if valor5 != 6:
	my_print("El valor es diferente")	
else:
	my_print("El valor es igual")	

# Las constantes de condición en los IF son:
# True = 1
# False = 0

# Se consideran valores vaciones 
# [], (), {}, 0, '', None --> Falsos por ser vacios
# [1], (1), {'a': 1}, 'h' --> Verdaderos por contener algún valor
# Por lo que si se condiciona por dichos valores, se devolverá False

if []:
	my_print("El resultado es Veradero")
else:
	my_print("El resultado es Falso")

if (1):
	my_print("El resultado es Veradero")
else:
	my_print("El resultado es Falso")

valor6 = ''

if valor6:
	my_print("Valor6 contiene algo")
else:
	my_print("Valor6 no contiene nada")


# Es posible decirle a una variable que no contenga tipo de valor
# mediante la palabra reservada 'None'

valor7 = None

if valor7:
	my_print("Valor7 contiene algo")
else:
	my_print("Valor7 no contiene nada")

# Múltiples condiciones dentro de una condicional

valor8 = None
valor9 = 30

# Consulta sobre si se cumplen AMBAS condiciones

if valor8 and valor9 > 30:
	my_print("Se cumplen ambas condiciones")
else:
	my_print("No se cumplen ambas condiciones")



# Consulta si se cumple AL MENOS UNA de las condicones

if valor8 or valor9 == 30:
	my_print("Se cumple al menos una condición")
else:
	my_print("No se cumplen condiciones")


