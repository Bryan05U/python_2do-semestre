# 21 de agosto de 2024
import math
"""
Tomando el código que hemos estado trabajando en la última clase, se solicita agregar nuevas Propiedades a la clase Persona:
• altura (float): Representa la altura de la persona en metros.
• peso (float): Representa el peso de la persona en kilogramos.

Modificar el constructor __init__ para aceptar estos nuevos parámetros y asignarlos a las propiedades correspondientes.
• Agregar un nuevo método para calcular el IMC
  - El método calcular_imc() debe calcular el Índice de Masa Corporal (IMC) de la persona utilizando la fórmula (peso/altura^2)
  - El método debe devolver el valor del IMC y mostrar un mensaje indicando si la persona está en un rango de peso normal, bajo peso, sobrepeso, u obesidad basado en el valor calculado.
• Agregar un método llamado promedio_asignatura() a la clase Persona().
  - Este método debe recibir tres notas (valores de tipo float) como parámetros.
  - El método debe calcular el promedio de estas tres notas.
  - Si el promedio es igual o superior a 4.0, el método debe imprimir un mensaje indicando que la persona aprobó la asignatura; de lo contrario, debe indicar que la persona no aprobó.
"""

class Persona():
    # Constructor de Clase
    def __init__(self, nombre, apellido, edad, estatura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.estatura = float(estatura)
        self.peso = float(peso)

    # Métodos (Comportamientos)
    def hablar(self):
        print(f"{self.nombre} está hablando sobre política")

    def caminar(self):
        print(f"{self.nombre} está caminando por las calles")

    def comer(self):
        print(f"{self.nombre} está comiendo pizza")

    def calcularIMC(self):
        print(f"El IMC es de: ", (math.trunc(self.peso / self.estatura **2)))
        if (self.peso / self.estatura **2) < 18.5:
            print(f"Rango de IMC: por debajo")
        elif (self.peso / self.estatura **2) >= 18.5 and (self.peso / self.estatura **2) < 24.9:
            print(f"Rango de IMC: saludable")
        elif (self.peso / self.estatura **2) >= 25 and (self.peso / self.estatura **2) < 29.9:
            print(f"Rango de IMC: sobrepeso")
        elif (self.peso / self.estatura **2) >= 30 and (self.peso / self.estatura **2) < 34.9:
            print(f"Rango de IMC: obesidad 1")
        elif (self.peso / self.estatura **2) >= 35 and (self.peso / self.estatura **2) < 39.9:
            print(f"Rango de IMC: obesidad 2")
        else:
            print(f"Rango de IMC: obesidad 3")

    def promedio_asignatura(self, n1: float, n2: float, n3: float):
        promedio = (n1 + n2 + n3) / 3
        if promedio >= 4.0:
            print(f"{self.nombre} ha aprobado con un promedio de {promedio}")
        else:
            print(f"{self.nombre} ha reprobado con un promedio de {promedio}")

# Creación de objetos de la clase Persona y agregando los atributos
persona1 = Persona("Bryan", "Cárcamo", 18, 1.75, 90)

# Acceso a los atributos y métodos del objeto
print(f"Nombre: {persona1.nombre}")
print(f"Apellido: {persona1.apellido}")
print(f"Edad: {persona1.edad} años")
print(f"Estatura: {persona1.estatura}")
print(f"Peso: {persona1.peso}")

# Llamando a los métodos de la Clase
persona1.hablar()
persona1.caminar()
persona1.comer()
persona1.calcularIMC() # Calcular IMC
persona1.promedio_asignatura(6.2, 4.4, 5.0) # Promedio notas
