from CambioDeEstado import *


class Llamada:
    def __init__(self, cliente):
        self.cliente = cliente
        self.descripcionOperador = ""
        self.detalleAccionRequerida = ""
        self.duracion = 0
        self.encuestaEnviada = None
        self.observacionAuditor = ""
        self.cambioDeEstado = []
        self.respuestaDeCliente = []

    def getDescripcionOperador(self):
        return self.descripcionOperador

    def setDescripcionOperador(self, valor):
        self.descripcionOperador = valor

    def getDetalleAccionRequerida(self):
        return self.detalleAccionRequerida

    def setDetalleAccionRequerida(self, valor):
        self.detalleAccionRequerida = valor

    def getDuracion(self):
        return self.duracion

    def setDuracion(self, valor):
        self.duracion = valor

    def getEncuestaEnviada(self):
        return self.encuestaEnviada

    def setEncuestaEnviada(self, valor):
        self.encuestaEnviada = valor

    def getObservacionAuditor(self):
        return self.observacionAuditor

    def setObservacionAuditor(self, valor):
        self.observacionAuditor = valor

    def getCambioDeEstado(self):
        return self.cambioDeEstado

    def setCambioDeEstado(self, valor):
        self.cambioDeEstado.append(valor)

    def getRespuestaDeCliente(self):
        return self.respuestaDeCliente

    def setRespuestaDeCliente(self, valor):
        self.respuestaDeCliente.append(valor)

    def esDePeriodo(self, fechaInicio, fechaFin):
        cambioDeEstadoInicial = None
        for cambio in self.cambioDeEstado:
            if self.cambioDeEstado[cambio].esEstadoInicial():
                cambioDeEstadoInicial = self.cambioDeEstado[cambio]
                break
        fechaLlamada = cambioDeEstadoInicial.getFechaHoraInicio()
        return fechaInicio <= fechaLlamada <= fechaFin

    def tieneRespuestas(self):
        return len(self.respuestaDeCliente) > 0

    def getNombreClienteDeLlamada(self):
        return self.cliente.getNombre()

    def obtenerEstadoActual(self):
        cambioEstadoActual = None
        for cambio in self.cambioDeEstado:
            if self.cambioDeEstado[cambio].esUltimoEstado():
                cambioEstadoActual = self.cambioDeEstado[cambio]
                break
        return cambioEstadoActual.getNombreEstado()

    def obtenerDescripcionDeRespuestas(self):
        pass


