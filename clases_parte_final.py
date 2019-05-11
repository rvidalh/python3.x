# Clases Parte Fianl

class Usuario:
	def __init__(self):
		self.__password = "Secret"

	def mostrar_password(self):
		print(self.__password)


usuario = Usuario()

# Se crea atributo fuera de la clase
# usuario.nombre = "Rodrigo"
#print(usuario.nombre) # Se crea atributo fuera de la clase
#print(usuario.__dict__)



usuario.__password = "No Secret"
print(usuario.__password)
print(usuario.__dict__)
usuario.mostrar_password()


print("\n")

# Métodos mágicos o especiales

class Usuario2:
	def __new__(cls):
		print("Este método es primero en ejecución")
		return super().__new__(cls)

	def __init__(self):
		print("Este método es segundo en ejecución")

	# Sobre escribe el método que me retorna el objeto
	# de lo contrario, si queremos acceder a él, muestra el espacio de memoria
	def __str__(self):
		return "Se imprime cuando intento mostrar objeto"

	# Método para indicar que no fue posible encontrar un atributo X en el objeto
	def __getattr__(self, nombre_atributo):
		print("No se encontró el atributo")
		self.otro_metodo()

	def otro_metodo(self):
		print("Otro método")



usuario2 = Usuario2()
print(usuario2)

print(usuario2.apellido)