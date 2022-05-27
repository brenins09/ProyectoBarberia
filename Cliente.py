from ProyectoBarberia.Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, correo: str, contraseña: str):
        super(). __init__("Cliente")
        self.correo = correo
        self.contraseña = contraseña

    #METODOS
    def ResivirAlertas(self, AlertaGenerada, DatosCliente):
        print("te ha llegado una alerta de barberia mi prmera cana")

    def ResivirComprobantePago(self, ComprobanPago, DatosCliente):
        print("el comprobante ha llegado a tu cuenta con exito")

    def EnviarComprobante(self, ComprobantePago, DatosAdministrador):
        print("el comprobante ha sido enviado con exito")