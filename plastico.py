from botella import Botella

#CLASE HIJA 2 
class Plastico(Botella):
  def __init__(self, capacidad, material, tipo_tapa):
        super().__init__(capacidad, material)
        self._tipo_tapa = tipo_tapa

  def get_tipo_tapa(self):
    return self._tipo_tapa

  def set_tipo_tapa(self, nuevo_datot):
        self._tipo_tapa = nuevo_datot

  #POLIMORFISMO
  def ver_info(self):
        super().ver_info()
        print(f"Tipo de Tapa: {self._tipo_tapa}")
