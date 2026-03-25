from animal import Animal
#CLASE HIJA 1

class Caballo(Animal):
    def __init__(self, nombre, tipo, velocidad):
        super().__init__(nombre, tipo)
        self._velocidad = velocidad
        
    def get_velocidad(self):
        return self._velocidad
    
    def set_velocidad(self, nuevo_v):
        self._velocidad = nuevo_v
        
    def ver_info(self):
        super().ver_info()
        print(f"Velocidad: {self._velocidad}")
        
    
    