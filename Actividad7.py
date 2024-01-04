import random

class Car:
    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color

    def imprimir(self):
        print(f"Matrícula: {self.matricula}, Color: {self.color}")

    def cambiar_color(self, nuevo_color):
        print(f"Cambiando el color de {self.matricula} a {nuevo_color}")
        self.color = nuevo_color

    def obtener_informacion(self):
        return f"Matrícula: {self.matricula}, Color: {self.color}"

# Pedir al usuario el número "n" por teclado
n = int(input("Ingrese el número de instancias (n): "))

# Crear "n" instancias de la clase Car
cars = []
for i in range(1, n + 1):
    matricula = i
    color = random.choice(["rojo", "blanco", "negro", "verde", "azul"])
    car = Car(matricula, color)
    cars.append(car)

# Imprimir los valores de las primeras 10 instancias o las "n" instancias si son menos de 10
for i in range(min(n, 10)):
    cars[i].imprimir()

# Ejemplo de cambio de color para la primera instancia
if n > 0:
    nuevo_color = input("Ingrese el nuevo color para el primer carro: ")
    cars[0].cambiar_color(nuevo_color)

# Imprimir la información actualizada para la primera instancia
if n > 0:
    print("Información actualizada para el primer carro:")
    print(cars[0].obtener_informacion())
