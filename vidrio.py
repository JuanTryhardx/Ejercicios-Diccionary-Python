from botella import Botella

# CLASE HIJA 1
class Vidrio(Botella):
    def __init__(self, capacidad, material, color):
        super().__init__(capacidad, material)
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, nuevo_datocolor):
        self._color = nuevo_datocolor

#POLISMORFISMO

    def ver_info(self):
        super().ver_info()
        print(f"Color: {self._color}")