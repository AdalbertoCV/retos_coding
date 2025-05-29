# Invertir una cadena.

def invertirCadena(cadena):
    res = ""
    limite = len(cadena) -1
    while(limite >= 0):
        res+=cadena[limite]
        limite-=1
    return res



if __name__ == "__main__":
    print(invertirCadena("Hola mundo."))
    print(invertirCadena("este mensaje esta al reves"))
    print(invertirCadena("sever la atse ejasnem etse"))