// Reto: Caminos únicos en una cuadrícula
// Descripción: Implementa un programa en Java que calcule el número de caminos únicos 
// para moverse desde la esquina superior izquierda hasta la esquina inferior derecha 
// de una cuadrícula de tamaño `m x n`. Solo se permiten movimientos hacia la derecha y hacia abajo. 
// Utiliza programación dinámica para optimizar el cálculo.


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class caminosUnicos{
    public static void main(String[] args){
        try{
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int m = Integer.parseInt(br.readLine());
            int n = Integer.parseInt(br.readLine());
            int[][] celdas = new int[m][n];
            llenarMatriz(celdas, m, n);
            System.out.print(calcularCaminosUnicos(celdas, m, n));
        }
        catch(IOException e){
            System.err.println("Error al ingresar los datos.");
        }
    };

    public static void llenarMatriz(int[][] celdas, int m, int n){
        for (int i = 0; i < m; i ++){
            for(int j = 0; j < n; j++){
                celdas[i][j] = 1;
            }
        }
    }

    public static int calcularCaminosUnicos(int[][] celdas, int m, int n){
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                celdas[i][j] = celdas[i - 1][j] + celdas[i][j - 1];
            }
        }

        return celdas[m - 1][n - 1];
    }
};