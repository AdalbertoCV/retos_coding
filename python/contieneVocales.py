# dada una string, determinar si tiene o no al menos una vocal

def contiene_vocales(texto):
    vocales =  ["a", "e", "i", "o", "u"]
    for c in vocales:
        if c in texto:
            return True
    return False


print(contiene_vocales("Hola"))
print(contiene_vocales("ffghj"))