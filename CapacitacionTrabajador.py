
from Administrador import Administrador


class CapacitacionTrabajador:
     def __init__(self, experienciaLaboral:str, cuestionario:str, administrador:Administrador ): 
        self.experienciaLaboral = experienciaLaboral
        self.cuestionario = cuestionario
        self.administrador = administrador
     
     #Metodos
     def RealizarExamen(self):
         print("ExamenRealizado")

     def CalcularPuntuacion(self):
         print("Puntuacion Calculada")

     def EnviarResultados(self):
         print("Resultado enviado")

objetoAdmin = Administrador(bool, 21, "xiomara", "6 abril 2001", 107234, 32189234)

objetoCapacitacionTrabajador = CapacitacionTrabajador("5 años", "preguntas", objetoAdmin)

#print(objetoCapacitacionTrabajador.CalcularPuntuacion())