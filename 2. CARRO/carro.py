# CLASE PADRE
class Carro:

    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo

    # GETTERS

    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    # SETTERS
    def set_marca(self, nueva_marca):
        self._marca = nueva_marca

    def set_modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo

    def crear_carro(self):
        return "Carro creado correctamente"

    def ver_info(self):
        print(f"Marca: {self._marca}")
        print(f"Modelo: {self._modelo}")