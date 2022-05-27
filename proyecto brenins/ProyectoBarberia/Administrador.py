from Usuario import Usuario

class Administrador(Usuario):
    def __init__(self, Validacion: bool, Edad: int, nombre: str, fechaNacimiento: int, cedula: int, numeroTelefonico: int):
        super(). __init__(nombre, fechaNacimiento, cedula, numeroTelefonico)
        self.Validacion = Validacion
        self.Edad = Edad

    # METODOS
    def ResivirResultados(self, Resultado):
        print("resultados del mes abril: 2`000.000")

    def ValidarCapacitacion(self, Resultados):
        pass

    def HabilitarUsuarios(self, Usuario):
        pass

    def DeshabilitarUsuarios(self, Datos):
        pass

    def HabilitarAlertas(self, FechasEspeciales):
        pass

objetoAdmin = Administrador(bool, 21, "xiomara", "6 abril 2001", 107234, 32189234)

#print(objetoAdmin.nombre)