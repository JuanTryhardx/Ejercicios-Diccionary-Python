from animal import Animal

#CLASS HIJA 3
class Pez(Animal):
    def __init__(self, nombre, tipo, tipo_agua):
        super().__init__(nombre, tipo)
        self._tipo_agua = tipo_agua
        
    def get_tipo_agua(self):
        return self._tipo_agua
    
    def set_tipo_agua(self, nuevo_t_a):
        self._tipo_agua = nuevo_t_a
        
    def ver_info(self):
        super().ver_info()
        print(f"Tipo de Agua: {self._tipo_agua}")
    
