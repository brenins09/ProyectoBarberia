class Barbero(Usuario):
    NumeroDeCorte:int
    PrecioCorte:int

    #CONSTRUCTOR
    def __init__(self, CapacitacionTrabajador):
        self.CapacitacionTrabajador = CapacitacionTrabajador

        #METODOS
        def CalcularPromedioDiario(self, NumeroDeCorte, PrecioCorte):