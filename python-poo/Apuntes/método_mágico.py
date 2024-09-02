# 2 de septiembre de 2024

# Suma __add__ + Define el comportamiento del operador + cuando se usa con objetos de la clase
# Resta __sub__ - Define el comportamiento del operador - cuando se usa con objetos de la clase.
# Producto __mul__ * Define el comportamiento del operador * cuando se usa con objetos de la clase.
# División __truediv__ / Define el comportamiento del operador / cuando se usa con objetos de la clase.
# Igualdad __eq__ == Define el comportamiento del operador == para comparar si dos objetos son iguales.
# Desigualdad __ne__ != Define el comportamiento del operador != para comparar si dos objetos son diferentes.
# Mayor que __gt__ > Define el comportamiento del operador > para comparar si un objeto es mayor que otro.
# Menor que __lt__ < Define el comportamiento del operador < para comparar si un objeto es menor que otro.
# Mayor o igual __ge__ >= Define el comportamiento del operador >= para comparar si un objeto es mayor o igual que otro.
# Menor o igual __le__ <= Define el comportamiento del operador <= para comparar si un objeto es menor o igual que otro.
# Inicialización __init__ Método constructor, se llama al crear una nueva instancia de la clase.
# Representación __str__ Devuelve una representación en cadena del objeto, llamada por print() y str().
# Representación formal __repr__ Devuelve una representación oficial del objeto, usada para debug y por repr().


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

class Triángulo:
    # Constructor de Clase
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    # Método mágico que devuelve una representación en cadena del triángulo
    def __str__(self):
        return f"El triángulo tiene los siguientes lados: {self.l1} cm, {self.l2} cm, {self.l3} cm"
    
    # Este método mágico compara si dos triángulos son iguales o no
    def __eq__(self, triangle):
        return {self.l1, self.l2, self.l3} == {triangle.l1, triangle.l2, triangle.l3}

    # Método mágico que permite sumar dos triángulos
    def __add__(self, triangle):
        return Triángulo(
           self.l1 + triangle.l1,
           self.l2 + triangle.l2,
           self.l3 + triangle.l3
        )
    # Método mágico que devuelve el perímetro del triángulo
    def __len__ (self):
        return int(self.l1 + self.l2 + self.l3)
    
    # Verificar si los lados ingresados forman un triángulo válido
    def es_válido(self):
        return (self.l1 + self.l2 > self.l3 and self.l1 + self.l3 > self.l2 and self.l2 + self.l3 > self.l1)

# Se crean 2 instancias de la clase Triangulo
triangulo1 = Triángulo(3, 4, 5)
triangulo2 = Triángulo(11, 12, 13)

# Se llama el método __str__ para representar el triángulo como una cadena
print(triangulo1) 

# Se usa el método __eq__ para comparar si dos triángulos son iguales
print(triangulo1 == triangulo2)

# Nuevo triángulo sumando dos triángulos
triangulo3 = triangulo1 + triangulo2
print(triangulo3) 

# Método __len__ para obtener el perímetro del triángulo
print(len(triangulo1)) 

# Verifica si los lados forman un triángulo válido
print(triangulo1.es_válido())