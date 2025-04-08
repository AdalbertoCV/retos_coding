/**
 * 🔥 Reto: El Número Perfecto
 * 
 * 📜 Descripción:
 * Un número perfecto es un número entero positivo que es igual a la suma de 
 * sus divisores propios (excluyendo el propio número). 
 * Por ejemplo, 6 es un número perfecto porque sus divisores propios son 1, 2 y 3,
 * y 1 + 2 + 3 = 6.
 * 
 * Tu tarea es escribir un programa en Java que reciba un número entero positivo 
 * y determine si es un número perfecto o no.
 * 
 * ✅ Entrada:
 * - Un número entero positivo N (1 ≤ N ≤ 10⁶).
 * 
 * 🔄 Salida:
 * - Imprime "SI" si el número es perfecto.
 * - Imprime "NO" si el número no es perfecto.
 * 
 * 📌 Ejemplos:
 * Entrada 1:
 * 6
 * Salida 1:
 * SI
 * 
 * Entrada 2:
 * 28
 * Salida 2:
 * SI
 * 
 * Entrada 3:
 * 12
 * Salida 3:
 * NO
 * 
 * Entrada 4:
 * 496
 * Salida 4:
 * SI
 * 
 * Entrada 5:
 * 100
 * Salida 5:
 * NO
 * 
 * ¡Buena suerte! 🚀
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class NumeroPerfecto {
    public static void main (String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int numero = Integer.parseInt(br.readLine());
        int suma = calcularSuma(numero);
        System.out.println(esPerfecto(numero, suma));
        br.close();
    }

    public static int calcularSuma(int num){
        int sum = 0;
        int numero_disminuido = num - 1;
        while (numero_disminuido > 0){
            if (num % numero_disminuido == 0){
                sum = sum + numero_disminuido;
            }
            numero_disminuido--;
        }
        return sum;
    }

    public static String esPerfecto(int num, int sum){
        if (num == sum){
            return "SI";
        }
        return "NO";
    }

}
