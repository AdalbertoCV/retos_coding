def esPrefijoOSufijo(cadena, subcadena):
    if cadena == subcadena:
        print("La subcadena es prefijo y sufijo (son iguales)")
    elif cadena[0:len(subcadena)] == subcadena and len(cadena) > len(subcadena):
        print("La subcadena es prefijo.")
    elif cadena[len(cadena)- len(subcadena):len(cadena)] == subcadena and len(cadena) > len(subcadena):
        print("La subcadena es sufijo.")
    else:
        print("La cadena no es prefijo ni sufijo.")
    

esPrefijoOSufijo("adiosmundo", "adios") # La subcadena es prefijo.
esPrefijoOSufijo("mundo adios", "adios") # La subcadena no es ni prefijo ni sufijo.
esPrefijoOSufijo("mundo adios", "mundo")  # La subcadena es prefijo.
esPrefijoOSufijo("mundo mundo", "mundo")  # La subcadena es prefijo.
esPrefijoOSufijo("buenosdiasadios", "adios")  # La subcadena es sufijo.
esPrefijoOSufijo("adios", "adios")  # La subcadena es prefijo y sufijo (son iguales).
esPrefijoOSufijo("abcde", "fgh")  # La subcadena no es ni prefijo ni sufijo.
esPrefijoOSufijo("hi", "hola")  # La subcadena no es ni prefijo ni sufijo.
