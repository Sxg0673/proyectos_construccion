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
        # Boton para registrar nuevo proyecto
        boton_registrar = tk.Button(self, text="Registrar Proyecto", command=self.abrir_formulario_registro) # Al hacer click se dirige a abrir_formulario_registro
        boton_registrar.grid(row=0, column=0, padx=10, pady=10, sticky="ew") # http://acodigo.blogspot.com/2017/03/tkinter-grid.html#google_vignette
        
    
    def abrir_formulario_registro(self):
        ventana = tk.Toplevel(self) # Crea ventana secundaria
        ventana.title("Nuevo Proyecto")
        ventana.geometry("300x200")

        # Etiqueta y campo para el nombre
        tk.Label(ventana, text="Nombre del proyecto").grid(row=0, column=0, padx=5, pady=5, sticky="e") # Creamos y posicionamos el label
        entrada_nombre = tk.Entry(ventana) # Creamos la entrada en la ventana secundaria
        entrada_nombre.grid(row=0, column=1, padx=5, pady=5) # La posicionamos
        

        # Etiqueta y campo para la longitud
        tk.Label(ventana, text="Longitud").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entrada_longitud = tk.Entry(ventana)
        entrada_longitud.grid(row=1, column=1, padx=5, pady=5)

        # Botón para registrar
        def confirmar():
            nombre = entrada_nombre.get() # Obtener nombre
            try:
                longitud = float(entrada_longitud.get()) # Obtener longitud como float
                registrar_proyecto(nombre, longitud) # Mandamos todo a registrar_proyecto
                messagebox.showinfo("Éxito", "Proyecto registrado correctamente") # Todo funciono correctamente
                ventana.destroy() # Destruimos ventana secundaria
            except ValueError: # Ocurrio un error de valores
                messagebox.showerror("Error", "La longitud debe ser un número válido")

        boton_guardar = tk.Button(ventana, text="Guardar", command=confirmar) # Boton de confirmar creado
        boton_guardar.grid(row=2, column=0, columnspan=2, pady=10) # Posicionamos el boton en la ventana secundaria



if __name__ == "__main__": # https://www.youtube.com/watch?v=wZKTUcTqekw
    app = App() # Inicializamos la clase App
    app.mainloop()