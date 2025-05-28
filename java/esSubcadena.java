// Descripción del reto: Verificar si una cadena es subcadena de otra

// Este programa recibe dos cadenas de texto: una cadena completa y una subcadena. El reto es determinar si 
// la subcadena se encuentra dentro de la cadena completa.

// Ejemplo de entrada:
// "hola"
// "ol"

// Ejemplo de salida:
// true

// Ejemplo de entrada:
// "programacion"
// "python"

// Ejemplo de salida:
// false


import java.util.Scanner;

public class esSubcadena {
    public static void main (String args[]){
        Scanner scanner = new Scanner(System.in);
        String cadena_completa = scanner.nextLine();
        String sub_cadena = scanner.nextLine();

        boolean esSubcadena = isSubString(sub_cadena, cadena_completa);
        System.out.println(esSubcadena);
        scanner.close();
    }

    public static boolean isSubString(String subString, String string){
        int limite = subString.length();
        for (int i = 0; i < string.length() - 1; i++){
            if (string.substring(i, i + limite).equals(subString)){
                return true;
            }
        }
        return false;
    }
}