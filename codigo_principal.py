from botella import Botella
from vidrio import Vidrio
from plastico import Plastico
from base_datos import Base_datos

bd_dt = Base_datos()

botella = Botella("1 L", "plastico")
vidrio = Vidrio("2 L", "vidrio", "gris")
plastico = Plastico("1 L", "plastico", "plastica")



print("-----------DATOS_BOTELLA-------------")
botella.ver_info()

print("\n-----------DATOS_BOTELLA_VIDRIO--------")
vidrio.ver_info()

print("\n-----------DATOS_BOTELLA_PLASTICO--------")
plastico.ver_info()

#AGREGAR lA BASE DE DATOS
bd_dt.agregar_botella(botella)
bd_dt.agregar_botella(vidrio)
bd_dt.agregar_botella(plastico)

print("\n -----VER TODAS------")
bd_dt.ver_todas()

#actualizar capacidad
print("\n--- ACTUALIZAR ID 1 ---")
bd_dt.actualizar_capacidad(1, "3 L")

#eliminar
print("\n--- ELIMINAR ID 3 ---")
bd_dt.eliminar_botella(3)

#final
print("\n--- BASE DE DATOS FINAL ---")
bd_dt.ver_todas()