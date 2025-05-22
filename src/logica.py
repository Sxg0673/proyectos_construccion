import csv
import random
import math
import os
import pandas as pd

# Ruta del archivo CSV que almacenará los proyectos
ARCHIVO_CSV = 'data/proyectos.csv'

def registrar_proyecto(nombre, longitud): # Necesito pedir el nombre y la longitud del proyecto
    """
    Registra un nuevo proyecto de construcción en el archivo CSV.
    - Genera un ángulo aleatorio entre 30° y 60°.
    - Calcula el resultado: tan(ángulo en radianes) * longitud.
    - Guarda los datos en el archivo.
    """
    angulo = random.uniform(30, 60)  # Ángulo en grados
    angulo_radianes = math.radians(angulo) # Paso a radianes
    resultado = math.tan(angulo_radianes) * longitud # Calculo el resultado

    # Este diccionario se convertira en una fila de la base de datos
    fila = { 
        'nombre': nombre, # El nombre que pedimos a traves de la GUI
        'angulo': round(angulo, 2),
        'longitud': longitud, # La longitud que pedimos a traves de la GUI
        'resultado': round(resultado, 2)
    }

    # Comprobamos si el archivo existe
    archivo_existe = os.path.isfile(ARCHIVO_CSV)
    
    # Abrimos el archivo en modo 'a' (append) para agregar contenido al final sin borrar lo anterior
    # newline='' evita que se agreguen lineas en blanco entre registros en algunos sistemas
    with open(ARCHIVO_CSV, mode='a', newline='') as f:
        
        # Creamos un escritor CSV que usará las claves del diccionario 'fila' como nombres de las columnas
        writer = csv.DictWriter(f, fieldnames=fila.keys()) # fila.keys saca dict_keys(['nombre', 'angulo', 'longitud', 'resultado'])
        
        # Si el archivo aún no existia, escribimos los encabezados (nombres de columnas) antes de la primera fila
        if not archivo_existe:
            writer.writeheader() #dict_keys(['nombre', 'angulo', 'longitud', 'resultado'])

        # Escribimos la fila con los datos del proyecto como una nueva línea en el archivo CSV.
        writer.writerow(fila)



def cargar_proyectos():
    """
    Carga y devuelve todos los proyectos almacenados en el CSV.
    Si el archivo no existe, devuelve un DataFrame vacío y capturamos el error.
    """
    try:
        return pd.read_csv(ARCHIVO_CSV) # Intento cargar los datos
    except FileNotFoundError: # Capturo el error de no encontrar el archivo
        return pd.DataFrame(columns=['nombre', 'angulo', 'longitud', 'resultado']) # Si no se puede devuelvo un DataFrame vacio


def ver_proyecto(indice): # Se requiere el indice
    """
    Devuelve los datos del proyecto ubicado en la fila 'indice'.
    Si el índice no existe, retorna None.
    """
    # Cargamos los datos
    df = cargar_proyectos()
    
    if 0 <= indice < len(df): # Compruebo que el indice se encuentre en el rango de indices existentes
        # Seleccionamos todas las columnas de la fila indice
        fila = df.iloc[indice] # https://www.analyticslane.com/2019/06/21/seleccionar-filas-y-columnas-en-pandas-con-iloc-y-loc/
        # Convertimos en diccionario
        return fila.to_dict() #https://www-geeksforgeeks-org.translate.goog/pandas-dataframe-to_dict/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
    else:
        None
        

def eliminar_proyecto(indice): # Se requiere el indice
    """
    Elimina el proyecto ubicado en la posición 'indice'.
    Retorna True si fue eliminado, False si el índice no existe.
    """
    # Cargamos los datos
    df = cargar_proyectos()
    
    if 0 <= indice < len(df): # Comprobamos que el indicie se encuentre en el rango de indice existentes
        # Elimino la fila por el indice y reacomodo indices
        df = df.drop(index=indice).reset_index(drop=True) # https://www.datacamp.com/es/tutorial/pandas-reset-index-tutorial
        # Sobrescribo el csv para guardarlo
        df.to_csv(ARCHIVO_CSV, index=False) # https://www.freecodecamp.org/espanol/news/dataframe-a-csv-como-guardar-pandas-dataframes-exportando/
        return True
    else:
        return False