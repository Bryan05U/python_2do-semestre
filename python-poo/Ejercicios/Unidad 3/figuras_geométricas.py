# 06 de diciembre de 2024
"""
Problema de Duck Typing

Estás desarrollando una aplicación para calcular el área de diferentes figuras geométricas. La aplicación no debe
preocuparse por el tipo exacto de la figura, sino por si esta puede calcular su área. Utilizando Duck Typing, implementa un
sistema donde cada figura geométrica tenga un método calcular_area() que realice el cálculo correspondiente.
El programa debe incluir las siguientes figuras geométricas:
- Circulo
- Rectángulo
- Triángulo
- Cuadrado 
- Trapecio
- Pentágono Regular

Objetivo
1.Implementar las clases para las figuras mencionadas, asegurando que cada una tenga el método calcular_area().
2.Diseñar una función llamada mostrar_area que reciba cualquier figura geométrica y llame al método calcular_area()
para mostrar el área calculada.
"""
import math

# Clase Círculo
class Círculo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_área(self):
        return math.pi * (self.radio ** 2)

# Clase Rectángulo
class Rectángulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_área(self):
        return self.base * self.altura

# Clase Triángulo
class Triángulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_área(self):
        return 0.5 * self.base * self.altura

# Clase Cuadrado
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_área(self):
        return self.lado ** 2

# Clase Trapecio
class Trapecio:
    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
    
    def calcular_área(self):
        return 0.5 * (self.base_mayor + self.base_menor) * self.altura

# Clase Pentágono Regular
class PentágonoRegular:
    def __init__(self, apotema, perímetro):
        self.apotema = apotema
        self.perímetro = perímetro
    
    def calcular_área(self):
        return 0.5 * self.perímetro * self.apotema

# Función para mostrar el área
def mostrar_área(figura):
    print(f"El área de la figura es: {figura.calcular_área()}")

# Creación de instancias para las figuras
círculo = Círculo(5)
rectángulo = Rectángulo(4, 6)
triángulo = Triángulo(3, 4)
cuadrado = Cuadrado(4)
trapecio = Trapecio(6, 4, 5)
pentágono = PentágonoRegular(3, 20)

# Mostrar áreas
mostrar_área(círculo)
mostrar_área(rectángulo)
mostrar_área(triángulo)
mostrar_área(cuadrado)  
mostrar_área(trapecio)
mostrar_área(pentágono)
