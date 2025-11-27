"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    x = open("files/input/data.csv", "r").readlines()

    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]

    y = list(z[0] for z in x)

    diccionario = {}

    for i in range(len(y)):
        if y[i] not in diccionario:
            diccionario[y[i]] = 0
        diccionario[y[i]] += int(x[i][1])

    diccionario = list(diccionario.items())
    diccionario.sort()


    return(diccionario)

