"""
Imagina que estás diseñando un sistema para gestionar cuentas bancarias.
Para ello, crea una clase llamada CuentaBancaria que modele el comportamiento básico de una cuenta de banco.
El sistema debe permitir realizar operaciones como depósitos, retiros y consultar el saldo actual.
Además, se debe utilizar el concepto de encapsulamiento para proteger la información sensible de la cuenta.
Asegúrate de encapsular adecuadamente los atributos que consideres sensibles.
Define métodos para interactuar con estos atributos de manera controlada.

Consideraciones de Encapsulamiento
● ¿Qué atributos deberían ser privados y por qué?
● ¿Qué métodos utilizarías para acceder o modificar estos atributos de manera controlada?
Por ejemplo, permitiendo consultar el saldo pero no modificarlo directamente.
"""

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial