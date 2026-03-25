# CLASE PADRE
class Botella:

    def __init__(self, capacidad, material):
        self._capacidad = capacidad
        self._material = material

    # GETTERS
    def get_capacidad(self):
        return self._capacidad

    def get_material(self):
        return self._material

    # SETTERS
    def set_capacidad(self, nuevo_datoc):
        self._capacidad = nuevo_datoc

    def set_material(self, nuevo_datom):
        self._material = nuevo_datom

    def crear_botella(self):
      info = (f"Botella Creada")
      return info

    def ver_info(self):
      print(f"la capacidad es: {self._capacidad}")
      print(f"material es: {self._material}")