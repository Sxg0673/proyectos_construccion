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
    def __init__(self): # Constructor
        super().__init__() # Heredamos el tk.Tk

        self.title("Registro de Proyectos de Construcción")
        self.geometry("500x300")
        self.resizable(True, True)

        self.configurar_grid()
        self.crear_widgets()
        
    def configurar_grid(self):
        pass  # Aquí se va a definir el grid en la próximamente

    def crear_widgets(self):
        pass  # Aquí se pone todos los botones, etc.

if __name__ == "__main__": # https://www.youtube.com/watch?v=wZKTUcTqekw
    app = App() # Inicializamos la clase App
    app.mainloop()