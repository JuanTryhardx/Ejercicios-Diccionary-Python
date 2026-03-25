from carro import Carro
from deportivo import Deportivo
from camion import Camion
from buseta import Buseta
from bd import Base_datos

bd_dt = Base_datos()

carro = Carro("Toyota", "2025")
deportivo = Deportivo("ferrary", "F8", "340 km/h")
camion = Camion("Volvo", "FH", "20 Toneladas")
buseta = Buseta("Mercedez Benz", "Sprinter", "25")


print("--------------DATOS CARRO----------------")
carro.ver_info()

print("-------------DATOS_CARRO_DEPORTIVO-------")
deportivo.ver_info()

print("-------------DATOS_CARRO_CAMION----------")
camion.ver_info()

print("-------------DATOS_CARRO_BUSETA----------")
buseta.ver_info()

bd_dt.agregar_carro(carro)
bd_dt.agregar_carro(deportivo)
bd_dt.agregar_carro(camion)
bd_dt.agregar_carro(buseta)

print("\n -------VER TODOS--------")
bd_dt.ver_todos()

print("\n ----ACTURALIZAR ID 1------")
bd_dt.actualizar_modelo(1, "2026 ")

print("\n ------ELIMINAR ID 3 ------")
bd_dt.eliminar_carro(3)

print("\n ---BASE DE DATOS FINAL----")
bd_dt.ver_todos()