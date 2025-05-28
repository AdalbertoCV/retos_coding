def fibonacci(n):
    sec = [0,1]
    while len(sec) < n:
        sec.append(sec[-1] + sec[-2])
    return sec

print(fibonacci(int(input("Dijite un numero entero positivo:"))))