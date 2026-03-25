from animal import Animal

#CLASE HIJA 2
class Coco(Animal):
    def __init__(self, nombre, tipo, habitad):
        super().__init__(nombre, tipo)
        self._habitad = habitad
        
    def get_habitad(self):
        return self._habitad
    
    def set_habitad(self, nuevo_h):
        self._habitad = nuevo_h
        
    def ver_info(self):
        super().ver_info()
        print(f"Su Habitad es: {self._habitad}")