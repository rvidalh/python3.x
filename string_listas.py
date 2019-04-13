# STRINGS COMO LISTAS

# String es una lista de carácteres
# En Python las listas comienzas en posición 0

mi_string = 'Curso de código facilito "Strings como listas".'
print(mi_string)


# Impresión de la letra en la posición indicada
# mi_string[posicion_de_la_letra]
# Dato: Los espacios cuentan como carácteres

print(mi_string[0])
print(mi_string[5])


# Obtener caŕacter desde derecha a izquierda
# mi_string[-posicion_de_la_letra]

print(mi_string[-1])
print(mi_string[-5])

# Otra forma de leer string de derecha a izquierda

print("Cadena de derecha a izquierda: " + mi_string[::-1])


# Obtener un extracto desde un string
# mi_string[indice_caracter_inicio:indidce_caracter_final]
# Observación: en el caso de obtener extracto, el indice_caracter_inicio
# parte desde la posición 1, es decir, si se quiere obtener desde el primer caracter
# debería escribirse mi_string[1:x]

print(mi_string[0:14])

# Obtener extracto desde un string, pero, en esta caso, caracter por medio
# pero es posible indicar cada cuanto caracteres me muestre uno
# mi_string[indice_caracter_inicio:indidce_caracter_final:secuencia]

print(mi_string[0:15:2])


#Función trim

mi_string = "  Cadena de prueba   "
string_trim = mi_string.strip()
print(string_trim, '-')