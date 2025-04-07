// Descripción del reto: Imprimir números pares en un rango dado

// Este programa recibe dos números enteros, uno como "inicio" y otro como "fin", e imprime todos los números pares dentro de ese rango, incluyendo ambos límites si son pares.
// Si el rango es inválido (es decir, si el número de inicio es mayor que el número de fin o el inicio es negativo), el programa imprime un arreglo vacío ("[]").

// Ejemplo de salida:
// Entrada: 1 10
// Salida: [2, 4, 6, 8, 10]

// Entrada: 5 3
// Salida: []


import java.util.ArrayList;
import java.util.Scanner;

public class PairNumbers {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int start = in.nextInt();
        int end = in.nextInt();
        printResult(start, end);
        in.close();
    }

    public static void printResult(int start, int end){
        if (limitsAreValid(start, end)){
            System.out.println(returnPairs(start, end));
        }
        else{
            System.out.println("[]");
        }
    }

    public static boolean limitsAreValid(int start, int end){
        if ((start > 0) && (start > end)){
            return false;
        }
        return true;
    }

    public static ArrayList<Integer> returnPairs(int start, int end){
        ArrayList<Integer> pairs = new ArrayList<>();
        for (int i = start; i <= end; i++){
            if (i % 2 == 0){
                pairs.add(i);
            }
        }
        return pairs;
    }
}
