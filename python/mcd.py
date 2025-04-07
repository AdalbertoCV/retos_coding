# Reto: Máximo Común Divisor (MCD)
# Descripción: Escribe un programa en Python que calcule el Máximo Común Divisor (MCD) 
# de dos números enteros utilizando el algoritmo de Euclides. 
# El programa debe leer un número `n` de casos de prueba e imprimir el MCD de cada par de números.

def mcd(a, b):
    temp = 0
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
n = int(input())
for i in range (n):
    caso = input().split(" ")
    a = int(caso[0])
    b = int(caso[1])
    print(mcd(a,b))  