# de un numero dado, filtrar solo los numeros pares en una lista.

def filtrarPares(num):
    pares = []
    for n in str(num):
        if int(n) % 2 == 0:
            pares.append(int(n))
    return pares

print(filtrarPares(12356))
print(filtrarPares(101010234568792938))