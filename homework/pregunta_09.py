"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    conteo = {} 

    with open('files/input/data.csv', "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split()
            if len(partes) < 5:
                continue

            columna5 = partes[4] 
            pares = columna5.split(",")

            claves_vistas = set()

            for par in pares:

                clave = par.split(":")[0]

                if clave not in claves_vistas:
                    claves_vistas.add(clave)
                    conteo[clave] = conteo.get(clave, 0) + 1

    # Ordenar el diccionario alfabéticamente por clave
    diccionario_ordenado = {k: conteo[k] for k in sorted(conteo.keys())}

    return diccionario_ordenado

print(pregunta_09())