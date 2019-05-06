# Módulo calculadora


# Si siempre se utilizará como módulo este archivo
# Deberemos indicar el interprete con el cual se ejecutará el módulo

#!/usr/bin/python3

# Documentar módulo

"""
Este módulo contiene funciones matemátcas básicas
"""

# Se agregan metadatas
# Información del módulo

__author__ = "Rodrigo Vidal"
__copyright__ = "Copyright 2016, Código Facilito"
__credits__ = "Código Facilito"

__licence__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Rodrigo"
__email__  = "rodrigo.vidal.hq@gmail.com"
__status__ = "Developer"


def suma(num_uno,num_dos):
	"""Regresa el resultado de la súma de dos números"""
	return num_uno + num_dos


def resta(num_uno, num_dos):
	"""Retorna el resultado de la resta de dos números"""
	return num_uno - num_dos

def multiplicacion(num_uno,num_dos):
	"""Retorna el resultado de la multiplicación de dos números"""
	return num_uno * num_dos

def division(num_uno, num_dos):
	"""Retorna el resultado de la división de dos números"""
	return num_uno / num_dos


# Atributo NAME obtiene nombre de módulo
from calculadora_2_estructura_modulo import __name__ as __name_calc__

# Si es el principal, devovlerá main, de lo contrario, el nombre del archivo importado

print(__name__)
print(__name_calc__)