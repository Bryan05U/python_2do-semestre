import pygame
import random

"""
2. A continuación, se proporciona el código base puntos rojos que ya caen y se reinician automáticamente en la ventana del juego.
El ejercicio consiste en implementar la clase Triangulo, que representará la nave, y el mecanismo de detección de colisiones.
Crear una nave (representada por un triángulo azul) que se mueva solamente horizontalmente y esquive los puntos rojos que caen desde la parte superior de la pantalla.
Además, deberás implementar la funcionalidad de colisión: si un punto rojo toca el triángulo, el juego se debe cerrar.
Instrucciones:
1. Implementar la clase Triangulo, que simulará la nave espacial. Esta debe moverse de izquierda a derecha con las teclas de flecha (izquierda y derecha).
2. La nave será un triángulo de color azul que se dibujará en la parte inferior de la pantalla.
3. Implementar un método que detecte la colisión entre la nave y los puntos rojos.
4. Cuando se detecte una colisión, el juego debe terminar.
5. Usar las dimensiones del triángulo y el radio de los puntos rojos para calcular si hay una colisión.
Se sugiere usar la distancia entre los centros de ambas figuras para esta detección.
"""

pygame.init()

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Laboratorio N°1 - Ejercicio 2")

# Colores
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

# FPS (Frames por segundo)
FPS = 60
reloj = pygame.time.Clock()

class Puntos:
    def __init__(self, x, y, velocidad):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.radio = 8  # Tamaño del punto

    def mover(self):
        self.y += self.velocidad
        if self.y > ALTO:  # Se reinicia la posición cuando el punto rojo sale de la pantalla
            self.reiniciar()

    def reiniciar(self):
        self.x = random.randint(0, ANCHO - self.radio)
        self.y = random.randint(-100, -40)

    def dibujar(self):
        pygame.draw.circle(pantalla, ROJO, (self.x, self.y), self.radio)

# Clase Triángulo
class Triángulo:
    def __init__(self, x, y, velocidad):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.radio = 20  # Tamaño del punto

    def mover(self):
        self.y += self.velocidad
        if self.y > ALTO:  # Se reinicia la posición cuando el punto rojo sale de la pantalla
            self.reiniciar()

    def reiniciar(self):
        self.x = random.randint(0, ANCHO - self.radio)
        self.y = random.randint(-100, -40)

    def dibujar(self):
        pygame.draw.triangle(pantalla, AZUL, (self.x, self.y), self.radio)

# Función Principal
def main():
    # Creación de la lista de puntos rojos
    puntos_rojos = [Puntos(random.randint(0, ANCHO - 10), random.randint(-100, -40), random.randint(2, 6)) for _ in range(5)]

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        # Limpiar pantalla
        pantalla.fill(NEGRO)

        # Mover y dibujar los puntos rojos
        for punto in puntos_rojos:
            punto.mover()
            punto.dibujar()

        # Actualizar pantalla
        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()

# Iniciar el juego
if __name__ == "__main__":
    main()
