# Reto:
# Escribe una función `obtener_kesimo_mayor(arreglo, k)` que reciba una lista de números
# y un número k. La función debe devolver el k-ésimo número más grande del arreglo.
# 
# Reglas:
# - Si k es mayor que la cantidad de números únicos en la lista, devolver None.
# - Si k es 1, devolver el número más grande.
# - La lista puede contener números repetidos, pero solo se consideran valores únicos.
# 
# Ejemplos:
# 
# arreglo = [1, 2, 100, 200, 1, 2, 3]
# print(obtener_kesimo_mayor(arreglo, 2))  # Salida esperada: 100
# 
# arreglo = [10, 20, 30, 40, 50]
# print(obtener_kesimo_mayor(arreglo, 3))  # Salida esperada: 30
# 
# arreglo = [5, 5, 5, 5, 5]
# print(obtener_kesimo_mayor(arreglo, 1))  # Salida esperada: 5
# 
# arreglo = [8, 6, 4, 2]
# print(obtener_kesimo_mayor(arreglo, 5))  # Salida esperada: None


def obtener_mayor(arreglo):
    mas_largo = 0
    for n in arreglo:
        cadena_num = str(n)
        if len(cadena_num) > len(str(mas_largo)):
            mas_largo = n
        else:
            if n > mas_largo:
                mas_largo = n
    arreglo.remove(mas_largo)
    return mas_largo

def obtener_kesimo(arreglo, k):
    if len(arreglo) < k:
        return None
    mas_largo = None
    while k > 0:
        mas_largo = obtener_mayor(arreglo)
        k-=1
    return mas_largo


arreglo = [1,2,100,200,1,2,3]
print(obtener_kesimo(arreglo,2))

arreglo = [10, 20, 30, 40, 50]
print(obtener_kesimo(arreglo, 3)) 

arreglo = [5, 5, 5, 5, 5]
print(obtener_kesimo(arreglo, 1)) 

arreglo = [8, 6, 4, 2]
print(obtener_kesimo(arreglo, 5)) 