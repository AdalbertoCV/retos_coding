// estrcutura de datos de apoyo para los retos

public class Nodo {
    String valor;
    Nodo nodo_izquierdo;
    Nodo nodo_derecho;

    public Nodo(String valor){
        this.valor = valor;
    }

    public String getValor() {
        return valor;
    }

    public void setValor(String valor) {
        this.valor = valor;
    }

    public void setNodo_derecho(Nodo nodo_derecho) {
        this.nodo_derecho = nodo_derecho;
    }

    public void setNodo_izquierdo(Nodo nodo_izquierdo) {
        this.nodo_izquierdo = nodo_izquierdo;
    }

    public Nodo getNodo_derecho() {
        return this.nodo_derecho;
    }

    public Nodo getNodo_izquierdo() {
        return this.nodo_izquierdo;
    }
}
