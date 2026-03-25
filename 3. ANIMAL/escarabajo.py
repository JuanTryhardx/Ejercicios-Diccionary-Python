from animal import Animal

# CLASE HIJA 4
class Escarabajo(Animal):
    def __init__(self, nombre, tipo, color):
        super().__init__(nombre, tipo)
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, nuevo_color):
        self._color = nuevo_color

    # POLIMORFISMO
    def ver_info(self):
        super().ver_info()
        print(f"Color: {self._color}")