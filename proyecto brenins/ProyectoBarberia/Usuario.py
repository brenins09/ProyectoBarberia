class Usuario:
    
    def __init__(self, nombre: str, fechaNacimiento: str, cedula: int, numeroTelefonico: int):
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento
        self.cedula = cedula
        self.numeroTelefonico = numeroTelefonico

    # METODOS
    def CrearUsuario(self):
        print("creado exitosaente")

    def ActualizarUsuario(self):
        print("actualizado correctamente")
objetoUsuario = Usuario("xiomara", "6 abril 2001", 107234, 32189234 )
#print(objetoUsuario.fechaNacimiento)