#include <stdio.h>

// Reto: Comparación de dos números
// Descripción: Escribe un programa en C que solicite al usuario dos números enteros 
// y determine cuál de los dos es mayor o si son iguales. 
// Usa estructuras condicionales `if`, `else if` y `else` para mostrar el resultado correspondiente.

int main() {
    int num1;
    int num2;

    printf("Ingresa el primer numero: \n");
    scanf("%d", &num1);
    printf("Ingresa el segundo numero: \n");
    scanf("%d", &num2);
    

    if (num1 == num2){
        printf("%d y %d son iguales.\n", num1, num2);
    }
    else if (num1 > num2){
        printf("%d es mayor.\n",num1);
    }
    else{
        printf("%d es mayor.\n", num2);
    }
    return 0;
}