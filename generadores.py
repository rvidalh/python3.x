from my_function import my_print

# GENERADORDES
# Los generadores permiten crear objetos, sin necesidad de almacenarlos
# en la memoria RAM


def generador(*args):
	for valor in args:
		yield valor * 10, True

# Si indicaramos un return, en el ejemplo de arriba,
# daría error, ya que no retorna un valor iterable, por lo
# que se utilizará yield, lo que devuelve un valor iterable
# Yienld puede retornar más de un valor, yield se utiliza para los generadores.



for valor_1, valor_2 in generador(1,2,3,4,5,6,7,8,9):
	my_print(("{} {}".format(valor_1, valor_2)))