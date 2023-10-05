# python listado_cheques.py 42874892 salida tipo_cheque estado_cheque rango_fechas

import sys
import pandas as pd
import numpy as np
from datetime import datetime

#Parseo del comando en argumentos

if len(sys.argv) > 1:
    # Argumento 1
    dni = sys.argv[1]
    print(f"El primer argumento es: {dni}")

if len(sys.argv) > 2:
    # Argumento 2
    salida = sys.argv[2]
    tipo_cheque = sys.argv[3]
    estado_cheque = sys.argv[4]
    salida = sys.argv[5]
    print(f"El segundo argumento es: {salida}")
    print(f"El segundo argumento es: {tipo_cheque}")
    print(f"El segundo argumento es: {estado_cheque}")
    print(f"El segundo argumento es: {salida}")


def containsArgs(list, *args): #Estado: Puede tener 3 valores pendiente, aprobado o rechazado.
    '''Comprueba que la lista dada solo contenga los args dados'''
    tam = i = len(args) - 1

    for item in list:
        i = tam

        while( 0 <= i and item != args[i]):
            i -= 1
        
        if( i < 0 ):
            return False
    
    return True

table = pd.read_csv('data/ejemplo.csv', sep=',', decimal= ".")
data = table.to_numpy()
print(table)
print(type(table))
print(type(data))

#Validacion de datos de entrada:

def func(): #Nombre del Archivo: El script de Python se debe llamar listado_cheques.py.
    '''esta funcion debe devolver true si el parametro ingresado es "listado_cheques.py" 
y false si no lo es, junto con la muestra por consola del error correspondiente'''
    '''descripcion'''

def func(): #Nombre del archivo CSV: Se debe proporcionar el nombre del archivo CSV
            #que contiene los registros de los cheques.
    '''esta funcion debe devolver true si se encuentra el archivo CSV dado por parametro
y false si no se encuentra, junto con la muestra por consola del error correspondiente'''
    '''descripcion'''

def func(): #DNI del Cliente: Se debe proporcionar el DNI del cliente para el cual se
            #realizará la consulta.
    '''esta funcion debe devolver true si el parametro de la funcion es un numero entero mayor 
a cero y false si no lo es, junto con la muestra por consola del error correspondiente'''
    '''descripcion'''

def func(): #Salida (PANTALLA o CSV): El usuario puede elegir si desea ver los resultados
            #en la pantalla o exportarlos a un archivo CSV.
    '''esta funcion debe devolver true si el parametro ingresado es "PANTALLA" o "CSV"
y false si no lo es, junto con la muestra por consola del error correspondiente'''
    '''descripcion'''

def func(): #Tipo de Cheque (EMITIDO o DEPOSITADO): El usuario debe especificar si
            #desea consultar cheques emitidos o depositados.
    '''esta funcion debe devolver true si el parametro ingresado es "EMITIDO" o "DEPOSITADO"
y false si no lo es, junto con la muestra por consola del error correspondiente'''
    '''descripcion'''

def func(): #Estado del Cheque (Opcional): El usuario puede proporcionar un estado de
            #cheque (PENDIENTE, APROBADO, RECHAZADO) como criterio de filtrado.
    '''esta funcion debe devolver true si el parametro ingresado es "PENDIENTE" o "APROBADO"
O "DEPOSITADO" y false si no lo es, junto con la muestra por consola del error correspondiente'''
    '''descripcion'''

def func(): #Rango de Fechas (Opcional): El usuario puede especificar un rango de
            #fechas para filtrar los cheques.  --fecha 2021-09-12:2
    '''PREGUNTAR AL PROFE COMO ES EL TEMA DEL RANGO'''
    '''descripcion'''

def func(): #Validar que la entrada es correcta con las funciones de arriba.
    '''esta funcion debe devolver true si la entrada dada por el usuario es correcta segun
las funciones de arriba y false si no lo es, junto con la muestra por consola del error
correspondiente'''
    '''descripcion'''

#FILTRO 1

#MANEJO DE ERRORES (NRO CHEQUES REPETIDOS)
def  haveRepeat(list): #NroCheque: Número de cheque, este debe ser único por cuenta.
    '''Si la lista dada tiene repetidos devuelve True, si no False.'''
    for j in range(len(list)):
        for i in range(j + 1, len(list)):
            if( list[j] == list[i] ):
                return True

    return False

#FILTRO 2

#FILTRO 3

def func(): #Filtrado por Estado (Opcional): Si el estado del cheque no se proporciona
            #como parámetro, se deben imprimir los cheques sin filtrar por estado.
    '''descripcion'''

#FILTRO 4

#SALIDA DE DATOS

def saveCsv(tabla): #Validar CSV con las funciones de arriba
    '''descripcion'''
            #CSV debe contener las siguientes columnas: NroCheque, CodigoBanco,
            #CodigoSucursal, NumeroCuentaOrigen, NumeroCuentaDestino, Valor,
            #FechaOrigen, FechaPago, DNI, Estado.
    '''Guarda el csv dado en un archivo salida.csv'''
    sep= ","
    strignTable = sep.join(map(str,table.columns.tolist()))

    for i in range(len(table)):
        strignTable = strignTable + '\n' + sep.join(map(str,table.iloc[i].tolist()))

    with open('data/salida.cvs', 'w') as file:
        file.write(strignTable)
        file.close()

def inRange(list, min=None, max=None): #CodigoBanco: Código numérico del banco, entre 1 y 100.
                                       #CodigoScurusal: Código numérico de la sucursal del banco va entre 1 y 300.
                                       #DNI: String con DNI del cliente donde se permite identificarlo
    '''Retorna true si todos los numeros de la lista dada estan en el rango entre [min, max], si no
    devuelve False junto con el indice del primer numero fuera de rango'''

    # if( not( isinstance(min, (int, float)) and isinstance(max, (int, float)) ) ):
    #     raise ValueError("El rango dado debe estar compuesto por numeros.")
    
    # if( min == max == None ):
    #     raise ValueError("El rango no esta dado.")          
    # elif( not( min==None or max==None ) ):
    #     if(min >= max ):
    #         raise ValueError(f"El rango ({min},{max}) no es valido.")

    for i in range(len(list)):
        if( not( isinstance(list[i], (int, float)) ) ):
            raise ValueError("La lista dada debe estar compuesto por numeros.")
        if (min is not None and list[i] < min) or (max is not None and list[i] > max):
            return False, i
    
    return True

def func(): #FechaOrigen: Fecha de emisión: (En timestamp)
    '''descripcion'''
    fecha = datetime.utcfromtimestamp(1631066400)
    print(fecha)


def func(): #Si el parámetro "Salida" es PANTALLA, imprimir por pantalla todos los
            #valores correspondientes a la consulta.
    '''descripcion'''

def save_in_csv(table:pd): #Si el parámetro "Salida" es CSV, exportar los resultados a un archivo CSV
    #con el nombre en el f
    '''descripcion'''