# Proyecto de Registro de Construcciones

Este programa permite registrar proyectos de construcción usando una interfaz gráfica desarrollada con `tkinter`.

---

## Funcionalidades principales

- Registrar nombre del proyecto.
- Generar un ángulo aleatorio entre 30° y 60°.
- Solicitar una longitud (adyacente).
- Calcular la altura usando la fórmula:  
  **altura = tan(ángulo en radianes) × longitud**.
- Guardar automáticamente los proyectos en un archivo `.csv`.

---

## El programa también permite:

- Cargar proyectos automáticamente desde el archivo si ya existe.
- Ver los datos de un proyecto mediante su número (índice).
- Eliminar un proyecto según su número.
- Agregar nuevos proyectos al final del archivo.

---

## Estructura del proyecto

proyectos_construccion/
├── data/ # Contiene el archivo registros.csv
├── src/ # Código fuente principal del programa
├── .gitignore # Archivos a ignorar por Git
├── README.md # Este archivo
└── requirements.txt # Librerías necesarias para ejecutar


---

## Cómo ejecutar el programa

1. Clona este repositorio:

git clone https://github.com/Sxg0673/proyectos_construccion.git
Instala las dependencias (si tienes un entorno virtual activado):
pip install -r requirements.txt
Ejecuta la aplicación desde la carpeta src:
python app.py


## Librerías utilizadas:

- tkinter
- math
- random
- csv
- pandas


## Autor: Santiago Castillo
## Trabajo final