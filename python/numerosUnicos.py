# dada una lista de numeros, devolver una lista nueva solo con los numeros unicos (sin repeticiones)

def numeros_unicos(numeros):
    return list(set(numeros))

print(numeros_unicos([1,1,1,2,3,4,5,6,7]))