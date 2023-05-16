def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
numero = int(input("Ingrese un número: "))
resultado = factorial(numero)
print("El factorial de", numero, "es:", resultado)
