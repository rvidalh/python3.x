# Métodos de Clase

class Animal:
	volador = True

class Cocodrilo(Animal):

	def __init__(self,nombre):
		self.nombre = nombre

	@classmethod
	def new(cls, nombre): # Método perteneciente a la clase
		cls.volador = False
		return Cocodrilo(nombre)


cocodrilo = Cocodrilo.new('coco')

print(cocodrilo.nombre)
print(cocodrilo.volador)