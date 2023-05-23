
class CambioDeEstado:
    def __init__(self, fechaHoraInicio, estado):
        self.fechaHoraInicio = fechaHoraInicio
        self.estado = estado

    def getFechaHoraInicio(self):
        return self.fechaHoraInicio

    def setFechaHoraInicio(self, valor):
        self.fechaHoraInicio = valor

    def getEstado(self):
        return self.estado

    def setEstado(self, valor):
        self.estado = valor

    def esEstadoInicial(self):
        return self.estado.esIniciada()

    def getNombreEstado(self):
        return self.estado.getNombre()
