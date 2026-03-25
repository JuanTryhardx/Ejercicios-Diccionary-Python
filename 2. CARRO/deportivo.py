from carro import Carro

# CLASE HIJA 1
class Deportivo(Carro):
    def __init__(self, marca, modelo, velocidad_max):
        super().__init__(marca, modelo)
        self._velocidad_max = velocidad_max

    def get_velocidad_max(self):
        return self._velocidad_max

    def set_velocidad_max(self, nueva_velocidad):
        self._velocidad_max = nueva_velocidad

    #POLIMORFISMO
    def ver_info(self):
        super().ver_info()
        print(f"Velocidad máxima: {self._velocidad_max}")