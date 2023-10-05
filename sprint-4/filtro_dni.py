#python filtro_dni.py Ejemplo.csv 55555555
import sys
import pandas as pd
import numpy as np
#FILTRO 1
def filtrar_datos_por_dni(nombre_archivo, dni):
    # Leer el archivo CSV
    df = pd.read_csv(nombre_archivo)

    # Convertir el DNI a un número
    dni = int(dni)

    # Filtrar los datos por DNI
    df_filtrado = df[df['DNI'] == dni]

    # Verificar si hay números de cheque duplicados para el mismo DNI y cuenta
    duplicados = df_filtrado[df_filtrado.duplicated(['NroCheque', 'NumeroCuentaOrigen'])]

    if not duplicados.empty:
        print("Error: Se encontraron números de cheque duplicados para el mismo DNI y cuenta.")
        print(duplicados)

    return df_filtrado

if __name__ == "__main__":
    if len(sys.argv) > 2:
        # Argumento 1: nombre del archivo
        nombre_archivo = 'data/'+sys.argv[1]

        # Argumento 2: DNI
        dni = sys.argv[2]

        # Filtrar los datos por DNI
        df_filtrado = filtrar_datos_por_dni(nombre_archivo, dni)

        # Imprimir los datos filtrados
        print(df_filtrado)
