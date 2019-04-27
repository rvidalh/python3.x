from my_function import my_print

#FOR LO UTILIZAREMOS CUANDO TENGAMOS CONOCIMIENTO DE LA CANTIDAD DE ITERACIONES

#Nos permitirá iterar objetos iterables, listas, tuplas, strings.

lista = [1,2,3,4,5,6,7,8,9,10]

# No ha sido necesario indicar un índice para indicar la posición actual
for valor in lista:
	my_print(valor)


# se crea un objeto con valores numéricos desde el 0 al 9
# range(x,y) x: desde; y: hasta --> entrega un objeto iterable
nuevo_rango = range(0,10)
for valor in nuevo_rango:
	my_print(valor)

# Si range() solamente lleva 1 parámetro, se obtendrá un objeto iterable
# dsde la posición 0, hasta la que se indique como único parámetro

nuevo_rango2 = range(15)
for valor in nuevo_rango2:
	my_print(valor)

# Si range(x,y,z) contiene 3 parámetros, el desgloce sería el siguiente_
# x: desde; y: hasta; z: saltos entre valores

nuevo_rango3 = range(0,21,2)
for valor in nuevo_rango3:
	my_print(valor)


# For con rango como parámetro

for valor in range(0,21,5):
	my_print(valor)


# manejar el índice de x valor apoyandonos de una variable

indice = 0
for valor in lista:
	print("{} tiene el índice {}".format(valor, indice))
	indice += 1


print("---------------------------")

# manejar el índice de x valor apoyandonos de la funcion enumerate()
for indice, valor in enumerate(lista):
	print("{} tiene el índice {}".format(valor,indice))

print("---------------------------")


# Reconocer el tamaño de una lista
# len(x) ---> retorna la cantidad de valores dentro de algún objeto iterable

my_print("La lista contiene {} elementos".format(len(lista)))

print("---------------------------")

# For con límite  el largo de la lista
for valor in range(0,len(lista)):
	my_print(valor)

# imprimir un string

for valor in "Curso":
	my_print(valor)


# Recorrido de un diccionario

diccionario = { 'a': 10, 'b' : 20, 'c' : 30, 'd' : 31}


# diccionario.items() nos retorna la llave y el valor
# diccionario.keys() nos retorna solo la llave
# diccionarios.values() nos retorna los valores

for llave,valor in diccionario.items():
	print("La llave ", llave, " tiene el valor de", valor)