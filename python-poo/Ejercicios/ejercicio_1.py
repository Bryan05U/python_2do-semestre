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
        self.estatura = estatura
        self.peso = peso

    # Métodos (Comportamientos)
    def hablar(self):
        print(f"{self.nombre} está hablando sobre política")

    def caminar(self):
        print(f"{self.nombre} está caminando por las calles")

    def comer(self):
        print(f"{self.nombre} está comiendo pizza")

    def calcularIMC(self):
        print(f"El IMC es de: ", (math.trunc(self.peso / self.estatura **2)))

    def promedio_asignatura(self, n1, n2, n3):
        print(f"El promedio de la asignatura es de: ", {self.n1}+{self.n2}+{self.n3} / 3)
        n1 = 4.5
        n2 = 3.7
        n3 = 4.4

# Creación de un objeto de la clase Persona y agregando los atributos
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
persona1.calcularIMC()