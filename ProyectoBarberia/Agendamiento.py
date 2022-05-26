
from ProyectoBarberia.Servicio import Servicio
from ProyectoBarberia.Administrador import Administrador

class Agendamiento():

    #CONSTRUCTOR
    def __init__(self, administrador:Administrador, horaDelTurno: str, fechaDelTurno: str, tipoDeBarbero: str, medioDePago: bool, servicio: Servicio):
        self.datosAdministrador = administrador
        self.horaDelTurno = horaDelTurno
        self.fechaDelTurno = fechaDelTurno
        self.tipoDeBarbero = tipoDeBarbero
        self.medioDePago = medioDePago
        self.servicio = servicio

    #METODOS
    def GenerarTurnos(self):
        print("turno generado")
    
    def EnviarNotificacion(self, DatosAdministrador):
        print("notificacion enviada")

    def CancelarCitas(self):
        print("cita cancelada")
    
    def ClasificarPago(self):
        print("pago clasificado")
objetoAgendamiento = Agendamiento("10:45 am", "10 abril 2021", "nicolas saldarriaga", "pago en linea")
print(objetoAgendamiento.horaDelTurno)