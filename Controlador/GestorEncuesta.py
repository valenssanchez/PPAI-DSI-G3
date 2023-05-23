
class GestorEncuesta():

    fechaInicio = ""
    fechaFin = ""
    llamadaSeleccionada = None
    csv = None

    def setFechaInicio(self, fecha):
        self.fechaInicio = fecha

    def getFechaInicio(self):
        return self.fechaInicio

    def setFechaFin(self, fecha):
        self.fechaFin = fecha

    def getFechaFin(self):
        return self.fechaFin

    def setLlamadaSeleccionada(self, llamada):
        self.llamadaSeleccionada = llamada

    def getLlamadaSeleccionada(self):
        return self.llamadaSeleccionada

    def setCSV(self, csv):
        self.csv = csv

    def getCSV(self):
        return self.csv

    def validarFechas(self, fechaInicio, fechaFin):
        return fechaInicio <= fechaFin

    def tomarFechaDelPeriodo(self, fechaInicio, fechaFin):
        if self.validarFechas(fechaInicio, fechaFin):
            self.setFechaInicio(fechaInicio)
            self.setFechaFin(fechaFin)

    def filtrarLlamadas(self, llamadas):
        llamadasFiltradas = []
        for llamada in llamadas:
            if (llamadas[llamada].esDePeriodo(self.fechaInicio, self.fechaFin)) and llamadas[llamada].tieneRespuestas():
                llamadasFiltradas.append(llamadas[llamada])

        if len(llamadasFiltradas) > 0:
            return llamadasFiltradas
        else:
            return False

    def tomarSeleccionDeLlamada(self, llamadaSelec):
        self.setLlamadaSeleccionada(llamadaSelec)


