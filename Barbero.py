from Usuario import Usuario
from CapacitacionTrabajador import CapacitacionTrabajador
from Administrador import Administrador

class Barbero(Usuario):
   def __init__(self, numeroDeCorte:int, precioCorte:int, capacitacionTrabajador:CapacitacionTrabajador, fechaNacimiento:str, cedula:int, numeroTelefonico:int, nombre:str):
        super(). __init__(fechaNacimiento, cedula, numeroTelefonico, nombre)
        self.NumeroDeCorte = numeroDeCorte
        self.PrecioCorte = precioCorte
        self.CapacitacionTrabajador = CapacitacionTrabajador

        #METODOS
        def CalcularPromedioDiario(self, NumeroDeCorte, PrecioCorte):
            print("promedio calculado")

objetoAdmin = Administrador(bool, 21, "xiomara", "6 abril 2001", 107234, 32189234)
objetoCapacitacionTrabajador = CapacitacionTrabajador("5 años", "preguntas", objetoAdmin)

objetoBarbero = Barbero(10, 20000, objetoCapacitacionTrabajador, "06 abril 2001", 101838, 314723526, "nicolas gray")