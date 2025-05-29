# Dado un texto, contar cuantas veces aparece cada palabra.

def contar_palabras(texto):
    palabras = texto.split(" ")
    actual = palabras[0]
    res = {}
    while (actual != None):
        if (actual in palabras):
            res[actual] =res.get(actual, 0) + 1
            palabras.remove(actual)
        if (len(palabras)>0):
            actual = palabras[0]
        else:
            actual = None
    return res


print(contar_palabras("Hola mundo Hola"))
print(contar_palabras("lorem ipsum dolor sit amet ipsum lorem dolor dolor"))