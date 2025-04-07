// Descripción del reto: Verificar si una palabra o frase es un palíndromo

// Este programa toma una cadena de texto ingresada por el usuario, elimina los espacios en blanco y convierte la cadena a minúsculas, luego verifica si esa cadena es un palíndromo.
// Un palíndromo es una palabra, frase, número u otra secuencia de caracteres que se lee igual hacia adelante que hacia atrás, ignorando los espacios y mayúsculas.

// Ejemplo de salida:
// Entrada: "A man a plan a canal Panama"
// Salida: true

// Entrada: "hello"
// Salida: false


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Palindromos {
    public static void main(String[] args) throws IOException{
        String string =  new BufferedReader(new InputStreamReader(System.in)).readLine().toLowerCase().replace(" ", "");
        System.out.print(compararCadenas(string, invertirCadena(string)));
    }

    public static boolean compararCadenas(String string1, String string2){
        return string1.equalsIgnoreCase(string2);
    }

    public static String invertirCadena(String string){
        return new StringBuilder(string).reverse().toString();
    }
}