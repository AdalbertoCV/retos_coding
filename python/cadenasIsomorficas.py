# RETO: Verificar si dos cadenas son isomórficas.
# 
# Dos cadenas son isomórficas si cada carácter en la primera cadena 
# se puede mapear de manera única a un carácter en la segunda cadena, 
# manteniendo el orden y sin que dos caracteres distintos de la primera 
# cadena se asignen al mismo carácter en la segunda.
# 
# Ejemplos:
# - son_isomorficas("egg", "add")  -> True
# - son_isomorficas("foo", "bar")  -> False
# - son_isomorficas("paper", "title")  -> True
# - son_isomorficas("aba", "baa")  -> False
# - son_isomorficas("badc", "baba")  -> False
# 
# Escribe una función `son_isomorficas(cadena1, cadena2)` que reciba dos 
# cadenas y devuelva True si son isomórficas, y False en caso contrario.


def obtener_tuplas(cadena1, cadena2):
    if (len(cadena1) != len(cadena2)):
        return False
    asigandas = []
    for n in range (len(cadena1)):
        letra1 = cadena1[n] 
        letra2 = cadena2[n]
        if (letra1, letra2) not in asigandas:
            asigandas.append((letra1, letra2))
    return asigandas
    

def son_isomorficas(cadena1, cadena2):
    tuplas = obtener_tuplas(cadena1, cadena2)
    letras_izquierda = []
    letras_derecha = []
    for t in tuplas:
        if (t[0] not in letras_izquierda):
            letras_izquierda.append(t[0])
        else: 
            return False
        
        if (t[1] not in letras_derecha):
            letras_derecha.append(t[1])
        else:
            return False
    return True


print(son_isomorficas("foo", "bar"))  # False
print(son_isomorficas("egg", "add"))  # True
print(son_isomorficas("paper", "title"))  # True
print(son_isomorficas("aba", "baa"))  # False
print(son_isomorficas("badc", "baba"))  # False
print(son_isomorficas("123", "456"))  # True
print(son_isomorficas("aaa", "bbb"))  # True
print(son_isomorficas("aab", "xyz"))  # False
print(son_isomorficas("abcd", "mnop"))  # True
print(son_isomorficas("add", "arm"))  # False