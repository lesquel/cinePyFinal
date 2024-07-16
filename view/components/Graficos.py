import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading

def crear_grafico_barras(frame, data, labels, title="Gráfico de Barras", x_label="X", y_label="Y", row=0, column=0):
    # Crear la figura de matplotlib
    fig, ax = plt.subplots()

    # Crear el gráfico de barras
    ax.bar(labels, data)

    # Añadir etiquetas y título
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    # Crear el canvas de Tkinter y añadir la figura
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    widget = canvas.get_tk_widget()
    widget.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

# Función para obtener datos y crear el gráfico en el hilo principal
def obtener_datos_y_crear_grafico(frame, data, labels, row, column, title, x_label, y_label):
    def actualizar_grafico():
        crear_grafico_barras(frame, data, labels, title, x_label, y_label, row, column)
    
    frame.after(0, actualizar_grafico)

# Función para ejecutar en un hilo
def Graficos(frame, data, labels, row, column, title="Gráfico de Barras", x_label="X", y_label="Y"):
    thread = threading.Thread(target=obtener_datos_y_crear_grafico, args=(frame, data, labels, row, column, title, x_label, y_label))
    thread.start()
