# 📜 Reto: El número escondido 🔢
# 
# Tienes un número entero positivo N y una lista de números enteros. 
# Debes encontrar cuántas veces aparece N dentro de la lista.
#
# 📥 Entrada:
# - Un número entero N (1 ≤ N ≤ 100).
# - Una lista de M números enteros separados por espacios (1 ≤ M ≤ 1000, cada número entre 1 y 100).
#
# 📤 Salida:
# - Un solo número indicando cuántas veces aparece N en la lista.
#
# 🔹 Ejemplo 1:
# 📌 Entrada:
# 5
# 1 5 3 5 7 5 9
#
# 📌 Salida:
# 3
# (El número 5 aparece 3 veces en la lista).
#
# 🔹 Ejemplo 2:
# 📌 Entrada:
# 2
# 8 6 4 3 9 7
#
# 📌 Salida:
# 0
# (El número 2 no está en la lista).
#
# 🎯 Restricciones y Consideraciones:
# - No puedes usar la función count() de Python o métodos similares en otros lenguajes.
# - Debes recorrer la lista manualmente y contar las ocurrencias de N.

def contarOcurrencias(lista, num):
    ocurrencias = 0
    for n in lista:
        if n == num:
            ocurrencias += 1
    return ocurrencias


lista = [1,1,2,3,4,5,1,9,1]
print(contarOcurrencias(lista, 1))