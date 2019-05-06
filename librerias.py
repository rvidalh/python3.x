# Uso de librerias definidas

import random
import datetime
import sys
import time


# USO LIBRERIA RANDOM


# Valor random entre 0 y 10, inclusive
valor = random.randint(0,10)
print(valor)


# Valor aleatorio de una lista definida

lista = [True, "String", 67, False, "Hola"]
valor = random.choice(lista)

print(valor)


# Desordenar lista

print(lista)
random.shuffle(lista)
print(lista)


# USO LIBRERIA DATETIME

# Obtener hora

valor = datetime.datetime.now()
print(valor)


# USO LIBRERIA SYS

for i in range(100):
	# Se agrega delay
	time.sleep(0.5)
	sys.stdout.write("\r%d %%" % i)
	sys.stdout.flush()

