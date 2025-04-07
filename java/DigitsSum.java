// Descripción del reto: Sumar los dígitos de un número

// Este programa tiene como objetivo recibir un número entero positivo e imprimir la suma de sus dígitos, 
// o bien, si el número tiene solo un dígito, imprimir el número tal cual.

// Ejemplo de entrada:
// 1234

// Ejemplo de salida:
// 10

// Ejemplo de entrada:
// 5

// Ejemplo de salida:
// 5


import java.util.Scanner;

public class DigitsSum {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String num = String.valueOf(in.nextInt());
        in.close();
        printResult(num);
    }

    public static boolean isMoreThanOneDigit(String stringnumber){
        if (stringnumber.length() > 1){
            return true;
        }
        return false;
    }

    public static int sumDigits(String stringnumber){
        int sum = 0;
        for (int i = 0; i < stringnumber.length(); i++){
            sum = sum + Integer.parseInt(String.valueOf(stringnumber.charAt(i)));
        }
        return sum;
    }

    public static void printResult(String stringnumber){
        if (isMoreThanOneDigit(stringnumber)){
            System.out.println(sumDigits(stringnumber));
        }else{
            System.out.println(stringnumber);
        }
    }
}
