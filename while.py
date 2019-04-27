#CICLO WHILE LO UTILIZAREMOS CUANDO DESCONOSCAMOS LA CANTIDAD DE ITERACIONES

from my_function import my_print


# while condicion:
#	codigo
# else(opcional):
# codigo

# Ejemplo utilizando break para cerrar el ciclo

contador = 0

while contador < 10: #Es posible el uso de condicionales >; >=; < ; <=; ==; !=
	my_print(contador)
	contador += 1

	if contador == 4:
		continue
	if contador == 6:
		break
else:
	my_print("Final")


# Ejemplo utilizando variable Bandera para finalizar MEJOR FORMA

contador2 = 0
bandera = True

while bandera: #Es posible el uso de condicionales >; >=; < ; <=; ==; !=
	my_print(contador2)
	contador2 += 1

	if contador2 == 4:
		continue
	if contador2 == 6:
		bandera = False
else:
	my_print("Final")