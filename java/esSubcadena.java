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
        if (subString.length() > string.length()){
            return false;
        }
        int limite = subString.length();
        int coincidencias = 0;
        int substring_index_start = 0;
        for (int i = 0; i < string.length(); i ++){
            for (int j = substring_index_start; j <subString.length();){
                if (String.valueOf(subString.charAt(j)).equals(String.valueOf(string.charAt(i)))){
                    coincidencias++;
                    if (coincidencias == limite){
                        return true;
                    }
                    substring_index_start++;
                } else{
                    coincidencias = 0;
                }
                break;
            }
        }
        return false;
    }
}