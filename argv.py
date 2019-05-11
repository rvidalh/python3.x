
# ARGV
# Se reciben argumentos que vienen al ejecutar un script

import sys

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print('Es necesario al menos 1 agumento')
	else:
		if sys.argv[1] == 'help':
			print('Texto de prueba')
		