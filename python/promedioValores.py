# Dado un diccionario, obtener el promedio de sus valores.

def promedio_dict(dict):
    suma = 0
    for key in dict:
        suma+= dict.get(key)
    return suma/len(dict)


print(promedio_dict({"Hola":10, "Mundo":20}))