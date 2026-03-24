class Base_datos:
#CRUD:
    def __init__(self):
        self.lista_botellas = []
        
    def agregar_botella(self, nuevo_obj):
        self.lista_botella.append(nuevo_obj)
        print(nuevo_obj)
        print(self.lista_botella[0])
        
        