// Descripción del reto: Cifrado César con lista doblemente enlazada

// Este programa implementa el cifrado César utilizando una lista doblemente enlazada para 
// representar el alfabeto. El cifrado César es un tipo de cifrado por sustitución en el que
// cada letra del texto es desplazada un número fijo de lugares en el alfabeto. En este caso, 
// se utiliza una lista doblemente enlazada para almacenar el alfabeto, lo que permite 
// realizar el desplazamiento de manera eficiente, tanto hacia adelante como hacia atrás.


// entrada: Hola Mundo! 3
// salida: krod pxqr!

// entrada: krod pxqr! -3
// salida: hola mundo!


import java.util.Scanner;

public class CifradoCesar {
    public static void main(String args[]){
        String alfabeto = "abcdefghijklmnopqrstuvwxyz";
        Scanner scanner = new Scanner(System.in);
        String cadena = scanner.nextLine();
        int desplazamientos = scanner.nextInt();
        scanner.close();
        ListaLigada lista = new ListaLigada();
        rellenarLista(alfabeto, lista);
        System.out.println(desplazar(cadena, desplazamientos, lista));
    }

    public static void rellenarLista(String alfabeto, ListaLigada lista){
        Nodo anterior = null;
        for (int i = 0; i < alfabeto.length(); i ++){
            char caracter = alfabeto.charAt(i);
            Nodo nodo = new Nodo(String.valueOf(caracter));
            if (nodo.getValor().equals("a")){
                lista.agregar(nodo);
                anterior = nodo;
                continue;
            }
            lista.agregar(nodo);
            nodo.setNodo_izquierdo(anterior);
            anterior.setNodo_derecho(nodo);
            anterior = nodo;
        }
        Nodo primero = lista.getPrimero();
        Nodo ultimo = lista.getUltimo();
        primero.setNodo_izquierdo(ultimo);
        ultimo.setNodo_derecho(primero);
    }

    public static String desplazar(String cadena, int desplazamientos, ListaLigada lista){
        if (desplazamientos == 0){
            return cadena;
        }
        String resultado = "";
        for (int i = 0; i < cadena.length(); i ++){
            Integer posicion = lista.getIndexValor(String.valueOf(cadena.charAt(i)).toLowerCase());
            if (posicion != null){
                lista.apuntar(posicion);
                int desplazamientos_restantes = desplazamientos;
                if (desplazamientos < 0){
                    while (desplazamientos_restantes < 0){
                        desplazamientos_restantes++;
                        lista.anterior();
                    }
                }else{
                    while (desplazamientos_restantes > 0){
                        desplazamientos_restantes--;
                        lista.siguiente();
                    } 
                }
                resultado = resultado + lista.getActual().getValor();
            }else{
                resultado = resultado + String.valueOf(cadena.charAt(i));
            }
        }
        return resultado;
    }
}
