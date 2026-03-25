from animal import Animal

# CLASE HIJA 5
class Pato(Animal):
    def __init__(self, nombre, tipo, puede_volar):
        super().__init__(nombre, tipo)
        self._puede_volar = puede_volar

    def get_puede_volar(self):
        return self._puede_volar

    def set_puede_volar(self, nuevo_valor):
        self._puede_volar = nuevo_valor

    # POLIMORFISMO
    def ver_info(self):
        super().ver_info()
        print(f"Puede volar?: {self._puede_volar}")