class Base_datos:
#CRUD:
    def __init__(self):
        self.lista_botellas = []
        
    def agregar_botella(self, nuevo_obj):
        self.lista_botellas.append(nuevo_obj)
        print(nuevo_obj)
        print(f"Botella agregada en posicion {len(self.lista_botellas) -1}")
        
    def buscar_botella(self, indice):
        if 0 <= indice < len(self.lista_botellas):
            print(f"\n Botella en posicion {indice}: ")
            self.lista_botellas[indice].ver_info()
            return self.lista_botellas[indice]
        else:
            print(f" No existe botella en esa posicion {indice}")
            return None
        
    def actualizar_capacidad(self, indice, nueva_capacidad):
        botella = self.buscar_botella(indice)
        if botella:
            botella.set_capacidad(nueva_capacidad)
            print(f"capacidad actualizada a: {nueva_capacidad}")
            
    def eliminar_botella(self, indice):
        if 0 <= indice < len(self.lista_botellas):
            self.lista_botellas.pop(indice)
            print(f"Botella en posicion {indice} eliminada.")
        else: 
            print(f"No existe botella en posicion {indice}")                   
            
        
        