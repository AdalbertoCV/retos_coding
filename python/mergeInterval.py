# 📝 Enunciado: Merge Intervals

# Dado un conjunto de intervalos representado como una lista de listas,
# fusiona todos los intervalos superpuestos y devuelve una nueva lista de intervalos.

# 📌 Ejemplo 1:
# entrada = [[1,3],[2,6],[8,10],[15,18]]
# salida = [[1,6],[8,10],[15,18]]
# 💡 Explicación: El intervalo [1,3] y [2,6] se solapan, por lo que se combinan en [1,6].

# 📌 Ejemplo 2:
# entrada = [[1,4],[4,5]]
# salida = [[1,5]]
# 💡 Explicación: Los intervalos [1,4] y [4,5] se fusionan en [1,5].

# 📌 Ejemplo 3:
# entrada = [[1,3],[5,7],[2,4]]
# salida = [[1,4],[5,7]]
# 💡 Explicación: [1,3] y [2,4] se solapan, por lo que se combinan en [1,4].

# 🔍 Restricciones:
# - 1 <= len(intervalos) <= 10^4
# - intervalos[i] tiene exactamente dos valores: [start, end]
# - 0 <= start <= end <= 10^4

# 🚀 Tu reto:
# Implementa la función merge_intervals(intervalos) que tome una lista de intervalos 
# y devuelva la lista de intervalos fusionados.

def merge_intervals(intervalos):
    anterior = [0,0]
    intervalos.sort()
    for i in intervalos:
        anterior_izquierdo = anterior[0]
        anterior_derecho = anterior[1]
        actual_izquierdo = i[0]
        actual_derecho = i[1]
        if (actual_izquierdo <= anterior_derecho):
            nuevo = [anterior_izquierdo, actual_derecho]
            intervalos.remove(i)
            intervalos.remove(anterior)
            intervalos.append(nuevo)
            intervalos.sort()
        anterior = i
    return intervalos

# Caso 1: Intervalos con solapamiento
intervalos = [[1,3],[5,7],[2,4]]
print(merge_intervals(intervalos))  # ➝ [[1,4], [5,7]]

# Caso 2: Intervalos solapados múltiples veces
intervalos = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervalos))  # ➝ [[1,6],[8,10],[15,18]]

# Caso 3: Intervalos consecutivos que se fusionan completamente
intervalos = [[1,4],[4,5]]
print(merge_intervals(intervalos))  # ➝ [[1,5]]

# Caso 4: Intervalos sin solapamiento
intervalos = [[1,2],[3,4],[5,6]]
print(merge_intervals(intervalos))  # ➝ [[1,2],[3,4],[5,6]]

# Caso 5: Un solo intervalo
intervalos = [[1,3]]
print(merge_intervals(intervalos))  # ➝ [[1,3]]

# Caso 6: Intervalos en desorden
intervalos = [[5,10],[1,3],[2,6],[15,18]]
print(merge_intervals(intervalos))  # ➝ [[1,6],[5,10],[15,18]]

# Caso 7: Intervalos con un solo número (rangos de un solo punto)
intervalos = [[1,1],[2,2],[3,3]]
print(merge_intervals(intervalos))  # ➝ [[1,1],[2,2],[3,3]]
