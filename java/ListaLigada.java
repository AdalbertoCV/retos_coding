// estructura de datos de apoyo para los retos

import java.util.ArrayList;
import java.util.List;

public class ListaLigada {
    List<Nodo> lista;
    Nodo actual;

    public ListaLigada(){
        this.lista = new ArrayList<>();
    }

    public void imprimir(){
        for (int i = 0; i < this.lista.size(); i++){
            System.out.println(lista.get(i).getValor());
        }
    }

    public Integer getIndexValor(String valor){
        for (int i = 0; i < this.lista.size(); i++){
            if (lista.get(i).getValor().equals(valor)){
                return i;
            }
        }
        return null;
    }

    public void apuntar(int posicion){
        setActual(lista.get(posicion));
    }

    public void agregar(Nodo nodo){
        lista.add(nodo);
    }

    public Nodo getActual(){
        if (lista.size() == 0){
            return null;
        }
        if (actual == null){
            setActual(lista.get(0));
        }
        return this.actual;
    }

    public Nodo getPrimero(){
        if (lista.size() != 0){
            return lista.get(0);
        }
        return null;
    }

    public Nodo getUltimo(){
        if (lista.size() != 0){
            return lista.get(lista.size() - 1);
        }
        return null;
    }

    private void setActual(Nodo actual) {
        this.actual = actual;
    }

    public void siguiente(){
        setActual(actual.getNodo_derecho());
    }

    public void anterior(){
        setActual(actual.getNodo_izquierdo());
    }
}
