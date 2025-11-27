"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    grupos = {}   

    with open('files/input/data.csv', "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split()

            letra = partes[0]           
            numero = partes[1]          
            numero = int(numero)

            #inicializar si no existe
            if numero not in grupos:
                grupos[numero] = set([letra])
            else:
                grupos[numero].add(letra)
            #Se usan sets para evitar que elementos se repetan

    resultado = []
    for numero, letras in grupos.items():
        lista_ordenada = sorted(list(letras))
        resultado.append((numero, lista_ordenada))

    return sorted(resultado)

print(pregunta_08())