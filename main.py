# File para el aprendizaje sobre el uso de paquetes

from animals import Gato
from animals import creador_gatos

gato = Gato('Nuevo gato por paquete')
print(gato.nombre)

gato2 = creador_gatos("Nuevo gato")
print(gato2.nombre)  

print (gato.comer())