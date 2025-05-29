# Indicar si una cadena es un palindromo, es decir que se lea igual al derecho y al reves.

from invertirCadena import invertirCadena

def es_palindromo(cadena):
    return cadena.replace(" ","") == invertirCadena(cadena.replace(" ",""))


print(es_palindromo("anita lava la tina"))
print(es_palindromo("hola mundo"))