class TinyIntError(Exception):
	def __init__(self):
		self.message = "El número no corresponde a un tinyInt"
	def __str__(self):
		return self.message