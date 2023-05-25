import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry


class PantallaEncuesta:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Pantalla de Encuesta")

        self.gestor = None
        self.fecha_inicio = None
        self.fecha_fin = None
        self.llamadas_filtradas = None
        self.llamada_seleccionada = None

        self.construirInterfaz()

    def construirInterfaz(self):
        boton_consultar = tk.Button(self.ventana, text="Consultar encuestas", command=self.mostrarVentanaFechas)
        boton_consultar.pack()

        self.ventana.mainloop()

    def mostrarVentanaFechas(self):
        self.ventana.withdraw()  # Ocultar la ventana principal

        ventana_fechas = tk.Toplevel(self.ventana)
        ventana_fechas.title("Fechas del Periodo")

        label_inicio = tk.Label(ventana_fechas, text="Fecha de inicio:")
        label_inicio.pack()
        entrada_inicio = DateEntry(ventana_fechas, width=12, background='darkblue', foreground='white',
                                   borderwidth=2, year=2023)
        entrada_inicio.pack(pady=5)

        label_fin = tk.Label(ventana_fechas, text="Fecha de fin:")
        label_fin.pack()
        entrada_fin = DateEntry(ventana_fechas, width=12, background='darkblue', foreground='white',
                                borderwidth=2, year=2023)
        entrada_fin.pack(pady=5)

        boton_filtrar = tk.Button(ventana_fechas, text="Filtrar",
                                  command=lambda: self.filtrarLlamadas(entrada_inicio.get_date(), entrada_fin.get_date()))
        boton_filtrar.pack(pady=10)

    def filtrarLlamadas(self, fecha_inicio, fecha_fin):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

        self.llamadas_filtradas = self.gestor.filtrarLlamadas(fecha_inicio, fecha_fin)

        if not self.llamadas_filtradas:
            messagebox.showinfo("Sin resultados", "No se encontraron llamadas en el periodo seleccionado.")
            return

        self.mostrarVentanaLlamadas()

    def mostrarVentanaLlamadas(self):
        ventana_llamadas = tk.Toplevel(self.ventana)
        ventana_llamadas.title("Llamadas Filtradas")

        tabla_llamadas = tk.Listbox(ventana_llamadas, selectmode=tk.SINGLE)
        for llamada in self.llamadas_filtradas:
            tabla_llamadas.insert(tk.END, llamada)
        tabla_llamadas.pack(pady=10)

        boton_seleccionar = tk.Button(ventana_llamadas, text="Seleccionar llamada", command=self.seleccionarLlamada)
        boton_seleccionar.pack(pady=5)

    def seleccionarLlamada(self):
        seleccion = self.tabla_llamadas.curselection()
        if seleccion:
            index = seleccion[0]
            self.llamada_seleccionada = self.llamadas_filtradas[index]
            self.mostrarDatosLlamada()
        else:
            messagebox.showwarning("Llamada no seleccionada", "Por favor, seleccione una llamada de la tabla.")

    def mostrarDatosLlamada(self):
        ventana_datos_llamada = tk.Toplevel(self.ventana)
        ventana_datos_llamada.title("Datos de Llamada")

        # Mostrar los datos de la llamada seleccionada en la ventana

    def ejecutar(self, gestor_encuestas):
        self.gestor = gestor_encuestas


# Ejemplo de uso
class GestorEncuestas:
    def filtrarLlamadas(self, fecha_inicio, fecha_fin):
        # Realizar las consultas necesarias y devolver las llamadas filtradas
        llamadas_filtradas = [...]  # Lista de llamadas filtradas
        return llamadas_filtradas


gestor_encuestas = GestorEncuestas()
pantalla_encuesta = PantallaEncuesta()
pantalla_encuesta.ejecutar(gestor_encuestas)
