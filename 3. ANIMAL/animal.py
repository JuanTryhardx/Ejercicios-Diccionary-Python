#CLASE PADRE

class Animal:
    def __init__(self, nombre, tipo):
        self._nombre = nombre
        self._tipo = tipo
        
    #GETTERS
    def get_nombre(self):
        return self._nombre
    
    def get_tipo(self):
        return self._material
    
    #SETTERS
    def set_nombre(self, nuevo_nom):
        self._nombre = nuevo_nom
        
    def set_tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo
        
    def crear_animal(self):
        info = (f"Animal creado")
        return info
    
    def ver_info(self):
        print(f"El nombre es: {self._nombre}")
        print(f"El tipo es: {self._tipo}")