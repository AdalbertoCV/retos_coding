# dado un texto, retornar el mismo texto invirtiendo el orden de sus palabras (ej: Hola mundo: mundo Hola)

def invertir_frase(frase):
    frase_list = frase.split(" ")
    frase_inversa = frase_list[::-1]
    return " ".join(frase_inversa)


print(invertir_frase("Hola mundo"))