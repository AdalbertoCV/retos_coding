# Reto: Número Mágico
# 
# Escribe una función que determine si un número es un "Número Mágico".
# Un número es considerado mágico si la suma de sus dígitos, repetida hasta
# obtener un solo dígito, da como resultado el número 7.
# 
# Ejemplo de entrada y salida:
# 
# Entrada: 49
# Proceso: 4 + 9 = 13 → 1 + 3 = 4
# Salida: False
# 
# Entrada: 259
# Proceso: 2 + 5 + 9 = 16 → 1 + 6 = 7
# Salida: True
# 
# Entrada: 777
# Proceso: 7 + 7 + 7 = 21 → 2 + 1 = 3
# Salida: False
# 
# Tu tarea es escribir la función `es_numero_magico(num: int) -> bool`
# que reciba un número entero positivo y retorne `True` si es mágico o `False` si no lo es.

def es_numero_magico(numero):
    cadena_numero = str(numero)
    while (len(cadena_numero) > 1):
        suma = 0
        for n in cadena_numero:
            suma+= int(n)
        cadena_numero = str(suma)
    if (suma == 7):
        return True
    return False


print(es_numero_magico(input()))