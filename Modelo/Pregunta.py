class Pregunta:
    def __init__(self, pregunta, respuesta):
        self.pregunta = pregunta
        self.respuesta = []

    def getPregunta(self):
        return self.pregunta

    def setPregunta(self, valor):
        self.pregunta = valor

    def getRespuesta(self):
        return self.respuesta

    def setRespuesta(self, valor):
        self.respuesta.append(valor)

