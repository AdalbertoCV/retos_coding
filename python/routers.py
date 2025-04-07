# Reto: Algoritmo de Kruskal para Árbol de Expansión Mínimo
# Descripción: Implementa el algoritmo de Kruskal en Python para encontrar el Árbol de Expansión Mínimo (MST) 
# en un grafo no dirigido y ponderado. El programa debe recibir el número de routers (nodos) y cables (aristas), 
# luego procesar las conexiones y calcular el costo mínimo necesario para conectar todos los routers.
# Utiliza la estructura de conjuntos disjuntos (Union-Find) para optimizar la unión y búsqueda de conjuntos.


parent = []
rank = []
def init(n):
    for i in range(n):
        parent[i] = i
        rank[i] = 0
def find(a):
    if (parent[a] != a):
        parent[a] = find(parent[a])
    return parent[a]
def union(a, b):
    a = find(a)
    b = find(b)
    if (a != b):
        if (rank[a] < rank[b]):
            parent[a] = b
        elif (rank[b] < rank[a]):
            parent[b] = a
        else:
            parent[b] = a
            rank[a] = rank[a] + 1
def kruskal():
    init(routers)
    for e in aristas:
        if (find(e[0]) != find(e[1])):
            union(e[0], e[1])
            mst.append(e)
entrada = input().split(" ")
routers = int(entrada[0])
cables = int(entrada[1])
aristas = []
mst = []
for i in range(cables+1):
    parent.append(0)
    rank.append(0)
    cable = input().split(" ")
    origen = int(cable[0])
    destino = int(cable[1])
    peso = int(cable[2])
    aristas.append([origen, destino, peso])
aristas.sort(key=lambda x: x[2])
kruskal()
suma = 0
for e in mst:
    suma = suma + e[2]
print(suma)