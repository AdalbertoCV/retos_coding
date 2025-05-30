# dada una lista de numeros, devolver una lista de los cuadrados de los numeros pares

def cuadrados_pares(numeros):
    cuadrados_pares = []
    for n in numeros:
        if int(n) % 2 == 0:
            cuadrados_pares.append(int(n) * int(n))
    return cuadrados_pares

print(cuadrados_pares([1,2,3,4,5,6]))