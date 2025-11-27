"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    resultado = []

    with open('files/input/data.csv', "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split()

          
            letra = partes[0]        
            columna4 = partes[3]         
            columna5 = partes[4]         

            # Contar elementos de cada columna
            elementos_col4 = len(columna4.split(","))
            elementos_col5 = len(columna5.split(","))

            resultado.append((letra, elementos_col4, elementos_col5))

    return resultado

print(pregunta_10())