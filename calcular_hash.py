import os
import hashlib

def calcular_md5(archivo):
    """Calcula el hash MD5 de un archivo."""
    hash_md5 = hashlib.md5()
    with open(archivo, "rb") as f:
        for bloque in iter(lambda: f.read(4096), b""):
            hash_md5.update(bloque)
    return hash_md5.hexdigest()

def procesar_archivos(directorio):
    """Calcula y muestra el hash MD5 de cada archivo en el directorio dado."""
    for nombre_archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, nombre_archivo)
        if os.path.isfile(ruta_archivo):
            hash_md5 = calcular_md5(ruta_archivo)
            print(f'{nombre_archivo}: {hash_md5}')

# Cambia esta variable por la ruta de tu directorio
directorio = 'irudia_folder'

procesar_archivos(directorio)
