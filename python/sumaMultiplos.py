# dada una lista de numeros, retornamos la suma de los multiplos de 3 y 5

def suma_multiplos(numeros):
    suma = 0
    for n in numeros:
        if int(n) % 3 == 0 or int(n) % 5 == 0:
            suma+= int(n)
    return suma

print(suma_multiplos([1, 3, 5, 7, 9, 15]))