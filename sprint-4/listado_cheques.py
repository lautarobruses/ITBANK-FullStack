# python listado_cheques.py 42874892 salida tipo_cheque estado_cheque rango_fechas

import sys
import pandas as pd
import numpy as np
from datetime import datetime

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

def filterTime(): #Filtrado por Estado (Opcional): Si el estado del cheque no se proporciona
            #como parámetro, se deben imprimir los cheques sin filtrar por estado.
    '''descripcion'''

#SALIDA DE DATOS
def timeToStr(number:int): #FechaOrigen: Fecha de emisión: (En timestamp)
    '''Retorna un string de la fecha dada por el timestamp dado.'''
    return datetime.utcfromtimestamp(number).strftime('%Y/%m/%d %H:%M:%S')

def printNumpy(table:np, head:list|None):
    '''Muestra por pantalla el numpy dado.'''
    sep = "|"
    table[:, 6] = [timeToStr(x) for x in table[:, 6]]
    table[:, 7] = [timeToStr(x) for x in table[:, 7]]

    if ( head != None ):
        print( sep.join([ x.center(11) for x in map( str, head ) ]) )

    for list in table:
        print( sep.join([ x.center(11) for x in map( str, list ) ]) )


def saveCsv(table:np, head:list|None):
    '''Guarda el numpy dado en un archivo salida.csv.'''
    sep= ","
    strignTable = sep.join(map( str, head ))

    for list in table:
        strignTable = strignTable + '\n' + sep.join(map( str, list ))

    with open('data/salida.csv', 'w') as file:
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
        if ( not( isinstance(list[i], (int, float)) ) ):
            raise ValueError("La lista dada debe estar compuesto por numeros.")
        if (min is not None and list[i] < min) or (max is not None and list[i] > max):
            return False, i
    
    return True


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

#Codigo principal

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
    rango_fechas = sys.argv[5]
    print(f"El segundo argumento es: {salida}")
    print(f"El segundo argumento es: {tipo_cheque}")
    print(f"El segundo argumento es: {estado_cheque}")
    print(f"El segundo argumento es: {salida}")


table = pd.read_csv('data/ejemplo.csv', sep=',', decimal= ".")

head = table.columns.tolist()

# Obtener los valores del DataFrame como un arreglo de NumPy

# Concatenar la cabecera como una fila al inicio del arreglo de datos
data = table.to_numpy()

leakedData= filterTime(data, rango_fechas)

if ( salida == 'PANTALLA' ):
    printNumpy(leakedData, head)
else:
    saveCsv(leakedData, head)