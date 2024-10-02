"""
1. Implementar un sistema básico para gestionar personajes de un videojuego utilizando programación orientada a objetos.
Cada personaje tendrá un nombre, nivel de vida y puntos de ataque. La idea es que los personajes puedan interactuar entre ellos, permitiendo
que un personaje ataque a otro, lo que disminuirá su vida. Además, deberás verificar si un personaje está vivo o no.
Requerimientos:
1. Clase Personaje:
○ Atributos: el nombre del personaje, el nivel de vida del personaje y los puntos de ataque del personaje.
○ Métodos: un método que permita que el personaje ataque a otro, disminuyendo la vida del otro personaje según los puntos de ataque del atacante.
Un segundo método, que verifique si el personaje sigue vivo. Debe devolver True si el nivel de vida es mayor a 0, y False si no. Por último
implementar un método mágico que permita devolver un string que muestre el estado del personaje (nombre, vida, y ataque).
Instrucciones:
1. Implementar la clase Personaje con los atributos y métodos descritos anteriormente.
2. Crear al menos dos personajes. Cada personaje debe tener un nombre, vida inicial y puntos de ataque.
3. Simula un combate entre los personajes haciendo que uno ataque al otro. Después de cada ataque, se debe mostrar el estado de ambos personajes.
4. Repetir los ataques hasta que uno de los personajes quede sin vida. Utiliza un método para verificar si el personaje sigue en pie.
"""

# Creando la clase Personaje
class Personaje:
    def __init__(self, nombre, nivel_vida, puntos_ataque):
        self.nombre = nombre
        self.nivel_vida = nivel_vida
        self.puntos_ataque = puntos_ataque

    def verificar(self):
        if self.nivel_vida > 0:
            True
        else:
            False

personaje_1 = Personaje('Player 1', 100, 10)
personaje_2 = Personaje('Player 2', 100, 7)