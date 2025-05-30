# dado un texto devolver su palabra mas larga.

def palabra_mas_larga(texto):
    texto = texto.replace(",","").replace(".","").replace(":","").replace(";","")
    palabras = texto.split(" ")
    mayor = palabras[0]
    for palabra in palabras:
        if len(palabra) >= len(mayor):
            mayor = palabra
    return mayor


print(palabra_mas_larga("Hola, este es un texto bastante largo..."))
