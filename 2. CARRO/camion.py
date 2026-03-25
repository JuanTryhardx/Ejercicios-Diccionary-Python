from carro import Carro

# CLASE HIJA 2
class Camion(Carro):
    def __init__(self, marca, modelo, capacidad_carga):
        super().__init__(marca, modelo)
        self._capacidad_carga = capacidad_carga

    def get_capacidad_carga(self):
        return self._capacidad_carga

    def set_capacidad_carga(self, nueva_capacidad):
        self._capacidad_carga = nueva_capacidad

    # POLIMORFISMO
    def ver_info(self):
        super().ver_info()
        print(f"Capacidad de carga: {self._capacidad_carga}")
