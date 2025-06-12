"""
Escribe una función que evalúe un conjunto de reglas sobre un diccionario de datos. 
Cada regla está definida como una tupla con (campo, operador, valor). 
Los operadores pueden ser: "==", "!=", ">", "<", ">=", "<=".
"""


def evaluar_reglas(datos, reglas):
    for campo, operador, valor in reglas:
        if campo not in datos:
            return False
        dato = datos[campo]
        if operador == "==":
            if not dato == valor:
                return False
        elif operador == "!=":
            if not dato != valor:
                return False
        elif operador == ">":
            if not dato > valor:
                return False
        elif operador == "<":
            if not dato < valor:
                return False
        elif operador == ">=":
            if not dato >= valor:
                return False
        elif operador == "<=":
            if not dato <= valor:
                return False
        else:
            return False
    return True

        

datos = {"edad": 30, "pais": "MX", "activo": True}
reglas = [("edad", ">=", 18), ("pais", "==", "MX"), ("activo", "==", True)]

print(evaluar_reglas(datos, reglas))