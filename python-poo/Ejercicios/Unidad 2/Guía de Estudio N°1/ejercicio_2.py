"""
Desarrollar un sistema de gestión de contactos, en el cual se debe crear dos clases, Contacto y Agenda, para gestionar los contactos de una agenda.
El objetivo es permitir al usuario realizar operaciones básicas como añadir, buscar, editar y listar contactos.
Además, el programa debe finalizar correctamente cuando el usuario lo solicite.

Clase Contacto
La clase debe tener los atributos privados de nombre, teléfono y email.

Métodos de la clase
● Constructor
● Método mágico que retorne una cadena con el nombre, teléfono y email del contacto.
● Otro método que permite modificar el nombre, teléfono o email de un contacto. Solo los datos que se proporcionen deben ser modificados.

Clase Agenda
La clase debe tener un atributo que almacene una lista pública de contactos.

Métodos de la clase
● Crear método que permita añadir un nuevo contacto a la agenda.
● Agregar método que muestre todos los contactos en la agenda.
● Un método para buscar un contacto en la agenda por nombre y lo muestra.
● Agregar un método para buscar un contacto por nombre y editar sus datos.
● Por último, crear un método que finalice el programa.

El programa debe mostrar un menú con las siguientes opciones:
● Añadir contactos
● Listar contactos
● Buscar contactos
● Editar contactos
● Cerrar agenda
"""

class Contacto:
    def __init__(self, nombre, teléfono, email):
        self.__nombre = nombre
        self.__teléfono = teléfono
        self.__email = email

    def __str__(self):
        return f"Nombre: {self.__nombre}, Teléfono: {self.__teléfono}, Email: {self.__email}"
    
    def editar_contacto(self, nombre=None, teléfono=None, email=None):
        if nombre:
            self.__nombre = nombre
        if teléfono:
            self.__teléfono = teléfono
        if email:
            self.__email = email

class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, nombre, teléfono, email):
        nuevo_contacto = Contacto(nombre, teléfono, email)
        self.contactos.append(nuevo_contacto)

    def listar_contactos(self):
        if not self.contactos:
            print(f"No se encuentra contactos en la agenda")
        else:
            for contacto in self.contactos:
                print(contacto)
    
    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto._Contacto__nombre.lower() == nombre.lower():
                return contacto
        return None
    
    def editar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            print("Se encontró un contacto:")
            print(contacto)
            nombre_nuevo = input("Nombre nuevo (dejar en blanco para no cambiar): ")
            teléfono_nuevo = input("Teléfono nuevo (dejar en blanco para no cambiar): ")
            email_nuevo = input("Email nuevo (dejar en blanco para no cambiar): ")
            contacto.editar(
                nombre = nombre_nuevo if nombre_nuevo else None,
                telefono = teléfono_nuevo if teléfono_nuevo else None,
                email = email_nuevo if email_nuevo else None
            )
            print(f"Se actualizó el contacto")
        else:
            print(f"No se encontró el contacto")

    def cerrar_agenda(self):
        print(f"Se está cerrando la agenda")

def menú():
    agenda = Agenda()

    while True:
        print("\nMenú:")
        print("1) Añadir contactos")
        print("2) Listar contactos")
        print("3) Buscar contactos")
        print("4) Editar contactos")
        print("5) Cerrar agenda")
        
        opción = input("Escoga una opción: ")

        if opción == '1':
            nombre = input("Nombre: ")
            teléfono = input("Teléfono: ")
            email = input("Email: ")
            agenda.añadir_contacto(nombre, teléfono, email)
            print("Se añadió el contacto")
        elif opción == '2':
            agenda.listar_contactos()
        elif opción == '3':
            nombre = input("Buscar un nombre: ")
            contacto = agenda.buscar_contacto(nombre)
            if contacto:
                print("Se encontró el contacto:")
                print(contacto)
            else:
                print("No se encontró el contacto")
        elif opción == '4':
            nombre = input("Editar nombre del contacto: ")
            agenda.editar_contacto(nombre)
        elif opción == '5':
            agenda.cerrar_agenda()
            break
        else:
            print("Opción inválida. Por favor, selecciona otra")

if __name__ == "__main__":
    menú()