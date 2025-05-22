import csv
import random
import math
import os
import pandas as pd

# Ruta del archivo CSV que almacenará los proyectos
ARCHIVO_CSV = 'data/proyectos.csv'

def registrar_proyecto(nombre, longitud):
    """
    Registra un nuevo proyecto de construcción en el archivo CSV.
    - Genera un ángulo aleatorio entre 30° y 60°.
    - Calcula el resultado: tan(ángulo en radianes) * longitud.
    - Guarda los datos en el archivo.
    """
    angulo = random.uniform(30, 60)  # Ángulo en grados
    angulo_radianes = math.radians(angulo)
    resultado = math.tan(angulo_radianes) * longitud

    fila = {
        'nombre': nombre,
        'angulo': round(angulo, 2),
        'longitud': longitud,
        'resultado': round(resultado, 2)
    }

    archivo_existe = os.path.isfile(ARCHIVO_CSV)

    with open(ARCHIVO_CSV, mode='a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fila.keys())
        if not archivo_existe:
            writer.writeheader()
        writer.writerow(fila)



def cargar_proyectos():
    """
    Carga y devuelve todos los proyectos almacenados en el CSV.
    Si el archivo no existe, devuelve un DataFrame vacío.
    """
    if os.path.isfile(ARCHIVO_CSV):
        return pd.read_csv(ARCHIVO_CSV)
    else:
        return pd.DataFrame(columns=['nombre', 'angulo', 'longitud', 'resultado'])
