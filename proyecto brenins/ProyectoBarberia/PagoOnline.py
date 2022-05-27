class PagoOnline():
    EntidadBancaria: str
    NumeroCuenta: int
    Password: int
    ValorDeposito: int
    Destinatario: str

    def __init__(self, Usuario, Servicio, Agendamiento):
    self.Usuario = Usuario
    self.Servicio = Servicio
    self.Agendamiento = Agendamiento

    #METODOS
    def GenerarCoprobantePago(self, DatosCliente, Destinatario, ValorDeosito, Servicio):

    def EnviarComprobante(self, DatosCliente, ComprobanteServicio):