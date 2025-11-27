"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    suma = {}

    with open('files/input/data.csv', "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split()

            letra = partes[0]         
            col5 = partes[4]        

            pares = col5.split(",")  

            #sumar los numéricos de la columna 5
            total_col5 = 0
            for par in pares:
                if ":" in par:
                    clave, valor_str = par.split(":")
                    total_col5 += int(valor_str)

            ##meterlo al diccionaroo
            if letra not in suma:
                suma[letra] = total_col5
            else:
                suma[letra] += total_col5

    suma_ordenada = {k: suma[k] for k in sorted(suma.keys())}

    return suma_ordenada

print(pregunta_12())
