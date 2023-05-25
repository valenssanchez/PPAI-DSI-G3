#test
from datetime import datetime

from Modelo.Cliente import Cliente
from Modelo.Llamada import Llamada
from Modelo.Pregunta import Pregunta
from Modelo.Encuesta import Encuesta
from Modelo.RespuestaPosible import RespuestaPosible
from Modelo.RespuestaDeCliente import RespuestaDeCliente
from Modelo.Estado import Estado
from Modelo.CambioDeEstado import CambioDeEstado
from Controlador.GestorEncuesta import GestorEncuesta


estado_iniciado = Estado("Iniciada")
estado_finalizado = Estado("Finalizada")

cambioEstado1 = CambioDeEstado(estado_iniciado)

cliente1 = Cliente("12345678", "Juan Perez", "123456789")
cliente2 = Cliente("87654321", "María González", "987654321")
cliente3 = Cliente("45678912", "Pedro Sanchez", "654321987")

llamada1 = Llamada(cambioEstado1, cliente1)
llamada2 = Llamada(cambioEstado1, cliente2)
llamada3 = Llamada(cambioEstado1, cliente3)

# Crear instancias de la clase RespuestaDeCliente
respuesta1 = RespuestaPosible("Azul", 1)
respuesta2 = RespuestaPosible("Rojo", 2)
respuesta3 = RespuestaPosible("Masculino", 1)
respuesta4 = RespuestaPosible("Femenino", 2)
respuesta5 = RespuestaPosible("Prefiero no decirlo", 3)

# Crear una instancia de la clase Pregunta
pregunta1 = Pregunta("¿Cuál es tu color favorito?", [respuesta1, respuesta2])
pregunta2 = Pregunta("¿Cuál es tu género?", [respuesta3, respuesta4, respuesta5])

# Asignar pregunta a respuesta
respuesta1.setPreguntaAsociada(pregunta1)
respuesta2.setPreguntaAsociada(pregunta1)
respuesta3.setPreguntaAsociada(pregunta2)
respuesta4.setPreguntaAsociada(pregunta2)
respuesta5.setPreguntaAsociada(pregunta2)

# Crear una instancia de la clase Encuesta
encuesta1 = Encuesta("Encuesta de colores", datetime(2023, 12, 31), [pregunta1])
encuesta2 = Encuesta("Encuesta de colores", datetime(2023, 12, 31), [pregunta2])


respuestaCliente1 = RespuestaDeCliente(respuesta1)
respuestaCliente2 = RespuestaDeCliente(respuesta4)

llamada1.setRespuestaDeCliente(respuestaCliente1)
#llamada2.setRespuestaDeCliente(respuestaCliente2)

gestor = GestorEncuesta()

llamadaArray = [llamada1, llamada2, llamada3]

gestor.setFechaInicio(datetime(2023, 5, 22))
gestor.setFechaFin(datetime(2023, 5, 24))

llamadasFiltradas = gestor.filtrarLlamadas(llamadaArray)

arrayEncuestas = [encuesta1, encuesta2]

nombreCliente, estadoActual, duracion, respuestas, preguntas, descripcionEncuesta = gestor.buscarDatosDeLlamadaSeleccionada(llamada1, arrayEncuestas)

print(nombreCliente, estadoActual, duracion, respuestas, preguntas, descripcionEncuesta)


