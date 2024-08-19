class Persona():
    # Atributos de Clase (Características compartidas por todos los objetos de la clase)
    nombre = "Bryan"
    apellido = "Apellido"
    edad = 18

    # Métodos (Comportamientos)
    def hablar(self):
        print(f"{self.nombre} está hablando sobre política")

    def caminar(self):
        print(f"{self.nombre} está caminando por las calles")

    def comer(self):
        print(f"{self.nombre} está comiendo pizza")

# Creación de un objeto de la clase Persona
persona1 = Persona()

# Acceso a los atributos y métodos del objeto
print(f"Nombre: {persona1.nombre}")
print(f"Apellido: {persona1.apellido}")
print(f"Edad: {persona1.edad} años")

# Llamando a los métodos de la Clase
persona1.hablar()
persona1.caminar()
persona1.comer()