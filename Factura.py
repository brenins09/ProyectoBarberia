from Cliente import Cliente
from Servicio import Servicio
from PagoOnline import PagoOnline
from Agendamiento import Agendamiento
from Administrador import Administrador

class Factura:
    #CONSTRUCTOR
    def __init__(self, datosCliente: Cliente, servicio: Servicio, PagoOnline: PagoOnline, idResivo: int, fecha: str, direccion: str, valorDeposito: int, tipoCuenta: str):
        self.datosCliente = datosCliente
        self.producto = servicio
        self.pagoOnline = PagoOnline
        self.idRecibo = idResivo
        self.fecha = fecha
        self.direccion = direccion
        self.valorDeposito = valorDeposito
        self.tipoCuenta = tipoCuenta

    def GenerarFactura(self):
        print("turno generado con exito")

    def EnviarFactura(self):
        print("factura enviada")

objetoCliente = Cliente("brenins@gmail.com", "create", "brenins", 1990, 101023456, 3147223526)

objetoServicio = Servicio(objetoCliente, 20000, "brenins")

objetoAdministrador = Administrador(bool, 21, "xiomara", "6 abril 2001", 107234, 32189234)

objetoAgendamiento = Agendamiento(objetoAdministrador, "10:45 am", "10 abril 2021", "nicolas saldarriaga", bool, objetoServicio)

objetoPagoOnline = PagoOnline(objetoCliente, objetoServicio, objetoAgendamiento, "bancolombia", 31399965, 653432, 40000, "jorge perez")

objetoFactura = Factura(objetoCliente, objetoServicio, objetoPagoOnline, 873864, "30 abril 2001", "calle 13 a 66", 20000, "ahorros")

#print(objetoFactura.idRecibo)