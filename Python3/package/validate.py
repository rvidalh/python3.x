def validate_tiny_int(valor):
	return valor >= 0 and valor <= 255


def validate_val(valor): #Valida si la entrada es numerica
	try:
		return isinstance(int(valor), int)
	except ValueError as error:
		return False


def call_back_function():
	print("Se ejecuta cuando existe un error")