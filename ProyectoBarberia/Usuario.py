class Usuario():
    
    def __init__(self, nombre: str, fechaNacimiento: int, cedula: int, numeroTelefonico: int):
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento
        self.cedula = cedula
        self.numeroTelefonico = numeroTelefonico

    # METODOS
    def CrearUsuario(self):
        print("creado exitosaente")

    def ActualizarUsuario(self):
        print("actualizado correctamente")