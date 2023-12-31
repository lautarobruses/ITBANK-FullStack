# python listado_cheques.py cheques.py 42874892 salida tipo_cheque estado_cheque --fecha rango_fechas

import sys
import pandas as pd
import numpy as np
from datetime import datetime

#CAMPOS TABLA
NRO_CHEQUE, COD_BANCO, COD_SUCURSAL, NRO_CUENTA_ORIGEN, NRO_CUENTA_DESTINO, VALOR, FECHA_ORIGEN, FECHA_PAGO, DNI, ESTADO = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#ARGUMENTOS
ANTE_ULTIMO, ULTIMO, NOMBRE_ARCHIVO, DNI_CLIENTE, SALIDA_PANTALLA, TIPO_CHEQUE, ESTADO_CHEQUE, TIPO_FECHAS, RANGO_FECHAS = (-2, -1, 1, 2, 3, 4, 5, 6, 7)

def muestraMensajeError(causa:str): 
    print(f"ERROR: {causa}")   
    print("El formato esperado es el siguiente:")   
    print("\n> python listado_cheques.py cheques.csv (DNI) (salida) (tipo-cheque) [estado-cheque] --fecha [aaaa-mm-dd:aaaa-mm-dd\n")   
    print("Los parentesis () indican que el parametro es obligatorio y los corchetes [] que es opcional.")   

#Validacion de datos de entrada:
def validaDNI(dni:str): 
    '''
    Esta funcion verifica si el formato de un DNI es valido.
    El DNI debe tener digitos numericos, ser mayor que 0 y no tener una longitud mayor a 8 caracteres.

    :param dni: DNI ingresado por el usuario.
    :type dni: string
    :return: Si el DNI es correcto.
    :rtype: bool
    '''
    return dni.isdigit() and int(dni) > 0 and len(dni) <= 8

def validaSalida(salida:str):
    '''
    Esta funcion verifica si el formato del parametro SALIDA es valido.
    El parametro ingresado debe ser igual a "PANTALLA" o "CSV".

    :param salida: tipo de salida deseada por el usuario.
    :type salida: string
    :return: Si el parametro ingresado es correcto.
    :rtype: bool
    '''
    return salida.upper() == "PANTALLA" or salida.upper() == "CSV"

def validaTipoCheque(tipo_cheque:str): 
    '''
    Esta funcion verifica si el formato del parametro TIPO CHEQUE es valido.
    El parametro ingresado debe ser igual a "EMITIDO" o "DEPOSITADO".

    :param tipo_cheque: tipo de cheque deseado por el usuario.
    :type tipo_cheque: string
    :return: Si el parametro ingresado es correcto.
    :rtype: bool
    '''
    return tipo_cheque.upper() == "EMITIDO" or tipo_cheque.upper() == "DEPOSITADO"

def validaEstadoCheque(estado_cheque:str):
    '''
    Esta funcion verifica si el formato del parametro ESTADO CHEQUE es valido.
    El parametro ingresado debe ser igual a "PENDIENTE" o "APROBADO" o "RECHAZADO".

    :param estado_cheque: estado de cheque deseado por el usuario.
    :type estado_cheque: string
    :return: Si el parametro ingresado es correcto.
    :rtype: bool
    '''
    return estado_cheque.upper() == "PENDIENTE" or estado_cheque.upper() == "APROBADO" or estado_cheque.upper() == "RECHAZADO"

def validaRangoFechas(tipo_fecha:str, rango_fechas:str): 
    '''
    Esta funcion verifica si el rango de fechas ingresado es valido.
    El parametro ingresado debe ser acorde al formato esperado y la fecha de inicio no debe ser mayor a la fecha de fin".

    :param tipo_fecha: argumento que especifica el formato del siguiente argumento.
    :type tipo_fecha: string
    :param rango_fechas: rango de fechas por la cual se desea filtrar los cheques.
    :type rango_fechas: string
    :return: Si el parametro ingresado es correcto.
    :rtype: bool
    '''
    if (tipo_fecha.upper() == "--FECHA"):
        fechas = rango_fechas.split(":")

        if len(fechas) == 2:
            fecha_inicio_str, fecha_fin_str = fechas[0], fechas[1]

            try:
                fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d")
                fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d")

                if fecha_inicio <= fecha_fin:
                    return True
            except ValueError:
                return False
    
    return False

#FILTRO 1
def filterDNI(dataFrame:pd.DataFrame, dni:str):
    dni = int(dni)

    # Filtrar los datos por DNI
    df_filtrado = dataFrame[dataFrame['DNI'] == dni]

    # Verificar si hay números de cheque duplicados para el mismo DNI y cuenta
    duplicados = df_filtrado[df_filtrado.duplicated(['NroCheque', 'NumeroCuentaOrigen'])]

    if not duplicados.empty:
        print("WARNING: Se encontraron números de cheque duplicados para el mismo DNI.")
        print(f'        Se descartaran los valores duplicados de los cheques con los siguientes NroCheque: {duplicados["NroCheque"].values}\n')
        df_filtrado = df_filtrado.drop_duplicates(subset='NroCheque', keep='first')

    return df_filtrado

#FILTRO 2: Tipo de Cheque (EMITIDO o DEPOSITADO)
def filterType(tabla:pd.DataFrame, dni:str, tipo_cheque:str):
    '''
    Filtra los datos de cheques bancarios según el tipo de cheque especificado y el número de DNI.

    :param tabla: Un arreglo de datos que contiene información de cheques bancarios.
    :type tabla: pd.DataFrame
    :param dni: El número de DNI (Documento Nacional de Identidad) como cadena de caracteres.
    :type dni: str
    :param tipo_cheque: El tipo de cheque a filtrar, puede ser "EMITIDO" o "DEPOSITADO".
    :type tipo_cheque: str
    :return: Un nuevo arreglo con los datos de los cheques que coinciden con el tipo especificado.
    :rtype: pd.DataFrame
    ''' 
    dni = int(dni)
    if (tipo_cheque.upper() == 'EMITIDO'):
        resultado = tabla[tabla['NumeroCuentaOrigen'] == dni]
    else:
        resultado = tabla[tabla['NumeroCuentaDestino'] == dni]
    return resultado
    
#FILTRO 3
def filterState(tabla:pd.DataFrame, estado_cheque: str):
    """
    Filtra los datos de cheques bancarios según el estado de cheque especificado(APROBADO, PENDIENTE y REACHAZADO).

    :param tabla: Un arreglo de datos que contiene la información de los cheques bancarios.
    :type tabla: pd.DataFrame
    :param estado_cheque: El estado de cheque a filtrar en mayúsculas.
    :type estado_cheque: str
    :return: Un nuevo arreglo con los datos de los cheques que coinciden con el estado especificado.
    :rtype: np.ndarray
    """
    return tabla[tabla['Estado'] == estado_cheque].to_numpy()

#FILTRO 4
def filterTime(table:np.ndarray, range:str):
    '''
    Filtra la fila 7 del ndarray segun el rango de fechas dado.
    El parametro ingresado debe ser acorde al formato esperado y la fecha de inicio no debe ser mayor a la fecha de fin.

    :param table: argumento que especifica el formato del siguiente argumento.
    :type table: np.ndarray
    :param range: rango de fechas por la cual se desea filtrar los cheques.
    :type rango_fechas: string
    :return: si el parametro ingresado es correcto retorna una tabla filtrado.
    :rtype: np.ndarray
    '''
    min_time_str, max_time_str = range.split(':')
 
    min_time = datetime.fromisoformat(min_time_str).replace(hour=0, minute=0, second=0)
    max_time = datetime.fromisoformat(max_time_str).replace(hour=23, minute=59, second=59)

    table[:, FECHA_PAGO] = [datetime.utcfromtimestamp(x) for x in table[:, FECHA_PAGO]]
    table = table[ (min_time <= table[:, FECHA_PAGO]) & (table[:, FECHA_PAGO] <= max_time)]
    table[:, FECHA_PAGO] = [int(x.timestamp()) for x in table[:, FECHA_PAGO]]

    return table

#SALIDA DE DATOS
def timeToStr(number:int): #FechaOrigen: Fecha de emisión: (En timestamp)
    '''
    Retorna un string de la fecha en timestamp dada.
    El parametro ingresado debe ser acorde al formato esperado.

    :param number: argumento que especifica una fecha.
    :type number: timestamp
    :return: retorna la fecha en un string del tipo YYYY/mm/dd HH:MM:SS.
    :rtype: strig
    '''
    return datetime.utcfromtimestamp(number).strftime('%Y/%m/%d %H:%M:%S')

def printNumpy(table:np.ndarray, head:list|None):
    '''
    Muestra por pantalla la tabla dada junto con el head dado.
    El parametro ingresado debe ser acorde al formato esperado.

    :param table: argumento que especifica una tabla.
    :type table: np.ndarray
    :param head: es la cabecera de la tabla dada, su cantidad de objetos debe ser igual al de cada fila de la tabla.
    :rtype: list
    '''
    if np.size(table) == 0:
        print("No se ha encontrado resultados para los argumentos ingresados.")
    else:
        sep = "|"
        table[:, FECHA_ORIGEN] = [timeToStr(x) for x in table[:, FECHA_ORIGEN]]
        table[:, FECHA_PAGO] = [timeToStr(x) for x in table[:, FECHA_PAGO]]

        if ( head != None ):
            print( sep.join([ x.center(11) for x in map( str, head ) ]) )

        for list in table:
            print( sep.join([ x.center(11) for x in map( str, list ) ]) )

def saveCsv(table:np, head:list|None, dni:int):
    '''Guarda el numpy dado en un archivo <dni><timestamp_actual>.csv.
    El parametro ingresado debe ser acorde al formato esperado.

    :param table: argumento que especifica una tabla.
    :type table: numpy
    :param head: es la cabecera de la tabla dada, su cantidad de objetos debe ser igual al de cada fila de la tabla.
    :rtype: list
    :param dni: es un dni dado por el usuario.
    :rtype: int
    '''
    if np.size(table) == 0:
        print("No se ha encontrado resultados para los argumentos ingresados.")
        print("Se descarta la creacion del CSV.")
    else:
        sep= ","
        strignTable = sep.join(map( str, head ))

        for list in table:
            strignTable = strignTable + '\n' + sep.join(map( str, list ))

        timestamp = int(datetime.timestamp(datetime.now()))
    
        with open(f'{dni}_{timestamp}.csv', 'w') as file: #nombre archivo = <DNI><TIMESTAMP_ACTUAL>.csv
            file.write(strignTable)
            file.close()

        print(f'Se genero el archivos {dni}_{timestamp}.csv con EXITO!')

#CODIGO PRINCIPAL
def main():
    if len(sys.argv) < 5 or len(sys.argv) > 8:
        muestraMensajeError("Los parametros ingresados son incorrectos. Intentelo nuevamente.")
    else:
        try:
            nombre_archivo = sys.argv[NOMBRE_ARCHIVO]
            dataFrame = pd.read_csv(nombre_archivo, sep=',', decimal= ".")

            dni = sys.argv[DNI_CLIENTE]
            salida = sys.argv[SALIDA_PANTALLA]
            tipo_cheque = sys.argv[TIPO_CHEQUE]

            if validaDNI(dni) and validaSalida(salida) and validaTipoCheque(tipo_cheque):
                tablaFiltrada = filterDNI(dataFrame, dni)         
                tablaFiltrada = filterType(tablaFiltrada, dni, tipo_cheque)
                resultado = tablaFiltrada.to_numpy()

                if len(sys.argv) == 6: #El ultimo parametro ingresado es el ESTADO DEL CHEQUE
                    if validaEstadoCheque(sys.argv[ULTIMO]): 
                        estado_cheque = sys.argv[5]
                        resultado = filterState(tablaFiltrada, estado_cheque)
                    else:
                        muestraMensajeError("El ultimo argumento ingresado es incorrecto. Intentelo nuevamente.")
                elif len(sys.argv) == 7: #El ultimo parametro ingresado es el RANGO DE FECHAS
                    if validaRangoFechas(sys.argv[ANTE_ULTIMO], sys.argv[ULTIMO]): 
                        tipo_fecha = sys.argv[ANTE_ULTIMO]
                        rango_fechas = sys.argv[ULTIMO]
                        resultado = filterTime(resultado, rango_fechas)
                    else:
                        muestraMensajeError("El ultimo argumento ingresado es incorrecto. Intentelo nuevamente.")
                elif len(sys.argv) == 8: #El comando posee todos los argumentos posibles
                    estado_cheque = sys.argv[ESTADO_CHEQUE]
                    tipo_fecha = sys.argv[TIPO_FECHAS]
                    rango_fechas = sys.argv[RANGO_FECHAS]
                    
                    if validaEstadoCheque(estado_cheque) and validaRangoFechas(tipo_fecha):
                        resultado = filterState(tablaFiltrada, estado_cheque)
                        resultado = filterTime(resultado, rango_fechas)
                    else:
                        muestraMensajeError("El ultimo argumento ingresado es incorrecto. Intentelo nuevamente.")

                #SALIDA
                head = dataFrame.columns.tolist()

                if (salida == 'PANTALLA'):
                    printNumpy(resultado, head)
                else:
                    saveCsv(resultado, head, int(dni))
            else:
                muestraMensajeError("Los parametros ingresados son incorrectos. Intentelo nuevamente.")
        except pd.errors.ParserError as e:
            muestraMensajeError("Error al leer el archivo CSV.")
        except FileNotFoundError as e:
            muestraMensajeError(f"El archivo {nombre_archivo} ingresado no existe.")

if __name__ == '__main__':
    main() 