"""
Crea una función que reciba una lista de tareas y devuelva un plan de ejecución diario, respetando su frecuencia.
"""

def planificar_tareas(tareas, dias):
    diccionario = {i: [] for i in range(1, dias + 1)}
    for tarea in tareas:
        nombre = tarea["nombre"]
        frecuencia = tarea["frecuencia"]
        for dia in range(1, dias + 1, frecuencia):
            diccionario[dia].append(nombre)
    return diccionario
        


tareas = [
    {"nombre": "Backup DB", "frecuencia": 1},  # cada día
    {"nombre": "Reporte ventas", "frecuencia": 2},  # cada 2 días
    {"nombre": "Actualizar sistema", "frecuencia": 3}
]

print(planificar_tareas(tareas, 4))