def fibonacci(n):
    fib = [0, 1]  # Inicializar la lista con los primeros dos números de Fibonacci
    
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])  # Agregar el siguiente número a la lista
    
    return fib

# Ejemplo de uso
n = int(input("Ingrese el valor de N: "))
resultado = fibonacci(n)
print("La serie de Fibonacci es:", resultado)
