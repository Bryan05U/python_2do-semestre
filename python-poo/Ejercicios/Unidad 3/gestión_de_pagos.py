"""
Contexto
Una empresa está desarrollando un sistema de gestión de pagos para su plataforma de comercio electrónico.
La plataforma admite diferentes métodos de pago, como tarjetas de crédito, transferencias bancarias y pagos en efectivo.
Cada método de pago tiene un comportamiento diferente. Por ejemplo:

1. Las tarjetas de crédito necesitan ser validadas antes de proceso_de el pago.
Las transferencias bancarias requieren un código de confirmación antes de
completar la transacción.

2. Los pagos en efectivo no necesitan validación ni confirmación, solo deben registrar
el monto recibido.

3. Actualmente, la clase base MétodoDePago() incluye un método proceso_de_pago() que
asume que todos los métodos de pago deben validación_dese antes de proceso_dese. Sin
embargo, este diseño está causando problemas, ya que los pagos en efectivo no
necesitan validación, y algunos métodos de pago están lanzando excepciones
inesperadas.

Problema a Resolver
El sistema actual viola el Principio de Sustitución de Liskov (LSP)
porque no todos los métodos de pago respetan el comportamiento esperado de la clase base.
Tu tarea es rediseñar la jerarquía de clases para que los métodos de pago cumplan con el LSP,
asegurando que las subclases puedan ser utilizadas de forma intercambiable sin romper el programa.
"""
from abc import ABC, abstractmethod

# Clase Método de Pago
class MétodoDePago(ABC):
    @abstractmethod
    def proceso_de_pago(self, monto):
        pass

# Clase Pago con Tarjeta de Crédito
class PagoConTarjetaCrédito(MétodoDePago):
    def __init__(self, número_tarjeta, fecha_expiración, cvv):
        self.número_tarjeta = número_tarjeta
        self.fecha_expiración = fecha_expiración
        self.cvv = cvv

    def validación_de_tarjeta(self):
        # Aquí iría la lógica de validación de la tarjeta
        print("Validando tarjeta de crédito...")

    def proceso_de_pago(self, monto):
        self.validación_de_tarjeta()
        print(f"Procesando el pago de ${monto} con tarjeta de crédito.")

# Clase Pago con Transferencia Bancaria
class PagoConTransferenciaBancaria(MétodoDePago):
    def __init__(self, cuenta_bancaria, banco):
        self.cuenta_bancaria = cuenta_bancaria
        self.banco = banco

    def validación_de_transferencia(self):
        # Aquí iría la lógica de validación de la transferencia
        print("Validando transferencia bancaria...")

    def obtener_codigo_confirmacion(self):
        # Lógica para obtener el código de confirmación
        print("Obteniendo código de confirmación de transferencia...")

    def proceso_de_pago(self, monto):
        self.validación_de_transferencia()
        self.obtener_codigo_confirmacion()
        print(f"Procesando el pago de ${monto} con transferencia bancaria.")

# Clase Pago en Efectivo
class PagoEnEfectivo(MétodoDePago):
    def __init__(self, monto_recibido):
        self.monto_recibido = monto_recibido

    def proceso_de_pago(self, monto):
        print(f"Registrando el pago en efectivo de ${monto}. Validación es innecesario.")

# Función para proceso_de pagos sin preocuparse por el tipo específico de método de pago
def proceso_de_pago_genérico(Método_pago, monto):
    Método_pago.proceso_de_pago(monto)

# Creación de instancias de distintos métodos de pago
tarjeta = PagoConTarjetaCrédito("1234567890123456", "12/25", "123")
transferencia = PagoConTransferenciaBancaria("ES1234567890123456789012", "Banco XYZ")
efectivo = PagoEnEfectivo(100)

# Procesar pagos con diferentes métodos
proceso_de_pago_genérico(tarjeta, 100)
proceso_de_pago_genérico(transferencia, 250)
proceso_de_pago_genérico(efectivo, 25)
