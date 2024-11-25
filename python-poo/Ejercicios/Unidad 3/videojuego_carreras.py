# 22 de noviembre de 2024

"""
Diseñar un sistema para un videojuego de carreras donde los vehículos tienen características y comportamientos compartidos,
pero también pueden combinar atributos de diferentes tipos (como "Terrestres", "Acuáticos" o "Aéreos").
Utilizar herencia múltiple para crear vehículos híbridos y polimorfismo para manejar diferentes tipos de vehículos de manera uniforme.
"""

# Creando una base Vehículo
class Vehículo:
    def __init__(self, nombre, velocidad_máxima):
        self.nombre = nombre
        self.velocidad_máxima = velocidad_máxima

    def movimiento(self):
        raise NotImplementedError("El método 'mover' no puede ser implementado si no tiene las clases derivadas")

    def obtener_tipo(self):
        return "Vehículo normal"



### Clases especializadas ###
# Clase Terrestre
class Terrestre(Vehículo):
    def __init__(self, nombre, velocidad_máxima, tracción):
        super().__init__(nombre, velocidad_máxima)
        self.tracción = tracción

    def movimiento(self):
        print(f"{self.nombre} se mueve sobre la tierra a {self.velocidad_máxima} km/h")

    def obtener_tipo(self):
        return "Terrestre"

# Clase Acuático
class Acuático(Vehículo):
    def __init__(self, nombre, velocidad_máxima, tipo_tractor):
        super().__init__(nombre, velocidad_máxima)
        self.tipo_tractor = tipo_tractor

    def movimiento(self):
        print(f"{self.nombre} navega sobre el agua a {self.velocidad_máxima} km/h")

    def obtener_tipo(self):
        return "Acuático"

# Clase Aéreo
class Aéreo(Vehículo):
    def __init__(self, nombre, velocidad_máxima, tipo_motor):
        super().__init__(nombre, velocidad_máxima)
        self.tipo_motor = tipo_motor

    def movimiento(self):
        print(f"{self.nombre} vuela por el aire a {self.velocidad_máxima} km/h")

    def obtener_tipo(self):
        return "Aéreo"



### Vehículos Híbridos ###
# Clase Terrestre-Acuático
class TerrestreAcuático(Terrestre, Acuático):
    def __init__(self, nombre, velocidad_máxima, tracción, tipo_tractor):
        Terrestre.__init__(self, nombre, velocidad_máxima, tracción)
        Acuático.__init__(self, nombre, velocidad_máxima, tipo_tractor)
    
    def movimiento(self):
        print(f"{self.nombre} se desplaza sobre tierra o agua a {self.velocidad_máxima} km/h")
    
    def obtener_tipo(self):
        return "Terrestre-Acuático"

# Clase Acuático-Aéreo
class AcuáticoAéreo(Acuático, Aéreo):
    def __init__(self, nombre, velocidad_máxima, tipo_tractor, tipo_motor):
        Acuático.__init__(self, nombre, velocidad_máxima, tipo_tractor)
        Aéreo.__init__(self, nombre, velocidad_máxima, tipo_motor)

    def movimiento(self):
        print(f"{self.nombre} puede navegar en el agua o volar a {self.velocidad_máxima} km/h")
    
    def obtener_tipo(self):
        return "Acuático-Aéreo"

# Clase Terrestre-Aéreo
class TerrestreAéreo(Terrestre, Aéreo):
    def __init__(self, nombre, velocidad_máxima, tracción, tipo_motor):
        Terrestre.__init__(self, nombre, velocidad_máxima, tracción)
        Aéreo.__init__(self, nombre, velocidad_máxima, tipo_motor)
    
    def movimiento(self):
        print(f"{self.nombre} puede andar en tierra o volar a {self.velocidad_máxima} km/h")
    
    def obtener_tipo(self):
        return "Terrestre-Aéreo"
    


### Uso del Polimorfismo ###
def iniciar_carrera(vehículos):
    for vehículo in vehículos:
        print(f"Vehículo: {vehículo.nombre} ({vehículo.obtener_tipo()})")
        vehículo.movimiento()



# Creación de Vehículos
terrestre = Terrestre('Todoterreno', 120, '4 x 4')
acuático = Acuático('Lancha', 100, 'Hélice')
aéreo = Aéreo('Avión caza', 300, 'Turbina')
terrestre_acuático = TerrestreAcuático('Anfibio', 80, '8 x 8', 'Hélice')
acuático_aéreo = AcuáticoAéreo('Hidroavión', 230, 'Hélice', 'Turbojet')
terrestre_aéreo = TerrestreAéreo('Auto volador', 110, '4 x 4', 'Turbina')

# Lista de Vehículos
vehículos = [terrestre, acuático, aéreo, terrestre_acuático, acuático_aéreo, terrestre_aéreo]

# Iniciar la carrera
iniciar_carrera(vehículos)