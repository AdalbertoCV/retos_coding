# RETO: Número equilibrado
# Un número es equilibrado si la suma de sus dígitos en la mitad izquierda es igual a la suma de sus dígitos en la mitad derecha.
# Si el número tiene un número impar de dígitos, el dígito central se ignora.
# Escribe una función que determine si un número dado es equilibrado.
#
# Entrada:
#   - Un número entero positivo.
#
# Salida:
#   - True si el número es equilibrado, False en caso contrario.
#
# Ejemplos:
#   Input: 1230
#   Output: True  (1+2 = 3+0)
#
#   Input: 12530
#   Output: True  (1+2 = 3+0)
#
#   Input: 1463
#   Output: False (1+4 ≠ 6+3)
#
#   Input: 987654
#   Output: True  (9+8+7 = 6+5+4)

#
# ¡Buena suerte!

def es_numero_equilibrado(numero):
    numlist = list(str(numero))
    if not (len(numlist) % 2 == 0):
        numlist.pop(int(len(numlist)/2 + .5) - 1)

    mitad = int(len(numlist) / 2)
    suma_izquierda = 0
    suma_derecha = 0
    for x in range(0,mitad):
        suma_izquierda+= int(numlist[x])
    for y in range(mitad, len(numlist)):
        suma_derecha+= int(numlist[y])
    if (suma_derecha == suma_izquierda):
        return True
    return False



print(es_numero_equilibrado(input()))
