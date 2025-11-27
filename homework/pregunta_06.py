"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    claves = {}

    with open("files/input/data.csv", "r") as f:
        for linea in f:
            partes = linea.strip().split()
            

            columna = partes[4]

            #Separar cada par clave yvalor
            pares = columna.split(",")

            for par in pares:
                
                clave, valor_str = par.split(":")
                valor = int(valor_str)

                #Inicializar si no existe aún
                if clave not in claves:
                    claves[clave] = [valor, valor]

                else:
                    if valor < claves[clave][0]:
                        claves[clave][0] = valor
                    if valor > claves[clave][1]:
                        claves[clave][1] = valor

    resultado = [(clave, datos[0], datos[1]) for clave, datos in claves.items()]
    return sorted(resultado)

print(pregunta_06())