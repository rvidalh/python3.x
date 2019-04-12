# STRINGS

#La declaración de un string puede ser como comillas dobles ("ejemplo") o simples ('ejemplo')
# Datos:
# string en comillas dobles, puede contener palabras encerradas en comillas simples
# string en comillas simples, puede contener palabras encerradas en comillas dobles


mi_string = "Hola Mundo!"
print(mi_string)

mi_string = 'Hola Mundo!'
print(mi_string)

# string con saltos de línea
# Texto con salto va dentro de triples comillas dobles o triples comillas simples.

mi_string = """Este string contiene un texto que incluye
saltos de línea. 
Ya no es necesario indicar el salto, si no, realizar un salto
en el texto escrito!
(También se puede utilizar el backslash+n)\nBye."""

print(mi_string)


# Concatenación de strings
nombre = 'Rodrigo'
apellido = "Vidal"

print("Mi nombre es " + nombre + " " + apellido)

# Otra forma de concatenar

mensaje_concat_1 = "Mi nombre es %s %s" %(nombre, apellido)
print(mensaje_concat_1)

#Otra forma más de concatenar

mensaje_concat_2 = "Mi nombre es {} {}".format(nombre, apellido)
print(mensaje_concat_2)

