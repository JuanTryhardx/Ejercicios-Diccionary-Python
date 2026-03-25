from animal import Animal
from caballo import Caballo
from cocodrilo import Coco
from pez import Pez
from escarabajo import Escarabajo
from pato import Pato
from bd import Base_datos

bd = Base_datos()

animal = Animal("pepito", "terrestre")
caballo = Caballo("spirit", "terrestre", "120 km/h")
coco = Coco("coquito", "reptil", "rios y pantanos")
pez = Pez("rex", "aguatero", "  salada")
escarabajo = Escarabajo("Eskiu", "terrestre", "negro")
pato = Pato("donal", "terrestre", "si, un poco")

print("-----------DATOS_ANIMAL-------------")
animal.ver_info()

print("\n-----------DATOS_ANIMAL_CABALLO--------")
caballo.ver_info()

print("\n-----------DATOS_ANIMAL COCODRILO--------")
coco.ver_info()

print("\n-----------DATOS_ANIMAL PEZ--------")
pez.ver_info()

print("\n-----------DATOS_ANIMAL ESCARaBAJo--------")
escarabajo.ver_info()

print("\n-----------DATOS_ANIMAL PATO--------")
pato.ver_info()


#AGREGAR lA BASE DE DATOS
bd.agregar_animal(animal)
bd.agregar_animal(caballo)
bd.agregar_animal(coco)
bd.agregar_animal(pez)
bd.agregar_animal(escarabajo)
bd.agregar_animal(pato)


print("\n -----VER TODAS------")
bd.ver_todos()

#actualizar capacidad
print("\n--- ACTUALIZAR ID 1 ---")
bd.actualizar_tipo(1, "aereo")

#eliminar
print("\n--- ELIMINAR ID 3 ---")
bd.eliminar_animal(3)

#final
print("\n--- BASE DE DATOS FINAL ---")
bd.ver_todos()