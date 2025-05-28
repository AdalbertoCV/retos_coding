def factorial(n):
    if n <= 1:
        return 1
    return factorial(n-1) * n


print(factorial(int(input("Ingrese el numero a calcular el factorial"))))