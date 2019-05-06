from my_function import my_print

# DECORADORES

# Es una función, que recibe como parámetro otra función, que retorna otra función
# A, B, C son funciones ---> A recibe como parámetro a B para poder crear C

def decorador(func): # A, B
	def nueva_funcion(*args,**kwargs):
		my_print("Inicio ejecución función")
		func(*args,**kwargs)
		my_print("Término de ejecución función")
	return nueva_funcion # C

@decorador
def saludo():
	my_print("Hi!")

@decorador
def suma(n_1,n_2):
	my_print(n_1 + n_2)


saludo()
suma(80, 20)


# Decorador con return
def decorador2(func): # A, B
	def inicio_msg():
		my_print("Inicio process")

	def fin_msg():
		my_print("Fin process")

	def nueva_funcion(*args,**kwargs):
		inicio_msg()
		result = func(*args,**kwargs)
		fin_msg()
		return result
	return nueva_funcion # C

@decorador2
def suma2(v_1, v_2):
	return v_1 + v_2

resultado = suma2(10,50)
my_print(resultado)


# Decorador con parámetros
def decorador3(is_valid):
	def _decorador3(func):
		def msg_ini():
			my_print("Inicio...")
		def msg_fin():
			my_print("Fin...")

		def nueva_funcion(*args, **kwargs):
			msg_ini()
			resultado = 0
			if is_valid:
				resultado = func(*args, **kwargs)
			msg_fin()
			return resultado
		return nueva_funcion
	return _decorador3

@decorador3(is_valid = True)
def suma2(v_1, v_2 , v_3):
	return v_1 + v_2 + v_3

resultado = suma2(10,50, 100)
my_print(resultado)