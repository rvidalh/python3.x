# Clases, objetos, Atributos y métodos

# Creación de clase

class Lapiz:
	#Atributos
	color = "Rojo"
	contiene_borrador = False
	usa_grafito = True

	#Métodos
	# Self: para indicar que es perteneciente de la clase
	# Y se pueden utilizar sus atributos y métodos
	def dibujar(self):
		print("El lápiz dibujó.")
	# Métodos dentro de métodos
	def borrar(self):
		if self.es_valido_para_borrar():
			print("El lápiz borró.")
		else:
			print("El lápiz no tiene borrador.")
	def es_valido_para_borrar(self):
		return self.contiene_borrador
	#Si se quiere llamar a un método desde otro método


# Creación de objeto
lapiz_generico = Lapiz()


# Utilización de Atributos

print(lapiz_generico.color)
print(lapiz_generico.contiene_borrador)
print(lapiz_generico.usa_grafito)


# Ejecución del método dibujar, perteneciente a la clase Lapiz
lapiz_generico.dibujar()
lapiz_generico.borrar()

# Métodos Privados y métodos públicos

# Si se quiere que algun atributo no se modifiqué
# luego se ser creado el objeto, se debe crear un atributo privado
# Estos solo serán modificados por la clase y no por la instancia del objeto
# El atributo privado se crea asignado doble guión bajo delante del nombre del
# atributo. Ej: __nombre_atributo.
# El atributo podrá ser accesado solo desde la clase misma que lo posee


class Usuario:
	def __init__(self, username, password, email):
		self.username = username
		self.__password = self.__generar_password(password)# Atributo privado
		self.email = email

	def __generar_password(self, password):
		return password.upper()
		# Si se quiere crear un método privado, también se indíca con doble
		# guión bajo ej: __nombre_metodo

	# Retorna atributo privado
	def get_password(self):
		return self.__password


usuario = Usuario('rvidalh','rvidalh123','rodrigo@vidal.com')



print(usuario.username)
#usuario.__password = 'vidalhrodrigo123'
#print(usuario.password)
print(usuario.email)
print(usuario.get_password())



# Métodos Estáticos


class Circulo():

	@staticmethod # Solo le pertenece a la clase y no a la instancia
	def pi():# Método estático no contiene el argumento self
		return 3.1416

	def __init__(self, radio):
		self.radio = radio

	def area(self):# Método de instancia, contiene la palabra self (un objeto puede llamarlo)
		return self.radio * self.radio * self.pi()


circulo_uno = Circulo(4)
circulo_dos = Circulo(3)

print(Circulo.pi())
print(circulo_uno.pi())
print(circulo_uno.area())

