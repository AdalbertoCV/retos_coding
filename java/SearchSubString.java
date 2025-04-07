// Descripción del reto: Buscar la cantidad de ocurrencias de una subcadena en una cadena principal

// El reto consiste en implementar un programa que cuente cuántas veces aparece una subcadena en una cadena principal.
// Para ello, el programa recibe una cadena de texto y una subcadena, luego imprime la cantidad de veces que la subcadena aparece en la cadena principal.

// Ejemplo de entrada y salida:
// Entrada: 
// "ababcabcabc"
// "abc"
// Salida:
// Number of occurrences: 3


import java.util.Scanner;

public class SearchSubString {
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        String string = in.nextLine();
        String subString = in.nextLine();
        System.out.println(string);
        System.out.println(subString);
        in.close();
        System.out.println("Number of occurrences: " + String.valueOf(searchString(string, subString)));

    }

    public static int searchString(String string, String subString){
        int cont = 0; 
        while(string.contains(subString)){
            cont++;
            string = string.replaceFirst(subString, "");
        }
        return cont;
    }
}
