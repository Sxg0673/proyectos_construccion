import tkinter as tk
from tkinter import messagebox

# Importamos todas las funciones necesarias desde logica.py
from logica import (
    registrar_proyecto,
    cargar_proyectos,
    ver_proyecto,
    eliminar_proyecto
)

class App(tk.Tk): # Hereda la clase tk.Tk
    def __init__(self):
        super().__init__()

        self.title("Registro de Proyectos de Construcción")
        self.geometry("500x300")
        self.resizable(True, True)

        self.configurar_grid()
        self.crear_widgets()