# Properties


class Usuario:
	def __init__(self, username, password, email):
		self.username = username
		self.__password = self.__generar_password(password)# Atributo privado
		self.email = email

	def __generar_password(self, password):
		return password.upper()
		# Si se quiere crear un método privado, también se indíca con doble
		# guión bajo ej: __nombre_metodo

	# Declaro una propiedad que me devolverá un valor privado
	# Solo devuelve el valor
	@property
	def password(self):
		return self.__password
	# Declaración de un setter, para modificar datos de la clase
	@password.setter
	def password(self,valor):
		self.__password = self.__generar_password(valor)
	

usuario = Usuario('rvidalh','rvidalh123','rodrigo@vidal.com')

print(usuario.password)
usuario.password = "Nueva Pass"
print(usuario.password)