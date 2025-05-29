# contar la cantidad de veces que aparece cada letra en un texto ignorando mayusculas y espacios.

def contar_letras(texto):
    texto_ignore_case = texto.lower().replace(" ", "")
    letras = list(texto_ignore_case)
    conteo = {}
    while (len(letras) > 0):
        actual = letras.pop()
        conteo[actual] = conteo.get(actual, 0) + 1
    return conteo



print(contar_letras("Hola hola mundoooooo"))