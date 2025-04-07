// Descripción del reto: Contar el número de palabras en una frase

// Este programa tiene como objetivo contar el número de palabras en una frase ingresada por el usuario.
// La frase es leída desde la entrada estándar y luego se divide en palabras utilizando el espacio como delimitador.
// Posteriormente, el programa imprime el número total de palabras presentes en la frase.

// Ejemplo de entrada:
// "Hola mundo, ¿cómo estás?"

// Ejemplo de salida:
// 5


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class CountWordsInPhrase {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String phrase = br.readLine();
        String[] words = phrase.split(" ");
        System.out.print(words.length);
    }
}
