# python listado_cheques.py cheques.py 42874892 salida tipo_cheque estado_cheque rango_fechas

import sys
import pandas as pd
import numpy as np
from datetime import datetime

def muestraMensajeError():
    print("ERROR: Los parametros ingresados son incorrectos. Intentelo nuevamente.")   
    print("El formato esperado es el siguiente:")   
    print("\n> python listado_cheques.py cheques.csv (DNI) (salida) (tipo-cheque) [estado-cheque] [rango_fechas]\n")   
    print("Los parentesis () indican que el parametro es obligatorio y los corchetes [] que es opcional.")   

#Validacion de datos de entrada:
def validaDNI(dni): 
    '''
    Esta funcion verifica si el formato de un DNI es valido.
    El DNI debe tener digitos numericos, ser mayor que 0 y no tener una longitud mayor a 8 caracteres.

    :param dni: DNI ingresado por el usuario.
    :type dni: string
    :return: Si el DNI es correcto.
    :rtype: bool
    '''
    es_digito = dni.isdigit()
    mayor_a_cero = int(dni) > 0
    longitud_menor_a_ocho = len(dni) <= 8

    return es_digito and mayor_a_cero and longitud_menor_a_ocho

def validaSalida(salida):
    '''
    Esta funcion verifica si el formato del parametro SALIDA es valido.
    El parametro ingresado debe ser igual a "PANTALLA" o "CSV".

    :param dni: tipo de salida deseada por el usuario.
    :type dni: string
    :return: Si el parametro ingresado es correcto.
    :rtype: bool
    '''

    return salida.upper() == "PANTALLA" or salida.upper() == "CSV"

def validaTipoCheque(tipo_cheque): 
    '''
    Esta funcion verifica si el formato del parametro TIPO CHEQUE es valido.
    El parametro ingresado debe ser igual a "EMITIDO" o "DEPOSITADO".

    :param dni: tipo de cheque deseado por el usuario.
    :type dni: string
    :return: Si el parametro ingresado es correcto.
    :rtype: bool
    '''

    return tipo_cheque.upper() == "EMITIDO" or tipo_cheque.upper() == "DEPOSITADO"

def validaEstadoCheque(estado_cheque):
    '''
    Esta funcion verifica si el formato del parametro ESTADO CHEQUE es valido.
    El parametro ingresado debe ser igual a "PENDIENTE" o "APROBADO" o "RECHAZADO".

    :param dni: estado de cheque deseado por el usuario.
    :type dni: string
    :return: Si el parametro ingresado es correcto.
    :rtype: bool
    '''

    return estado_cheque.upper() == "PENDIENTE" or estado_cheque.upper() == "APROBADO" or estado_cheque.upper() == "RECHAZADO"

def validaRangoFechas(): #Rango de Fechas (Opcional): El usuario puede especificar un rango de
            #fechas para filtrar los cheques.  --fecha 2021-09-12:2
    '''PREGUNTAR AL PROFE COMO ES EL TEMA DEL RANGO'''
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

#CODIGO PRINCIPAL

def main():
    if len(sys.argv) < 5:
        muestraMensajeError()
    else:
        nombre_archivo = sys.argv[1]
        print(nombre_archivo)

        #VERIFICAR QUE EL ARCHIVO EXISTA Y ABRIRLO --> sino devolver error

        data = pd.read_csv('data/ejemplo.csv', sep=',', decimal= ".")
        head = data.columns.tolist()
        tabla = data.to_numpy()

        dni = sys.argv[2]
        salida = sys.argv[3]
        tipo_cheque = sys.argv[4]

        if validaDNI(dni) and validaSalida(salida) and validaTipoCheque(tipo_cheque):
            print("APLICO 1ER FILTRO")
            print("APLICO MANEJO DE ERRORES")
            print("APLICO 2DO FILTRO")

            if len(sys.argv) == 6:
                if validaEstadoCheque(sys.argv[5]): #El ultimo parametro ingresado es el ESTADO DEL CHEQUE
                    print("APLICO 3ER FILTRO")
                elif validaRangoFechas(sys.argv[5]): #El ultimo parametro ingresado es el RANGO DE FECHAS
                    print("APLICO 4TO FILTRO")
                else:
                    muestraMensajeError()
                
            elif len(sys.argv) == 7:
                estado_cheque = sys.argv[5]
                rango_fechas = sys.argv[6]

                if validaEstadoCheque(estado_cheque) and validaRangoFechas(rango_fechas):
                    print("APLICO 3ER FILTRO")
                    print("APLICO 4TO FILTRO")
                else:
                    muestraMensajeError()
        else:
            muestraMensajeError()

        leakedData = filterTime(data, rango_fechas)

        if ( salida == 'PANTALLA' ):
            printNumpy(leakedData, head)
        else:
            saveCsv(leakedData, head)  

main() 