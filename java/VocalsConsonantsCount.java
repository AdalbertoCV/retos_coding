// Descripción del reto: Contar vocales y consonantes en un texto dado

// En este reto, el programa cuenta cuántas vocales y cuántas consonantes hay en un texto ingresado por el usuario.
// El programa distingue entre vocales y consonantes, ignorando el caso de las letras (mayúsculas o minúsculas).

// Ejemplo de entrada y salida:
// Entrada: 
// "Hola Mundo"
// Salida:
// Número de vocales en el texto: 4
// Número de consonantes en el texto: 5

// Entrada: 
// "abc efg"
// Salida:
// Número de vocales en el texto: 2
// Número de consonantes en el texto: 6


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class VocalsConsonantsCount {

    public static void main(String[] args) throws IOException {
        String[] vocals = {"a","e","i","o","u"};
        String[] consonants = {"b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"};
        String[] text = new BufferedReader(new InputStreamReader(System.in)).readLine().toLowerCase().split("");
        System.out.println("Número de vocales en el texto: " + String.valueOf(countOcurrences(text, vocals)));
        System.out.println("Número de consonantes en el texto: " + String.valueOf(countOcurrences(text, consonants)));
    }

    public static Long countOcurrences(String[] text, String[] charlist){
        return Arrays.stream(text).filter(character -> Arrays.stream(charlist).anyMatch(x -> x.equalsIgnoreCase(character))).count();
    }
}