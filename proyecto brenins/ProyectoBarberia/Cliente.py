from Usuario import Usuario
from Alerta import Alerta

class Cliente(Usuario):
    def __init__(self, correo: str, contraseña: str, nombre: str, fechaNacimiento: int, cedula: int, numeroTelefonico: int):
        super(). __init__(nombre, fechaNacimiento, cedula, numeroTelefonico)
        self.correo = correo
        self.contraseña = contraseña

    #METODOS
    def ResivirAlertas(self, AlertaGenerada:Alerta):
        AlertaGenerada.GenerarAlertas()
        print("te ha llegado una alerta de barberia mi prmera cana")

    def ResivirComprobantePago(self, ComprobanPago):
        print("el comprobante ha llegado a tu cuenta con exito")

    def EnviarComprobante(self, ComprobantePago):
        print("el comprobante ha sido enviado con exito")

objetoGerar = Alerta()

objetoCliente = Cliente("brenins@gmail.com", "create", "brenins", 1990, 101023456, 3147223526)
#print(objetoCliente.ResivirAlertas(objetoGerar))
