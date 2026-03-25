from carro import Carro

# CLASE HIJA 3
class Buseta(Carro):
    def __init__(self, marca, modelo, pasajeros):
        super().__init__(marca, modelo)
        self._pasajeros = pasajeros

    def get_pasajeros(self):
        return self._pasajeros

    def set_pasajeros(self, nuevos_pasajeros):
        self._pasajeros = nuevos_pasajeros

    # POLIMORFISMO
    def ver_info(self):
        super().ver_info()
        print(f"Cantidad de pasajeros: {self._pasajeros}")