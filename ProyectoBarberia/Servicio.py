from ProyectoBarberia.Cliente import Cliente

class Servicio():
    #CONSTRUCTOR
    def __init__(self, datosCliente:Cliente, precio: int, nombre: str):
        self.datosCliente = datosCliente
        self.precio = precio
        self.nombre = nombre

    #METODOS
    def CalcularPrecio(self):
        print("precio 25.000")

    def AplicarDescuentos(self):
        print("descuento aplicado")
    
    def GenerarCoprobante(self):
        print("comprobante generado")