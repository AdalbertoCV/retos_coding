# dada una lista de numeros, devolver una lista unicamente con los duplicados.

def duplicados(numeros):
    visitados = set()
    duplicados = set()
    for n in numeros:
        if n in visitados:
            duplicados.add(n)
        visitados.add(n)
    return sorted(duplicados)

print(duplicados([1, 2, 3, 2, 4, 5, 1]))
