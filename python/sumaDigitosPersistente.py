#
# Reto: Suma de Dígitos Persistente
# -----------------------------------
# La "suma persistente" de un número es la cantidad de veces que necesitas sumar 
# los dígitos de un número hasta obtener un solo dígito.
# Entrada:
# - Un número entero positivo N (1 <= N <= 10^9)
# Salida:
# - Un número entero que representa la cantidad de sumas necesarias para 
#   reducir el número a un solo dígito.

# Ejemplo 1:
# Entrada:
# 9875
# Salida:
# 3
# Explicación:
# 9 + 8 + 7 + 5 = 29
# 2 + 9 = 11
# 1 + 1 = 2 (ya es un solo dígito, terminamos)
# Se realizaron 3 sumas en total.

# Ejemplo 2:
# Entrada:
# 123456
# Salida:
# 2
# Explicación:
# 1 + 2 + 3 + 4 + 5 + 6 = 21
# 2 + 1 = 3 (ya es un solo dígito, terminamos)
# Se realizaron 2 sumas en total.



def obtenerNumSumas(num):
    cadena = str(num)
    sumas = 0
    while (len(cadena) > 1):
        suma_numero = 0
        for n in cadena:
            suma_numero = suma_numero + int(n)
        cadena = str(suma_numero)
        sumas+=1
    return sumas

print(obtenerNumSumas(input()))