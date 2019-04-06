#Tipos de números en python.
# Enteros = {10, 2, 545, 1223, -34, -54, 10000000, etc.}.
# Flotas = {9.4; -19.43; 123.455444; etc.}.
# Boleanos = V(1), F(0).
# Complex = No se verán en este documento.


#Suma
numero_uno = 54
numero_dos = 66
resultado= numero_uno + numero_dos

print("El resultado de la suma es: ", resultado)


#Resta
resultado = numero_dos - numero_uno

print("El resultado de la resta es: ", resultado)

#Multiplicación
resultado = numero_uno * numero_dos

print("El resultado de la multiplicación es: ", resultado)

#División
numero_uno = 2

#Casteo para que el resultado sea un entero
resultado = int(numero_dos / numero_uno)

#Se agrega el tipo de dato resultante
print("El resultado de la división es: ", resultado, type(resultado))

