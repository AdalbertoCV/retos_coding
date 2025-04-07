// Descripción del reto: FizzBuzz

// Este programa resuelve el clásico problema de FizzBuzz, en el que se imprimen los números del 1 al 100, pero con ciertas reglas:
// 1. Si un número es divisible entre 3, se imprime "Fizz".
// 2. Si un número es divisible entre 5, se imprime "Buzz".
// 3. Si un número es divisible tanto entre 3 como entre 5, se imprime "FizzBuzz".
// 4. Si no es divisible entre 3 ni entre 5, simplemente se imprime el número.

// Ejemplo de salida:
// 1
// 2
// Fizz
// 4
// Buzz
// Fizz
// 7
// 8
// Fizz
// Buzz
// Fizz
// 13
// 14
// FizzBuzz
// 16
// ...


public class FizzBuzz {
    public static void main(String[] args) {
        int cont = 1;
        while (cont < 101){
            if (cont % 3 == 0 && cont % 5 == 0){
                System.out.println("FizzBuzz");
            }
            else{
                if (cont % 3 == 0){
                    System.out.println("Fizz");
                }
                else{
                    if (cont % 5 == 0){
                        System.out.println("Buzz");
                    }
                    else{
                        System.out.println(cont);
                    }
                }
            }
            cont++;
        }
        
    }
}
