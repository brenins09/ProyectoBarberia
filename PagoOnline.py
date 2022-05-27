from Cliente import Cliente
from Servicio import Servicio
from Agendamiento import Agendamiento
from Administrador import Administrador

class PagoOnline():

    def __init__(self, datosCliente: Cliente, servicio: Servicio, agendamiento: Agendamiento, entidadBancaria: str, numeroCuenta: int, password: int, valorDeposito: int, destinatario: str):
        self.datosCliente = Cliente
        self.servicio = servicio
        self.agendamiento = agendamiento
        self.EntidadBancaria = entidadBancaria
        self.numeroCuenta = numeroCuenta
        self.password = password
        self.valorDeposito = valorDeposito
        self.destinatario = destinatario

    #METODOS
    def GenerarComprobantePago(self):
        print("comprobante de pago")

    def EnviarComprobante(self, ComprobantePago: GenerarComprobantePago):
        print("enviado con exito! ")

objetoCliente = Cliente("brenins@gmail.com", "create", "brenins", 1990, 101023456, 3147223526)

objetoServicio = Servicio(objetoCliente, 20000, "brenins")

objetoAdministrador = Administrador

objetoAgendamiento = Agendamiento(objetoAdministrador, "10:45 am", "10 abril 2021", "nicolas saldarriaga", bool, objetoServicio)

objetoPagoOnline = PagoOnline(objetoCliente, objetoServicio, objetoAgendamiento, "bancolombia", 31399965, 653432, 40000, "jorge perez")

#print(objetoPagoOnline.password)