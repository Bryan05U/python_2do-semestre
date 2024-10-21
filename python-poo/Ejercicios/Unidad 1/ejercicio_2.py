# 21 de agosto de 2024
import math
"""
Crea la clase Coche que contenga las siguientes propiedades:
• marca (string): La marca del coche.
• gasolina (float): La cantidad de gasolina disponible en el coche.

La clase tendrá un método llamado conducir() que recibirá como argumento el número de kilómetros a
recorrer y sumará los kilómetros recorridos al valor de la propiedad kilometros_recorridos. Por cada 10
kilómetros recorridos, se restará 1 litro de gasolina al valor de la propiedad gasolina. Si la gasolina no es
suficiente para recorrer la distancia solicitada, el coche conducirá solo hasta donde alcance la gasolina y
mostrará un mensaje indicando que se ha quedado sin gasolina.

Además, la clase contendrá otro método llamado cargar_gasolina() que recibirá como argumento los
litros de gasolina que se desean agregar al coche, sumando estos litros al valor de la propiedad gasolina.
"""

class Coche():
    # Constructor de Clase
    def __init__(self, marca, bencina):
        self.marca = marca
        self.bencina = bencina
        self.km_recorridos = 0

    # Métodos (Comportamientos)
    def conducir(self, kilómetros):
       bencina_necesaria = kilómetros / 10

       # Averiguar si hay bencina suficiente
       if bencina_necesaria <= self.bencina:
        self.update_estado(kilómetros, bencina_necesaria)
        print(f"Has recorrido {kilómetros} kilómetros. Litros de bencina restantes: {self.bencina}")
       else:
        km_posibles = self.bencina * 10
        self.update_estado(km_posibles, self.bencina)
        print(f"Después de recorrer {km_posibles} kilómetros, la bencina se terminó")

    def cargar_bencina(self, litros):
       self.bencina += litros
       print(f"Agregaste {litros} litros de bencina. La cantidad actual son {self.bencina} litros de bencina")

    def update_estado(self, kilómetros, bencina_usada):
       self.km_recorridos += kilómetros
       self.bencina -= bencina_usada

# Uso del class Coche()
mi_coche = Coche("Toyota", 10)

# Acceso a los atributos y métodos del objeto
print(f"Tu marca de coche: {mi_coche.marca}")

# Llamando a los métodos de la Clase
mi_coche.conducir(50)
mi_coche.conducir(60)
mi_coche.cargar_bencina(5)
mi_coche.conducir(30)
