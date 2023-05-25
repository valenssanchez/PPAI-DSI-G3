
class Llamada:
    def __init__(self, cambioDeEstado, cliente):
        self.cliente = cliente
        self.descripcionOperador = ""
        self.detalleAccionRequerida = ""
        self.duracion = 0
        self.encuestaEnviada = None
        self.observacionAuditor = ""
        self.cambioDeEstado = [cambioDeEstado]
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
        fechaLlamada = self.obtenerFechaInicio()
        return fechaInicio <= fechaLlamada <= fechaFin

    def tieneRespuestas(self):
        return len(self.respuestaDeCliente) > 0

    def getNombreClienteDeLlamada(self):
        return self.cliente.getNombre()

    def obtenerEstadoActual(self):
        cambioEstadoActual = None
        ultimaFecha = None
        for cambioEstado in self.cambioDeEstado:
            fecha = cambioEstado.getFechaHoraInicio()
            if ultimaFecha is None:
                cambioEstadoActual = cambioEstado
                ultimaFecha = fecha
            else:
                if fecha > ultimaFecha:
                    cambioEstadoActual = cambioEstado
                    ultimaFecha = fecha
        return cambioEstadoActual.getNombreEstado()

    def obtenerDescripcionDeRespuestasYPreguntas(self):
        respuestas = []
        preguntas = []

        for respuesta in self.respuestaDeCliente:
            respuestas.append(respuesta.getDescripcionRta())
            preguntas.append(respuesta.getDescPreguntaAsociada())

        return respuestas, preguntas

    def obtenerFechaInicio(self):
        fechaInicio = None
        for cambioEstado in self.cambioDeEstado:
            fecha = cambioEstado.getFechaHoraInicio()
            if fechaInicio is None:
                fechaInicio = fecha
            else:
                if fecha < fechaInicio:
                    fechaInicio = fecha

        return fechaInicio


