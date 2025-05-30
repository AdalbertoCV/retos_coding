# dado un diccionario, devolvemos la clave con el valor mas grande.

def valor_mayor(dict):
    mayor = 0
    for key in dict:
        value = dict.get(key)
        if value > mayor:
            mayor = value
            clave_mas_grande = key
    return clave_mas_grande


print(valor_mayor({"Clave 1": 10,"clave 2":20}))