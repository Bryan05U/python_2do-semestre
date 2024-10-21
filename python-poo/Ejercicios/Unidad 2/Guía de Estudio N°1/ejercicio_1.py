"""
Implementar un programa que gestione la información de un grupo de estudiantes. Cada estudiante tendrá un nombre y un promedio de notas.
Además, el sistema debe determinar si el estudiante ha aprobado o no, y permitir la actualización de sus notas de forma controlada.
Instrucciones:
1) Implementar la clase Estudiante con los atributos privados (nombre y promedio) y atributo público (estado)
que debe indicar si el estudiante ha aprobado o no (Booleano)
2) El programa debe permitir la creación de al menos tres estudiantes con su respectivo nombre y promedio.
3) Imprimir el estado de cada estudiante utilizando un método mágico para mostrar su nombre y promedio.
4) Simular una actualización de notas utilizando un método para ello.
5) Evaluar si los estudiantes han aprobado llamando a un método para evaluar el estado del estudiante,
y que muestre un mensaje con su estado de aprobación.
"""

class Estudiante:
    def __init__(self, nombre, promedio):
        self.__nombre = nombre
        self.__promedio = promedio
        self.estado = self.evaluar_estado()

    def __str__(self):
        return f"Nombre: {self.__nombre}, Promedio: {self.__promedio}, Aprobado: {self.estado}"
    
    def actualizar_notas(self, promedio_nuevo):
        if 0 <= promedio_nuevo <= 50:
            self.__promedio = promedio_nuevo
            self.estado = self.evaluar_estado()
        else:
            print(f"El promedio debería estar entre el 0 y el 50")

    def evaluar_estado(self):
        return self.__promedio >= 28
    
primer_estudiante = Estudiante("Felipe", 34)
segundo_estudiante = Estudiante("Eva", 48)
tercer_estudiante = Estudiante("Miguel", 27)

print(primer_estudiante)
print(segundo_estudiante)
print(tercer_estudiante)

print("\nActualización de notas")
tercer_estudiante.actualizar_notas(30)

print(tercer_estudiante)