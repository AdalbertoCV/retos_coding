/*
 * Reto: Transformación de Números
 *
 * Descripción:
 * Dado un número entero positivo `n`, aplica las siguientes reglas hasta llegar a 1:
 *  - Si `n` es par, divídelo entre 2.
 *  - Si `n` es impar, multiplícalo por 3 y súmale 1.
 * 
 * Devuelve la cantidad de pasos necesarios para llegar a 1.
 *
 * Entrada:
 * - Un número entero positivo `n` (1 ≤ n ≤ 10^6).
 *
 * Salida:
 * - Un solo entero que representa la cantidad de pasos necesarios para reducir `n` a 1.
 *
 * Ejemplo 1:
 * Entrada:
 * 6
 *
 * Proceso:
 * 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
 *
 * Salida:
 * 8
 *
 * Restricciones:
 * - La solución debe ejecutarse en tiempo razonable para valores grandes de `n`.
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class TransformarNumeros {
    public static void main (String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int numero = Integer.parseInt(br.readLine());
        System.out.println(transformar(numero));
        br.close();
    }

    public static int transformar(int num){
        int pasos = 0;
        while (num!=1) {
            if (num % 2 == 0){
                num = num / 2;
            }
            else{
                num = (num * 3) + 1;
            }
            pasos++;
        }
        return pasos;
    }
}
