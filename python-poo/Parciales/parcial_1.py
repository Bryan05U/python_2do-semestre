"""
1. Eres el responsable de diseñar un sistema que permita gestionar un Café de Gatos, un lugar donde los clientes pueden disfrutar de
su café mientras interactúan con los gatos del lugar. Cada gato en el café tiene su propio espacio, y tú eres responsable de gestionar
tanto el bienestar de los gatos como el inventario de productos necesarios para su cuidado.
Además, debes controlar el uso de recursos como alimentos y juguetes para los gatos.

Instrucciones:

Gestión de Gatos en el Café (40 Puntos)
Los gatos son los protagonistas del café y cada uno tiene características y necesidades únicas.
Piensa en cómo representarías a los gatos dentro del sistema.
1. ¿Cómo representarías a los gatos dentro del sistema?
   a. ¿Qué atributos crees que serían importantes para describir a un gato?
   Piensa en atributos como el nombre, la edad, el nivel de energía y el nivel de hambre.
   b. ¿Cómo se encapsulan estos atributos para evitar que otras partes del programa puedan modificarlos directamente?

2. Métodos que necesita la clase Gato:
   a. ¿Cómo diseñarías un método que permita que los gatos jueguen y cómo impactaría esto en sus niveles de energía y hambre?
   b. ¿Cómo diseñarías un método que permita alimentar a los gatos y restaurar sus niveles de energía?

3. Método Mágico:
   a. Implementa un método que te permita imprimir de forma clara el estado del gato.
   ¿Qué información incluirías en la representación del gato?
"""

class Gato:
    def __init__(self, nombre, color, género, edad, energía, hambre):
        self.nombre = nombre
        self.color = color
        self.género = género
        self.edad = edad
        self.energía = energía
        self.hambre = hambre

    def gato_jugando(self, gato):
        if gato:
            print(f"El gato {self.nombre} está jugando")
        else:
            print(f"El gato {self.nombre} está descansando")

    def __str__(self):
        return f"Nombre del gato: {self.nombre}\n Edad: {self.edad}, Nivel de energía: {self.energía}, Nivel de hambre: {self.hambre}"
    
gato1 = Gato("Henry", "Marrón", "Macho", 3, 100, 0)
gato2 = Gato("Daniel", "Blanco", "Macho", 5, 100, 0)
gato3 = Gato("Lucy", "Negro", "Hembra", 4, 100, 0)

print(gato1)
print(gato2)
print(gato3)

gato2.gato_jugando(gato=1)

print(gato2)

"""
Gestión de Espacios en el Café (20 Puntos)
El café tiene diferentes áreas donde los gatos pueden estar. Imagina cómo organizarías estas áreas dentro del sistema.
1. ¿Cómo representarías las áreas dentro del café?
   a. ¿Qué atributos serían importantes para describir un área del café?
   Piensa en atributos como el nombre del área, la capacidad máxima de gatos que puede albergar, y una lista de los gatos presentes.

2. Métodos que necesita la clase Area:
   a. ¿Cómo diseñarías un método que permita agregar un gato a un área? Debes asegurarte de que no se exceda la capacidad máxima del área.
   b. ¿Cómo diseñarías un método que permita listar los gatos presentes en el área?
"""

class Área:
    def __init__(self, nombre, mesas, capacidad_gatos, gatos_presentes):
        self.nombre = nombre
        self.mesas = mesas
        self.capacidad_gatos = capacidad_gatos
        self.gatos_presentes = []

    def añadir_gatos(self, capacidad_gatos):
        if capacidad_gatos <= 6:
            print(f"Cantidad de gatos: {capacidad_gatos}")
        else:
            print(f"La cantidad de gatos sobrepasa el límite")

    def listar_gatos(self):
        self.gatos_presentes

    def __str__(self):
        return f"Espacio: {self.nombre}\n Mesas: {self.mesas}, Capacidad de gatos: {self.capacidad_gatos}, Gatos presentes: {self.gatos_presentes}"

área1 = Área("Sala 1", 7, 6, 3)
área2 = Área("Sala 2", 9, 7, 2)
área3 = Área("Sala 3", 5, 3, 1)

print(área1)
print(área2)
print(área3)

"""
Inventario del Café (20 Puntos)
El café necesita mantener un inventario de productos, como alimentos y juguetes, para el cuidado de los gatos.
Piensa en cómo podrías gestionar estos recursos dentro del sistema.
1. ¿Cómo representarías el inventario del café?
   ○ ¿Qué atributos serían importantes para describir el inventario?
   ○ ¿Cómo representarías los productos y la cantidad disponible de cada uno?

2. Métodos que necesita la clase Inventario:
   ○ ¿Cómo diseñarías un método que permita agregar productos al inventario y controlar las cantidades?
   ○ ¿Cómo diseñarías un método que permita utilizar productos del inventario,
   donde se debe asegurar de que no se usen más productos de los que están disponibles?
"""

class Inventario:
    def __init__(self, alimentos, juguetes):
        self.alimentos = alimentos
        self.juguetes = juguetes
    
    def añadir_producto(self, alimentos, juguetes):
        self.alimentos.append()
        self.juguetes.append()

"""
Estado de los Gatos e Interacción entre Clases (20 Puntos)
Cada gato tiene diferentes estados (hambriento, con energía, cansado).
Piensa en cómo representar estos estados dentro del sistema y cómo cambiarían dependiendo de sus acciones
(jugar, comer, descansar).
1. ¿Cómo podrías usar un método mágico para imprimir el estado de un gato?
   a. ¿Qué información incluirías en la representación del gato?
   Piensa en el nombre, la edad, el nivel de energía y el nivel de hambre.
   b. ¿Cómo actualizarías estos valores a medida que el gato interactúa con el entorno (juega, come, etc)?

2. Métodos de interacción entre las clases:
   a. ¿Cómo permitirías que los gatos interactúen con el inventario, como por ejemplo consumir alimentos o juguetes?
   b. ¿Cómo gestionarías la adición de gatos a las áreas, asegurándote de que el sistema se mantenga organizado?
"""

