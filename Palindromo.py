def es_palindroma(palabra):
    palabra = palabra.lower()  # Convertir la palabra a minúsculas
    palabra = palabra.replace(" ", "")  # Eliminar espacios en blanco
    
    if palabra == palabra[::-1]:  # Comparar la palabra original con su inversa
        return True
    else:
        return False

# Ejemplo de uso
palabra = input("Ingrese una palabra: ")
if es_palindroma(palabra):
    print("La palabra es palíndroma.")
else:
    print("La palabra no es palíndroma.")
