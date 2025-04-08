# Reto: Contar los Anagramas
# Descripción:
# Escribe una función que reciba dos cadenas de texto y determine si una es un anagrama de la otra.
# Un **anagrama** de una cadena es otra cadena que contiene las mismas letras, pero en un orden diferente.

# Requisitos:
# 1. La función debe ser sensible a mayúsculas y minúsculas (es decir, "Abc" no es un anagrama de "abc").
# 2. Las cadenas pueden tener cualquier longitud, incluyendo cadenas vacías.
# 3. La función debe devolver `True` si las cadenas son anagramas y `False` si no lo son.

# Ejemplos:

# Entrada: "listen", "silent"
# Salida: True  (son anagramas)

# Entrada: "triangle", "integral"
# Salida: True  (son anagramas)

# Entrada: "hello", "world"
# Salida: False (no son anagramas)

# Restricciones:
# - No utilices funciones de ordenamiento (`sort()`, etc.).
# - Debes lograrlo con una eficiencia de O(n), donde n es la longitud de la cadena.


def esAnagrama(cadena1, cadena2):
    coincidencias = 0
    for i in cadena1:
        if i in cadena2:
            coincidencias+=1
    if coincidencias == len(cadena1):
        return True
    return False


cadena1 = input()
cadena2 = input()
print(esAnagrama(cadena1, cadena2))