def imprimir_multiplos(x, n):
    count = 0
    
    for i in range(1, n+1):
        if i % x == 0:
            print(i)
            count += 1
    
    return count

# Ejemplo de uso
x = int(input("Ingrese el valor de X: "))
n = int(input("Ingrese el valor de N: "))
cantidad = imprimir_multiplos(x, n)
print("Cantidad de múltiplos encontrados:", cantidad)
