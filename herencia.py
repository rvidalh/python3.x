# Herencia


print('Herencia \n')

class Animal: # Clase padre 1
	@property
	def terrestre(self):
		return True
	
class Felino(Animal): # Clase padre 2
	@property
	def garras_retractiles(self):
		return True

	def cazar(self):
		print("El felino está casando")

class Mascota:
	nombre = ''
	def mostrar_nombre(self):
		print(self.nombre)


class Gato(Felino, Mascota):
	def gato_cazador(self):
		self.cazar()
	def mostrar_nombre(self): # Sobreescritura de método
		Mascota.mostrar_nombre(self) # Ejecutrar mismo método de una clase padre
		print("El nombre del gato es {}".format(self.nombre))

class Jaguar(Felino):
	pass


gato = Gato()
jaguar = Jaguar()

print(gato.garras_retractiles)
print(gato.gato_cazador())
print(jaguar.garras_retractiles)
print(gato.terrestre)# se puede utilizar propiedas o métodos de la clase padre 1

print('\n')
print('Herencia Múltiple \n')

# Herencia Múltiple

# Herencia mútliple permite herdad de múltiples clases


gato_2 = Gato()
gato_2.nombre = "Cuchitu"
gato_2.mostrar_nombre()


# Override

print('\n')
print('Override \n')




class Animal2: # Clase padre 1
	@property
	def terrestre(self):
		return True
	
class Felino2(Animal2): # Clase padre 2
	@property
	def garras_retractiles(self):
		return True

	def cazar(self):
		print("El felino está casando")

class Mascota2:
	def __init__(self, nombre):
		self.nombre = nombre

	def mostrar_nombre(self):
		print(self.nombre)


class Gato2(Felino2, Mascota2):
	def __init__(self,nombre):
		Mascota2.__init__(self, nombre)
		self.nombre_gato = nombre

	def gato_cazador(self):
		self.cazar()
	def mostrar_nombre(self): # Sobreescritura de método
		Mascota2.mostrar_nombre(self) # Ejecutrar mismo método de una clase padre
		print("El nombre del gato es {}".format(self.nombre))


gato_3 = Gato2("Panchita")
#gato_3.nombre = "Groot"
gato_3.mostrar_nombre()

