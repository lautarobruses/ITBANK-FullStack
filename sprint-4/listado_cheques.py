''' CONSIGNA: 
El objetivo de este proyecto es desarrollar un script de Python llamado
listado_cheques.py que permita procesar y consultar información de cheques
bancarios almacenados en un archivo CSV. El script debe permitir a los 
usuariosfiltrar y visualizar los datos de los cheques emitidos y depositados
por un cliente específico, considerando diferentes criterios de filtrado, 
como el estado del chequey el rango de fechas. Además, se debe gestionar 
la exportación de datos a unarchivo CSV si es necesario.

Este tipo de archivo se sabe que contiene los siguientes campos con la
siguiente información:

NroCheque: Número de cheque, este debe ser único por cuenta.
CodigoBanco: Código numérico del banco, entre 1 y 100.
CodigoScurusal: Código numérico de la sucursal del banco va entre 1 y 300.
NumeroCuentaOrigen: Cuenta de origen del cheque.
NumeroCuentaDestino: Cuenta donde se cobra el cheque.
Valor: float con el valor del cheque.
FechaOrigen: Fecha de emisión: (En timestamp)
FechaPago: Fecha de pago o cobro del cheque (En timestamp)
DNI: String con DNI del cliente donde se permite identificarlo
Estado: Puede tener 3 valores pendiente, aprobado o rechazado.

Requisitos Específicos:

Nombre del Archivo: El script de Python se debe llamar listado_cheques.py.

Argumentos de Línea de Comando:

Nombre del archivo CSV: Se debe proporcionar el nombre del archivo CSV
que contiene los registros de los cheques.
DNI del Cliente: Se debe proporcionar el DNI del cliente para el cual se
realizará la consulta.
Salida (PANTALLA o CSV): El usuario puede elegir si desea ver los resultados
en la pantalla o exportarlos a un archivo CSV.
Tipo de Cheque (EMITIDO o DEPOSITADO): El usuario debe especificar si
desea consultar cheques emitidos o depositados.
Estado del Cheque (Opcional): El usuario puede proporcionar un estado de
cheque (PENDIENTE, APROBADO, RECHAZADO) como criterio de filtrado.
Rango de Fechas (Opcional): El usuario puede especificar un rango de
fechas para filtrar los cheques.

Manejo de Errores:
Si se encuentra un número de cheque repetido en la misma cuenta para un DNI
dado, mostrar un mensaje de error indicando el problema.

Salida de Datos:
Si el parámetro "Salida" es PANTALLA, imprimir por pantalla todos los
valores correspondientes a la consulta.
Si el parámetro "Salida" es CSV, exportar los resultados a un archivo CSV
con el nombre en el formato "<DNI><TIMESTAMP_ACTUAL>.csv". El archivo
CSV debe contener las siguientes columnas: NroCheque, CodigoBanco,
CodigoSucursal, NumeroCuentaOrigen, NumeroCuentaDestino, Valor,
FechaOrigen, FechaPago, DNI, Estado.
Filtrado por Estado (Opcional): Si el estado del cheque no se proporciona
como parámetro, se deben imprimir los cheques sin filtrar por estado.
Documentación y Comentarios: Agregar comentarios descriptivos en el código
para explicar su funcionalidad y proporcionar una documentación clara de
cómousar el script.

Validación de Parámetros: Asegurarse de que los parámetros proporcionados
por el usuario sean válidos y manejar posibles errores de entrada.
Optimización del Código: Considerar la optimización del código para cargar y
procesar grandes conjuntos de datos de manera eficiente.
Manejo de Fechas y Formato CSV: Asegurarse de que las fechas se manejen
correctamente y se formateen adecuadamente al exportar a CSV
'''

import sys
import pandas as pd

#Funciones:

#MANEJO DE ERRORES
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

#Validacion de CSV

def func(): #NroCheque: Número de cheque, este debe ser único por cuenta.
    '''descripcion'''

def func(): #CodigoBanco: Código numérico del banco, entre 1 y 100.
    '''descripcion'''

def func(): #CodigoScurusal: Código numérico de la sucursal del banco va entre 1 y 300.
    '''descripcion'''

def func(): #NumeroCuentaOrigen: Cuenta de origen del cheque.
    '''descripcion'''

def func(): #NumeroCuentaDestino: Cuenta donde se cobra el cheque.
    '''descripcion'''

def func(): #FechaOrigen: Fecha de emisión: (En timestamp)
    '''descripcion'''

def func(): #DNI: String con DNI del cliente donde se permite identificarlo
    '''descripcion'''

def func(): #Estado: Puede tener 3 valores pendiente, aprobado o rechazado.
    '''descripcion'''

def func(): #Validar CSV con las funciones de arriba
    '''descripcion'''

#SALIDA

def func(): #Si el parámetro "Salida" es PANTALLA, imprimir por pantalla todos los
            #valores correspondientes a la consulta.
    '''descripcion'''

def save_in_csv(table:pd): #Si el parámetro "Salida" es CSV, exportar los resultados a un archivo CSV
            #con el nombre en el formato "<DNI><TIMESTAMP_ACTUAL>.csv". El archivo
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

def func(): #Filtrado por Estado (Opcional): Si el estado del cheque no se proporciona
            #como parámetro, se deben imprimir los cheques sin filtrar por estado.
    '''descripcion'''

#Codigo Principal:

table = pd.read_csv('data/ejemplo.csv', sep=',', decimal= ".")