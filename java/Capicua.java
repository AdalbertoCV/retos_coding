/*
 * Reto: Generador de Números Capicúa
 *
 * Descripción:
 * Un número capicúa es aquel que se lee igual de izquierda a derecha que de derecha a izquierda,
 * como 121, 1331 o 4554. 
 * 
 * El reto consiste en desarrollar un programa en Java que genere el siguiente número capicúa 
 * a partir de un número dado.
 * 
 * Reglas:
 * 1. Si el número ya es capicúa, se debe devolver el siguiente número capicúa más grande.
 * 2. Si el número no es capicúa, encontrar el más cercano que sea mayor.
 * 3. El número ingresado será siempre positivo.
 *
 * Ejemplo de Entrada y Salida:
 * Entrada: 123   → Salida: 131
 * Entrada: 808   → Salida: 818
 * Entrada: 999   → Salida: 1001
 * Entrada: 2023  → Salida: 2112
 * 
 */



import java.util.Scanner;

public class Capicua {
    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        int numero = scanner.nextInt();
        System.out.println(generarSiguienteCapicua(numero));
        scanner.close();
    }

    public static int generarSiguienteCapicua(int numero){
        numero++;
        String num = String.valueOf(numero);
        while (!num.equals(invertirNumero(numero))){
            numero++;
            num = String.valueOf(numero);
        }
        return numero;
    }

    public static String invertirNumero(int numero){
        String res = "";
        String num = String.valueOf(numero);
        for (int i = num.length() - 1; i >= 0; i--){
            res = res + num.charAt(i);
        }
        return res;
    }
}
