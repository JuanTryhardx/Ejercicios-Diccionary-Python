from botella import Botella
from vidrio import Vidrio
from plastico import Plastico
from base_datos import Base_datos

bd_dt = Base_datos()

botella = Botella("1 L", "plastico")
print("-----------DATOS_BOTELLA-------------")
botella.ver_info()

vidrio = Vidrio("2 L", "vidrio", "gris")
print("\n-----------DATOS_BOTELLA_VIDRIO--------")
vidrio.ver_info()

plastico = Plastico("1 L", "plastico", "plastica")
print("\n-----------DATOS_BOTELLA_PLASTICO--------")
plastico.ver_info()

obj_base_dt.agregar_botella(obj_botella)
print(obj_botella)