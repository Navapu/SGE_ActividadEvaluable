import sys

# Recibir los argumentos desde la consola
# Recibir los argumentos desde la consola
# Recibir los argumentos desde la consola

argumentos = sys.argv[1:]

# Imprimir los argumentos recibidos
print("Argumentos recibidos:", argumentos)

# Acceder a cada argumento por su posición
if len(argumentos) >= 2:
    parametro1 = argumentos[0]
    parametro2 = argumentos[1]

    print("Primer parámetro:", parametro1)
    print("Segundo parámetro:", parametro2)
else:
    print("Por favor, ingrese al menos dos parámetros desde la consola.")


# Sobrecarga de funciones
# Sobrecarga de funciones
# Sobrecarga de funciones

def funcion_variable(*args):
    """
    Función que acepta un número variable de parámetros.
    """
    if not args:
        print("La función no recibió ningún parámetro.")
    else:
        print("Parámetros recibidos:")
        for parametro in args:
            print(parametro)

# Ejemplos de uso
funcion_variable()
funcion_variable(1, 2, 3)
funcion_variable("a", "b", "c", "d")
