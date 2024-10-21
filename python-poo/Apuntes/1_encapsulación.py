class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, soy {self.nombre} tengo {self.edad} años"
    
class Test:
    #def __uno(self):
        #print("Este método es privado, ya que su nombre empieza por __")

    def dos(self):
        print("Este método es público")

    def __tres__(self):
        print("Este método también es público, porque su nombre empieza y acaba por __")

p = Test()
#p.__uno() # No funciona, ya que es un método privado
p.dos() # Funciona, ya que el método dos es público
p.__tres__() # También funciona