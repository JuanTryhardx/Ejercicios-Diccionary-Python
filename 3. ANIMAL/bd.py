class Base_datos:
#CRUD
    def __init__(self):
        self.lista_animal = []
        
    def agregar_animal(self, nuevo_obj):
        self.lista_animal.append(nuevo_obj)
        print(nuevo_obj)
        print(f"Animal agregado en posicion {len(self.lista_animal) -1 }")
        
    def ver_todos(self):
        if not self.lista_animal:
            print("la base de datos esta vacia.")
            return
        print("\n------------------BASE DE DATOS------------------")
        for i in range(len(self.lista_animal)):
            print(f"\n Posicion: {i}")
            self.lista_animal[i].ver_info()
            print("-----------------------------------------------")
            
    def buscar_animal(self, indice):
        if 0 <= indice < len(self.lista_animal):
            print(f" animal en posicion: {indice}: ")
            self.lista_animal[indice].ver_info()
            return self.lista_animal[indice]
        else:
            printf(f"No existe animal en posicion {indice}")
            return None
        
    def actualizar_tipo(self, indice, nuevo_tipo):
        animal = self.buscar_animal(indice)
        if animal:
            animal.set_tipo(nuevo_tipo)
            print(f"tipo actualizado a: {nuevo_tipo}")
            
    def eliminar_animal(self, indice):
        if 0 <= indice < len(self.lista_animal):
            self.lista_animal.pop(indice)
            print(f"animal en posicion {indice} eliminado")
        else:
            print(f"No existe animal en posicion {indice}")       