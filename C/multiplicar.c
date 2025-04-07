#include <stdio.h>

// Reto: Tabla de multiplicar
// Descripción: Escribe un programa en C que solicite al usuario un número entero 
// y luego imprima la tabla de multiplicar de ese número del 1 al 10. 
// Usa un ciclo `for` para iterar y mostrar los resultados en el formato "n x i = resultado".

int main() {
    int numero;

    printf("Ingresa el número a multiplicar: \n");
    scanf("%d", &numero);

    for (int i = 1; i <=10; i++){
        printf("%d x %d = %d\n", numero, i, numero*i);
    }
}