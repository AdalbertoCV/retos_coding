# Indicar su una cadena es sucadena de otra

def esSubString(cadena, subcadena):
    limite = len(subcadena)
    for i in range(len(cadena)):
        if cadena[i:i+limite] == subcadena:
            return True
    return False

print(esSubString(input("Ingrese una cadena:\n"), input("Ingrese la subcadena a buscar:\n")))