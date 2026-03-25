class Base_datos:
#CRUD
    def __init__(self):
        self.lista_carros = []
        
    def agregar_carro(self, nuevo_obj):
        self.lista_carros.append(nuevo_obj)
        print(nuevo_obj)
        print(f"Carro agregado en posicion {len(self.lista_carros) -1 }")
        
    def ver_todos(self):
        if not self.lista_carros:
            print("la base de datos esta vacia.")
            return
        print("\n------------------BASE DE DATOS------------------")
        for i in range(len(self.lista_carros)):
            print(f"\n Posicion: {i}")
            self.lista_carros[i].ver_info()
            print("-----------------------------------------------")
            
    def buscar_carro(self, indice):
        if 0 <= indice < len(self.lista_carros):
            print(f" Botella en posicion: {indice}: ")
            self.lista_carros[indice].ver_info()
            return self.lista_carros[indice]
        else:
            printf(f"No existe carro en posicion {indice}")
            return None
        
    def actualizar_modelo(self, indice, nuevo_modelo):
        carro = self.buscar_carro(indice)
        if carro:
            carro.set_modelo(nuevo_modelo)
            print(f"Capacidad actualizada a: {nuevo_modelo}")
            
    def eliminar_carro(self, indice):
        if 0 <= indice < len(self.lista_carros):
            self.lista_carros.pop(indice)
            print(f"Carro en posicion {indice} eliminado")
        else:
            print(f"No existe carro en posicion {indice}")       