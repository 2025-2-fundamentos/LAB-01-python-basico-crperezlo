"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    x = open("files/input/data.csv", "r").readlines()

    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]

    x = list(z[0] for z in x)
    x.sort()

    lista = []
    elementos = []

    for element in x:
        if element not in elementos:
            elementos.append(element)
            lista.append((element, x.count(element)))


    return(lista)

