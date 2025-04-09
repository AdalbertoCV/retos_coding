# 🏆 Reto: Números Escalera
# 
# Descripción:
# Un número escalera es un número en el que cada dígito es igual o mayor que el anterior.
# Por ejemplo, 123, 555, 789, y 1123 son números escalera, pero 321, 908, y 552 no lo son.
# 
# Tu tarea:
# Escribe una función en Python que reciba un número entero y determine si es un número escalera.

def es_numero_escalera(num):
    cadena_num = str(num)
    anterior = 0
    for n in cadena_num:
        actual = int(n)
        if not actual >= anterior:
            return False
        anterior = actual
    return True


print(es_numero_escalera(123))
print(es_numero_escalera(555))
print(es_numero_escalera(789))
print(es_numero_escalera(1123))
print(es_numero_escalera(321))
print(es_numero_escalera(908))
print(es_numero_escalera(552))