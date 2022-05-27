
from Servicio import Servicio
from Administrador import Administrador

class Agendamiento:
    #CONSTRUCTOR
    def __init__(self, datosAdministrdor: Administrador, horaDelTurno: str, fechaDelTurno: str, tipoDeBarbero: str, medioDePago: bool, servicio: Servicio):
        self.datosAdministrador = datosAdministrdor
        self.horaDelTurno = horaDelTurno
        self.fechaDelTurno = fechaDelTurno
        self.tipoDeBarbero = tipoDeBarbero
        self.medioDePago = medioDePago
        self.servicio = servicio

    #METODOS
    def GenerarTurnos(self):
        print("turno generado")
    
    def EnviarNotificacion(self):
        print("notificacion enviada")

    def CancelarCitas(self):
        print("cita cancelada")
    
    def ClasificarPago(self):
        print("pago clasificado")

objetoAdministrador = Administrador

objetoServicio = Servicio

objetoAgendamiento = Agendamiento(objetoAdministrador, "10:45 am", "10 abril 2021", "nicolas saldarriaga", bool, objetoServicio)

#print(objetoAgendamiento.tipoDeBarbero)