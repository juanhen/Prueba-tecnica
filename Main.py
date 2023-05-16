import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
from tkinter import ttk

# Configuración de la conexión a la base de datos
config = {
    'user': 'root',
    'password': '0314',
    'host': 'localhost',
    'database': 'prueba',
    'raise_on_warnings': True
}

# Función para obtener los registros de la base de datos
def obtener_registros():
    try:
        # Establecer conexión a la base de datos
        cnx = mysql.connector.connect(**config)

        # Realizar la consulta a la base de datos
        cursor = cnx.cursor()
        query = "SELECT * FROM registros"
        cursor.execute(query)

        # Obtener los resultados de la consulta
        registros = cursor.fetchall()

        # Cerrar cursor y conexión
        cursor.close()
        cnx.close()

        return registros
    except mysql.connector.Error as err:
        print("Error al intentar conectar a la base de datos:", err)

# Función para mostrar los registros en la tabla
def mostrar_registros():
    # Obtener los registros de la base de datos
    registros = obtener_registros()

    # Limpiar la tabla
    for row in tabla.get_children():
        tabla.delete(row)

    # Insertar los registros en la tabla
    for registro in registros:
        tabla.insert('', 'end', text=registro[0], values=(registro[1], registro[2], registro[3], registro[4]))

# Función para registrar en la base de datos
def registrar_en_bd(tipo_prueba, variables, resultado):
    try:
        # Establecer conexión a la base de datos
        cnx = mysql.connector.connect(**config)

        # Obtener fecha y hora actual
        fecha_hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Insertar registro en la base de datos
        cursor = cnx.cursor()
        insert_query = "INSERT INTO registros (fecha_hora, tipo_prueba, variables, resultado) VALUES (%s, %s, %s, %s)"
        registro = (fecha_hora_actual, tipo_prueba, variables, resultado)
        cursor.execute(insert_query, registro)
        cnx.commit()

        # Cerrar cursor y conexión
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error de acceso a la base de datos. Verifica las credenciales.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos especificada no existe.")
        else:
            print("Error al intentar conectar a la base de datos:", err)

# Ejemplo de cómo registrar en la base de datos
def es_palindroma():
    palabra = entrada_palabra.get().lower().replace(" ", "")
    if palabra == palabra[::-1]:
        messagebox.showinfo("Palíndroma", "La palabra es palíndroma.")
        registrar_en_bd("Palíndroma", palabra, "Palíndroma")
    else:
        messagebox.showinfo("No Palíndroma", "La palabra no es palíndroma.")
        registrar_en_bd("Palíndroma", palabra, "No Palíndroma")

def fibonacci():
    try:
        n = int(entrada_fibonacci.get())
        if n < 1:
            raise ValueError
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        messagebox.showinfo("Fibonacci", "La serie de Fibonacci es: {}".format(fib))
       # Registro en la base de datos
        tipo_prueba = "Fibonacci"
        variables = str(n)
        resultado = str(fib)
        registrar_en_bd(tipo_prueba, variables, resultado)
        
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número entero mayor a cero.")

def par_impar():
    try:
        numero = int(entrada_par_impar.get())
        if numero % 2 == 0:
            messagebox.showinfo("Par", "El número es par.")
            registrar_en_bd("Par o Impar", numero, "Par")
        else:
            messagebox.showinfo("Impar", "El número es impar.")
            registrar_en_bd("Par o Impar", numero, "impar")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número entero.")

def multiplos():
    try:
        x = int(entrada_multiplos_x.get())
        n = int(entrada_multiplos_n.get())
        if x < 1 or n < 1:
            raise ValueError
        multiplos_list = [str(i) for i in range(1, n+1) if i % x == 0]
        count = len(multiplos_list)  # Contar los múltiplos
        messagebox.showinfo("Múltiplos", "Encontrados: {}Múltiplos: {}".format(count, " ".join(multiplos_list)))
                # Registro en la base de datos
        tipo_prueba = "Múltiplos"
        variables = "x={}, n={}".format(x, n)
        resultado = "Encontrados: {}Múltiplos: {}".format(count, " ".join(multiplos_list))
        registrar_en_bd(tipo_prueba, variables, resultado)
    except ValueError:
        messagebox.showerror("Error", "Ingrese números enteros mayores a cero.")
def factorial():
    try:
        numero = int(entrada_factorial.get())
        if numero < 0:
            raise ValueError
        def factorial_recursive(n):
            if n == 0:
                return 1
            else:
                return n * factorial_recursive(n - 1)
        resultado = factorial_recursive(numero)
        messagebox.showinfo("Factorial", "El factorial de {} es: {}".format(numero, resultado))
                # Registro en la base de datos
        tipo_prueba = "Factorial"
        variables = "n={}".format(numero)
        resultado = "El factorial de {} es: {}".format(numero, resultado)
        registrar_en_bd(tipo_prueba, variables, resultado)
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número entero no negativo.")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Prueba de algoritmos")

# Etiquetas
etiqueta_palabra = tk.Label(ventana, text="Palabra:")
etiqueta_palabra.grid(row=0, column=0, sticky=tk.W)
etiqueta_fibonacci = tk.Label(ventana, text="Número (Fibonacci):")
etiqueta_fibonacci.grid(row=1, column=0, sticky=tk.W)
etiqueta_par_impar = tk.Label(ventana, text="Número (Par/Impar):")
etiqueta_par_impar.grid(row=2, column=0, sticky=tk.W)
etiqueta_multiplos_x = tk.Label(ventana, text="X (Múltiplos):")
etiqueta_multiplos_x.grid(row=3, column=0, sticky=tk.W)
etiqueta_multiplos_n = tk.Label(ventana, text="N (Múltiplos):")
etiqueta_multiplos_n.grid(row=4, column=0, sticky=tk.W)
etiqueta_factorial = tk.Label(ventana, text="Número (Factorial):")
etiqueta_factorial.grid(row=5, column=0, sticky=tk.W)
#Entradas
entrada_palabra = tk.Entry(ventana)
entrada_palabra.grid(row=0, column=1)
entrada_fibonacci = tk.Entry(ventana)
entrada_fibonacci.grid(row=1, column=1)
entrada_par_impar = tk.Entry(ventana)
entrada_par_impar.grid(row=2, column=1)
entrada_multiplos_x = tk.Entry(ventana)
entrada_multiplos_x.grid(row=3, column=1)
entrada_multiplos_n = tk.Entry(ventana)
entrada_multiplos_n.grid(row=4, column=1)
entrada_factorial = tk.Entry(ventana)
entrada_factorial.grid(row=5, column=1)

#Botones
boton_palindroma = tk.Button(ventana, text="Verificar Palíndroma", command=es_palindroma)
boton_palindroma.grid(row=0, column=2)
boton_fibonacci = tk.Button(ventana, text="Generar Fibonacci", command=fibonacci)
boton_fibonacci.grid(row=1, column=2)
boton_par_impar = tk.Button(ventana, text="Verificar Par/Impar", command=par_impar)
boton_par_impar.grid(row=2, column=2)
boton_multiplos = tk.Button(ventana, text="Buscar Múltiplos", command=multiplos)
boton_multiplos.grid(row=3, column=2)
boton_factorial = tk.Button(ventana, text="Calcular Factorial", command=factorial)
boton_factorial.grid(row=5, column=2)

#Ejecutar ventana

# Crear la ventana
ventana = tk.Tk()
ventana.title("Tabla de Registros")

# Crear una tabla
tabla = ttk.Treeview(ventana)
tabla['columns'] = ('Fecha y Hora', 'Tipo de Prueba', 'Variables', 'Resultado')

# Definir encabezados de la tabla
tabla.heading('#0', text='ID')
tabla.column('#0', width=50)
tabla.heading('Fecha y Hora', text='Fecha y Hora')
tabla.column('Fecha y Hora', width=150)
tabla.heading('Tipo de Prueba', text='Tipo de Prueba')
tabla.heading('Variables', text='Variables')
tabla.column('Variables', width=300)
tabla.heading('Resultado', text='Resultado')
tabla.column('Resultado', width=300)

# Obtener los registros de la base de datos
registros = obtener_registros()

# Insertar los registros en la tabla
for registro in registros:
    tabla.insert('', 'end', text=registro[0], values=(registro[1], registro[2], registro[3], registro[4]))

# Colocar la tabla en la ventana
tabla.pack()

# Botón para actualizar la tabla
boton_actualizar = tk.Button(ventana, text="Actualizar Tabla", command=mostrar_registros)
boton_actualizar.pack()

# Ejecutar ventana
ventana.mainloop()