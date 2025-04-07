// Descripción del reto: Verificar si el animal favorito es una tortuga

// En este reto, el programa solicita al usuario que ingrese su animal favorito y verifica si ese animal es una tortuga.
// Dependiendo de la respuesta del usuario, el programa mostrará un mensaje correspondiente.

// Ejemplo de entrada y salida:
// Entrada: 
// "gato"
// Salida:
// Ese animal es genial, pero prefiero las tortugas

// Entrada: 
// "Tortuga"
// Salida:
// También me gustan las tortugas.


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Turtles {
    public static void main(String[] args) throws IOException {
        System.out.println("Por favor, escribe tu animal favorito.");
        String animal_favorito = new BufferedReader(new InputStreamReader(System.in)).readLine();
        mostrarMensaje(esTortuga(animal_favorito));
    }

    public static boolean esTortuga(String animal){
        return animal.equalsIgnoreCase("tortuga");
    }

    public static void mostrarMensaje(boolean esTortuga){
        if(!esTortuga){
            System.out.println("Ese animal es genial, pero prefiero las tortugas");
        }
        else{
            System.out.println("También me gustan las tortugas.");
        }
    }
}