# 06 de diciembre de 2024

class Pato:
    def graznar(self):
        print("¡Cuack!")
    
class Persona:
    def graznar(self):
        print("¡Estoy imitando a un pato!")

def graznido(ser):
    ser.graznar()

pato = Pato()
persona = Persona()

graznido(pato)
graznido(persona)