
class RespuestasPosibles:
    def __init__(self, descripcion, valor):
        self.descripcion = descripcion
        self.valor = valor

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, valor):
        self.descripcion = valor

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor
