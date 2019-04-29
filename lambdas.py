from my_function import my_print

# LAMBDAS

# Lamba nos sirve para poder crear funciones anónimas en una linea de código

# funcion = lambda valor_1, valor_2, valor_n : acción a ejecutar

mi_funcion = lambda val_1, val_2 : val_1 + val_2

resultado = mi_funcion(10,15)

my_print(resultado)


mi_funcion_2 = lambda sentencia : '¿{}?'.format(sentencia)

resultado = mi_funcion_2('es esto una pregunta')
my_print(resultado)

# Las lambdas deben de ejecutar alguna acción

mi_funcion_3 = lambda : print('ejecucción de algo')

resultado = mi_funcion_3()
my_print(resultado)