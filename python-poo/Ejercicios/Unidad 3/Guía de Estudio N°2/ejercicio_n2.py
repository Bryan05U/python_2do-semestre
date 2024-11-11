"""
Un gimnasio necesita gestionar las suscripciones de sus clientes y aplicar descuentos según el tipo de suscripción.
También necesitan controlar el acceso a las clases en función de la cantidad de suscripciones activas.

1) Encapsulación y Variables de Instancia
¿Qué datos deberían encapsularse en la clase principal? Considera atributos como nombre del cliente, tipo de suscripción (mensual, trimestral, anual), y costo.
¿Cuál debería ser privado y cuál público? ¿Por qué?

2) Variables de Clase
Si el gimnasio decide ofrecer un descuento especial para suscripciones anuales, ¿cómo implementarías esta lógica?
¿Este descuento debería ser una variable de clase o de instancia? ¿Por qué?

3) Accesores y Mutadores
¿Cómo utilizarías setters y getters para modificar el costo de la suscripción, considerando que solo algunos tipos de suscripciones pueden tener descuentos?

4) Métodos Estáticos
En el supuesto, que deseas calcular el costo final de una suscripción aplicando un descuento de bienvenida a nuevos clientes.
¿Cómo podrías implementar esta función como un método estático? ¿Qué ventajas tendría?

5) Asertos e Invariantes
¿Qué asertos serían útiles para asegurar que el costo de la suscripción no sea negativo?
¿Qué invariante podrías establecer para evitar tipos de suscripción inválidos?

6) Especificación e Interfaz de Clase
¿Qué métodos debería exponer la clase principal para permitir la creación de suscripciones, la consulta de costo y la aplicación de descuentos?
¿Cómo puedes estructurar estos métodos en la interfaz de la clase?
"""

class Suscripcion:
    descuento_anual = 0.15  # 15% de descuento para suscripciones anuales.

class Suscripcion:
    def __init__(self, nombre_cliente, tipo_suscripcion, costo_base):
        self.nombre_cliente = nombre_cliente
        self.tipo_suscripcion = tipo_suscripcion
        self._costo_base = costo_base
        self._costo_final = costo_base

    def setCosto(self, nuevo_costo):
        # Validar tipo de suscripción y aplicar descuento
        if self.tipo_suscripcion == 'anual':
            self._costo_final = nuevo_costo * (1 - Suscripcion.descuento_anual)
        else:
            self._costo_final = nuevo_costo

    def getCosto(self):
        return self._costo_final

class Suscripcion:
    descuento_bienvenida = 0.10  # 10% de descuento para nuevos clientes

    @staticmethod
    def calcularCostoConDescuentoBienvenida(costo_base):
        return costo_base * (1 - Suscripcion.descuento_bienvenida)

costo_con_descuento = Suscripcion.calcularCostoConDescuentoBienvenida(100)
print(costo_con_descuento)  # 90.0

def setCosto(self, nuevo_costo):
    assert nuevo_costo >= 0, "El costo no puede ser negativo"
    self._costo_base = nuevo_costo
    # Aquí va la lógica para aplicar descuentos si es necesario

class Suscripcion:
    descuento_anual = 0.15  # Descuento anual global.

    def __init__(self, nombre_cliente, tipo_suscripcion, costo_base):
        assert tipo_suscripcion in ['mensual', 'trimestral', 'anual'], "Tipo de suscripción inválido"
        self.nombre_cliente = nombre_cliente
        self.tipo_suscripcion = tipo_suscripcion
        self._costo_base = costo_base
        self._costo_final = costo_base

    def setCosto(self, nuevo_costo):
        assert nuevo_costo >= 0, "El costo no puede ser negativo"
        if self.tipo_suscripcion == 'anual':
            self._costo_final = nuevo_costo * (1 - Suscripcion.descuento_anual)
        else:
            self._costo_final = nuevo_costo

    def getCosto(self):
        return self._costo_final

    @staticmethod
    def calcularCostoConDescuentoBienvenida(costo_base):
        return costo_base * (1 - Suscripcion.descuento_bienvenida)

    def aplicarDescuento(self):
        if self.tipo_suscripcion == 'anual':
            self._costo_final *= (1 - Suscripcion.descuento_anual)
