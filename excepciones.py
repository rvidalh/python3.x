# Excepciones



# Controla excepción del tipo divide by zero
try:
	print(2/0)
except ZeroDivisionError as ex:
	print("Hubo un error del tipo {}".format(ex))


# Controla excepción del tipo IndexError
try:
	lista = [1,2]
	print(lista[9])
except IndexError as ex:
	print("Hubo un error del tipo {}".format(ex))


# Se pueden anidar los except

try:
	#print(2/0)
	lista = [1,2]
	print(lista[9])
except ZeroDivisionError as ex:
	print("Hubo un error del tipo {}".format(ex))
except IndexError as ex:
	print("Hubo un error del tipo {}".format(ex))


# Cuando se desconoce el tipo de error, se puede usar un
# reconocimiento de error genérico o automático

try:
	print('6' + 10)
except Exception as ex:
	print("Hubo un error del tipo {}".format(ex))


# Utilización de bloque finally
# Lo del bloque finally siempre se ejecutará

try:
	print(10 + 10)
except Exception as ex:# Se ejecuta cuando existe un error
	print("Hubo un error del tipo {}".format(ex))
finally: # Siempre se ejecuta
	print("Se terminó el script")
