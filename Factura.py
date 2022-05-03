class Factura():
    IdResivo: int
    Fecha: int
    Direccion: str
    ValorDeposito: int
    TipoCuenta: str
    #CONSTRUCTOR
    def __init__(self, Usuario, Cliente, Servicio, PagoOnline):
    self.Usuario = Usuario
    self.Cliente = Cliente
    self.Servicio = Servicio
    self.PagoOnline = PagoOnline

    def GenerarFactura(self, DatosCliente, Fecha, ValorDeposito, Producto, IdResivo):

    def EnviarFactura(self, DatosCliente)