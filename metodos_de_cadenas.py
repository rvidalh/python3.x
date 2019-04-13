# MÉTODOS DE CADENAS
from my_function import my_print

curso = "Curso"
impartidor = "Código Facilito"

# Método de concatenación FORMAT

salida = "{} de {}".format(curso, impartidor)
my_print(salida)

#Le daremos un alias a cada entrada, pará así identificar donde reemplazar el valor
salida = "{a} de {b} {a}".format(a = curso, b = impartidor)
my_print(salida)

# Convertir toda la cadena en minúscula

salida = salida.lower()
my_print(salida)

# Convertir toda la cadena a Mayúscula

salida = salida.upper()
my_print(salida)

# Formatear el string como un Titulo
# El método reemplaza la primera letra de cada palabra por la misma en mayúscula

salida = salida.title()
my_print(salida)


# Método para buscar una palabra o letra dentro de un string
# El método retorna la posición en donde comienza la palabra 
# que coincida con la búsqueda

string_busqueda = "Cadena de prueba Cadena"
resultado_busqueda = string_busqueda.find('prueba')
my_print(resultado_busqueda)

# Método para retornar la frecuencia en que se repite una palabra o letra

# Frecuencia de una letra
count_frecuencia = string_busqueda.count('e')
my_print(count_frecuencia)

# Frecuencia de una palabra
count_frecuencia = string_busqueda.count('Cadena')
my_print(count_frecuencia)


# Método de sustitución

# Método replace.
# El método reemplaza solamente coincidencia. En el ejemplo solamente
# sustituirá la letra 'a', pero no la que este en mayúscula o la que contiene acento.

cadena_sustitucion = "Alguna palabra será sustituida"
cadena_sustitucion = cadena_sustitucion.replace('a','x')
my_print(cadena_sustitucion)

cadena_sustitucion = "Alguna palabra palabra repetida"
cadena_sustitucion = cadena_sustitucion.replace('palabra', 'word')
my_print(cadena_sustitucion)

# Método split
# Realiza una separación de la cadena total, en subcadenas según el criterio dado
# En el ejemplo, separa la cadena por los espacios en blanco.
# Cada subcadena es agregada a una lista, que es lo que retorna el método

cadena_split = "Cadena para hacer split"
cadena_split = cadena_split.split(' ')

# Mediante un for, se imprime cada palabra de la cadena que generó el split
for elemento in cadena_split:
	my_print(elemento)
