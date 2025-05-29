# Indicar si los parentesis de un texto estan balanceados o no lo estan.

def esta_balanceado(text):
    pila = []
    for c in text:
        if c == "(":
            pila.append(c)
        elif c == ")":
            if len(pila) == 0:
                return False
            pila.pop()
    return len(pila) == 0
        



print(esta_balanceado(" hola ()"))
print(esta_balanceado(" hola )("))
print(esta_balanceado(" hola ()()("))
print(esta_balanceado(" hola ()"))
print(esta_balanceado(" hola ())()"))