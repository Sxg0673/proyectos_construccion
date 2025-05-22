import tkinter as tk
from tkinter import messagebox

# Importamos todas las funciones necesarias desde logica.py
from logica import (
    registrar_proyecto,
    cargar_proyectos,
    ver_proyecto,
    eliminar_proyecto,
    actualizar_proyecto
)

class App(tk.Tk): # Hereda la clase tk.Tk
    def __init__(self): # Constructor
        super().__init__() # Heredamos el tk.Tk

        self.title("Registro de Proyectos de Construcción")
        self.geometry("500x300")
        self.resizable(True, True)
        
        self.configure(bg="#f5f5f5") # Color de fonod

        self.configurar_grid()
        self.crear_widgets()
        
        
    def configurar_grid(self):
        # Queremos 4 filas que se expandan proporcionalmente
        for i in range(4):
            self.grid_rowconfigure(i, weight=1)

        # Solo una columna que también se expanda
        self.grid_columnconfigure(0, weight=1)
        


    def crear_widgets(self):
        # Botón para registrar nuevo proyecto
        boton_registrar = tk.Button(self, text="Registrar Proyecto", command=self.abrir_formulario_registro)
        boton_registrar.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # http://acodigo.blogspot.com/2017/03/tkinter-grid.html#google_vignette

        # Botón para ver un proyecto
        btn_ver = tk.Button(self, text="Ver proyecto", command=self.abrir_formulario_ver)
        btn_ver.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Botón para eliminar un proyecto
        btn_eliminar = tk.Button(self, text="Eliminar proyecto", command=self.abrir_formulario_eliminar)
        btn_eliminar.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Botón para actualizar un proyecto
        btn_actualizar = tk.Button(self, text="Actualizar proyecto", command=self.abrir_formulario_actualizar)
        btn_actualizar.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")


    
    def abrir_formulario_registro(self):
        ventana = tk.Toplevel(self) # Crea ventana secundaria
        ventana.title("Nuevo Proyecto")
        ventana.geometry("350x200")

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

    def abrir_formulario_ver(self):
        ventana_ver = tk.Toplevel(self)
        ventana_ver.title("Ver Proyecto por Índice")

        # Entrada del indice
        tk.Label(ventana_ver, text="Índice del proyecto:").grid(row=0, column=0, padx=5, pady=5)
        entrada_indice = tk.Entry(ventana_ver)
        entrada_indice.grid(row=0, column=1, padx=5, pady=5)

        # Area de texto para mostrar el resultado
        texto = tk.Text(ventana_ver, width=50, height=10)
        texto.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        def mostrar():
            try:
                idx = int(entrada_indice.get()) # Recibimos el indice
                proyecto = ver_proyecto(idx) # Le enviamos el indice a ver_proyecto en logica.py
                if proyecto: # Si lo encuentra
                    texto.delete('1.0', tk.END) # Borramos lo que teniamos en texto si habia algo
                    #Para cada par clave-valor en el diccionario proyecto, guarda la clave en k y el valor en v, y repite
                    for k, v in proyecto.items(): # .items devuelve una lista de pares clave-valor
                        # tk.END va llevando todo al final a medida que se agrega algo
                        texto.insert(tk.END, f"{k}: {v}\n") # Inserta el par clave-valor
                else:
                    messagebox.showerror("Error", "Índice no válido.") # No encontro el indice
            except ValueError:
                messagebox.showerror("Error", "Ingrese un número válido.") # No puso un numero

        tk.Button(ventana_ver, text="Buscar", command=mostrar).grid(row=1, column=0, columnspan=2, pady=5) # Boton para buscar el indice y mostrar los datos

    def abrir_formulario_eliminar(self):
        ventana_eliminar = tk.Toplevel(self) # Ventana secundaria
        ventana_eliminar.title("Eliminar Proyecto")

        # Campo para ingresar el índice
        tk.Label(ventana_eliminar, text="Índice a eliminar:").grid(row=0, column=0, padx=5, pady=5)
        entrada_indice = tk.Entry(ventana_eliminar)
        entrada_indice.grid(row=0, column=1, padx=5, pady=5)

        def eliminar():
            try:
                idx = int(entrada_indice.get()) # Obtiene el indice
                proyecto = ver_proyecto(idx) 
                if proyecto:
                    confirmacion = messagebox.askyesno("Confirmar", f"¿Estás seguro de eliminar el proyecto '{proyecto['nombre']}'?")
                    if confirmacion:
                        eliminar_proyecto(idx)
                        messagebox.showinfo("Eliminado", "Proyecto eliminado correctamente.")
                        ventana_eliminar.destroy()
                else:
                    messagebox.showerror("Error", "Índice fuera de rango.")
            except ValueError:
                messagebox.showerror("Error", "Ingrese un número válido.")

        tk.Button(ventana_eliminar, text="Eliminar", command=eliminar).grid(row=1, column=0, columnspan=2, pady=10)

    def abrir_formulario_actualizar(self):
        ventana_actualizar = tk.Toplevel(self)
        ventana_actualizar.title("Actualizar Proyecto")

        # Entrada de índice
        tk.Label(ventana_actualizar, text="Índice del proyecto:").grid(row=0, column=0, padx=5, pady=5)
        entrada_indice = tk.Entry(ventana_actualizar)
        entrada_indice.grid(row=0, column=1, padx=5, pady=5)

        # Campos que se llenaran automáticamente si el indice es válido
        tk.Label(ventana_actualizar, text="Nuevo nombre:").grid(row=1, column=0, padx=5, pady=5)
        entrada_nombre = tk.Entry(ventana_actualizar)
        entrada_nombre.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(ventana_actualizar, text="Nueva longitud:").grid(row=2, column=0, padx=5, pady=5)
        entrada_longitud = tk.Entry(ventana_actualizar)
        entrada_longitud.grid(row=2, column=1, padx=5, pady=5)

        def cargar_datos():
            try:
                idx = int(entrada_indice.get()) # Toma el indice del que queremos ver los valores
                proyecto = ver_proyecto(idx) # Entregamos el indice a ver_proyecto
                if proyecto: # Si esta en proyecto entonces:
                    entrada_nombre.delete(0, tk.END) # Borramos lo que teniamos en la entrada de nombre
                    entrada_nombre.insert(0, proyecto["nombre"]) # Incertamos el nombre de ese indice
                    entrada_longitud.delete(0, tk.END) # Borramos el campo de longitud
                    entrada_longitud.insert(0, str(proyecto["longitud"])) # Insertamos la longitud del indice indicado
                else:
                    messagebox.showerror("Error", "Índice fuera de rango.") # Si pone un indice que no existe
            except ValueError:
                messagebox.showerror("Error", "Ingrese un número válido.") # Si pone algo que no sea numero

        def actualizar():
            try:
                idx = int(entrada_indice.get()) # Tomamos el indice
                nombre = entrada_nombre.get().strip() # https://www-geeksforgeeks-org.translate.goog/python-string-strip/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=rq
                longitud = float(entrada_longitud.get()) # Tomamos tanto el nombre como la longitud

                if nombre == "": # Hacemos manejo de errores
                    messagebox.showerror("Error", "El nombre no puede estar vacio.")
                    return

                if actualizar_proyecto(idx, nombre, longitud): # Usamos actualizar_proyecto de logica.py
                    messagebox.showinfo("Exito", "Proyecto actualizado correctamente.")
                    ventana_actualizar.destroy()
                else:
                    messagebox.showerror("Error", "Indice fuera de rango.") 
            except ValueError:
                messagebox.showerror("Error", "Ingrese valores validos.")

        tk.Button(ventana_actualizar, text="Cargar", command=cargar_datos).grid(row=3, column=0, pady=10)
        tk.Button(ventana_actualizar, text="Actualizar", command=actualizar).grid(row=3, column=1, pady=10)


if __name__ == "__main__": # https://www.youtube.com/watch?v=wZKTUcTqekw
    app = App() # Inicializamos la clase App
    app.mainloop()
    