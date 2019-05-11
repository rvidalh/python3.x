# Variables de Clase

class Circulo():
	# Variable de clase
	# Éstas no son inmutables
	pi = 3.1416

	def __init__(self, radio):
		self.radio = radio

	def area(self):
		return self.radio * self.radio * self.pi


circulo_uno = Circulo(4)
circulo_dos = Circulo(3)

print(circulo_uno.radio)
print(circulo_dos.radio)
print(Circulo.pi)# Impresión de variable de clase

# __dict__ retorna un diccionario con todos los atributos de la clase
# a excepción de la variable de clase

print(circulo_uno.__dict__)

print(circulo_uno.area())

