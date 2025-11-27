"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    suma = {}  

    with open('files/input/data.csv', "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split()
            
            col2 = int(partes[1])  
            col4 = partes[3]              

            letras = col4.split(",")

            for letra in letras:
                if letra not in suma:
                    suma[letra] = col2
                else:
                    suma[letra] += col2

    suma_ordenada = {k: suma[k] for k in sorted(suma.keys())}

    return suma_ordenada

print(pregunta_11())
