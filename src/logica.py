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
    angulo_radianes = math.radians(angulo) # Paso a radianes
    resultado = math.tan(angulo_radianes) * longitud # Calculo el resultado

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
    Si el archivo no existe, devuelve un DataFrame vacío y capturamos el error.
    """
    try:
        return pd.read_csv(ARCHIVO_CSV)
    # Capturo el error de no encontrar el archivo
    except FileNotFoundError:
        return pd.DataFrame(columns=['nombre', 'angulo', 'longitud', 'resultado'])


def ver_proyecto(indice):
    """
    Devuelve los datos del proyecto ubicado en la fila 'indice'.
    Si el índice no existe, retorna None.
    """
    # Cargamos los datos
    df = cargar_proyectos()
    
    if 0 <= indice < len(df):
        # Seleccionamos todas las columnas de la fila indice
        fila = df.iloc[indice] # https://www.analyticslane.com/2019/06/21/seleccionar-filas-y-columnas-en-pandas-con-iloc-y-loc/
        # Convertimos en diccionario
        return fila.to_dict() #https://www-geeksforgeeks-org.translate.goog/pandas-dataframe-to_dict/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
    else:
        None
        
    
    
    
    