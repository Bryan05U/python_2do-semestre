import matplotlib.pyplot as plt

"""
6. Mediante el uso de clases, modelar el movimiento rectilíneo uniforme (MRU) de un objeto utilizando la programación orientada a objetos.
Se deben implementar dos clases:
Cuerpo, que representa un objeto en movimiento con velocidad constante, y SimuladorMovimiento, que se encargará de simular y graficar el movimiento del objeto en función del tiempo.

La clase Cuerpo debe modelar un objeto en movimiento con una velocidad constante.
Mientras que la clase SimuladorMovimiento simula el movimiento y grafica la posición del objeto en función del tiempo utilizando la fórmula del MRU.
Fórmula del MRU:
x = x0 + vt
"""

# Creando una clase Cuerpo que debe representar un objeto en movimiento con velocidad constante
class Cuerpo:
    def __init__(self, posición_inicial, velocidad):
        self.posición_inicial = posición_inicial
        self.velocidad = velocidad
    
    def posición_en_tiempo(self, tiempo):
        return self.posición_inicial + self.velocidad * tiempo
    
# Creando una clase SimuladorMovimiento encargado de simular y graficar el movimiento del objeto en función del tiempo
class SimuladorMovimiento:
    def __init__(self, cuerpo, tiempo_max, intervalos):
        self.cuerpo = cuerpo
        self.tiempo_max = tiempo_max
        self.intervalos = intervalos
    
    # Simulación del movimiento del objeto
    def simular(self):
        tiempos = []
        posiciones = []

        tiempo = 0
        while tiempo <= self.tiempo_max:
            tiempos.append(tiempo)
            posiciones.append(self.cuerpo.posición_en_tiempo(tiempo))
            tiempo += self.intervalos

        return tiempos, posiciones
    
    def graficar(self):
        tiempos, posiciones = self.simular()

        # Generando una gráfica del movimiento del tiempo
        plt.figure(figsize=(10, 6))
        plt.plot(tiempos, posiciones, marker='o', linestyle='-', color='b')
        plt.title('Movimiento Rectilineo Uniforme (MRU)')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Posición (m)')
        plt.grid(True)
        plt.show()

# Crear un objeto Cuerpo con una posicion inicial de 0 y velocidad de 7 m/s
cuerpo = Cuerpo(posición_inicial=0, velocidad=7)

# Crear un 
simulador = SimuladorMovimiento(cuerpo, tiempo_max=10, intervalos=1)

# Ejecutar la simulación y mostrar la gráfica
simulador.simular()

if __name__ == "__main__":
    cuerpo = Cuerpo(posición_inicial=0, velocidad=5) # Posición inicial de 0 y velocidad de 5 m/s
    simulador = SimuladorMovimiento(cuerpo=cuerpo, tiempo_max=10, intervalos=1) # Simular con tiempo máximo de 10 segundos con intervalo de 1 s
    simulador.graficar()