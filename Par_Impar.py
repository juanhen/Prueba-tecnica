def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Ejemplo de uso
numero = int(input("Ingrese un número: "))
if es_par(numero):
    print("El número es par.")
else:
    print("El número es impar.")
