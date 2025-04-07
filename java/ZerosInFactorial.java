// Descripción del reto: Contar los ceros finales en el factorial de un número

// Este programa tiene como objetivo calcular cuántos ceros finales tiene el factorial de un número dado.
// El factorial de un número n (denotado como n!) es el producto de todos los enteros desde 1 hasta n. Por ejemplo, 5! = 5 * 4 * 3 * 2 * 1 = 120.
// El desafío consiste en determinar cuántos ceros hay al final del número resultante de n! sin calcular el valor completo del factorial.

// Ejemplo de entrada y salida:
// Entrada: 
// 100
// Salida:
// 24
// Explicación: El factorial de 100 tiene 24 ceros finales.


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ZerosInFactorial {
    public static void main(String[] args) throws IOException{
        Long n = Long.parseLong(new BufferedReader(new InputStreamReader(System.in)).readLine());
        System.out.print(countZeros(n));
    }

    public static int countZeros(Long n){
        int count = 0;
        while (n >= 5) {
            n /= 5;
            count += n;
        }
        return count;
    }
}