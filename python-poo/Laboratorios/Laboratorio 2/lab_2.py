"""
La universidad ofrecerá descuentos en la cafetería para estudiantes y académicos. Los estudiantes tienen un 20% de descuento y los académicos un 10%.
Si una persona no es estudiante ni académico, no tiene descuento. El sistema debe gestionar a los clientes,
calcular el precio final de su compra después de aplicar el descuento adecuado y registrar las compras realizadas en la cafetería.

Requerimientos:
Encapsulación y Atributos Privados

1. Encapsulación de Datos del Cliente
   A. ¿Qué datos del cliente crees que deben encapsularse en una clase Cliente?
   Considera atributos como el tipo de cliente (estudiante, académico, otro) y el precio de la compra.
   ¿Cuál de estos atributos debería ser privado y cuál público? ¿Por qué?
2. Diccionario de Descuentos
   A. ¿Cómo organizarías los descuentos disponibles para cada tipo de cliente en el sistema?
   ¿Crees que un diccionario privado podría ser útil para almacenar los descuentos para cada tipo de cliente?
   ¿o se necesita otro tipo de estructura de datos?
   B. ¿Por qué sería útil encapsular la estructura de datos anterior de descuentos en lugar de exponerlo directamente?

Variables de Clase
1. Definición de Descuentos
   A. ¿Cómo definirías los descuentos para cada tipo de cliente en el sistema?
   Considera que el descuento para los estudiantes es del 20% y para los académicos del 10%.
   B. ¿Crees que estos descuentos deberían ser variables de clase o variables de instancia?
   Justifica tu respuesta en términos de reutilización y claridad del sistema.

Accesores y Mutadores
1. Métodos para Modificar el Precio de Compra
   A. ¿Cómo permitirías la modificación del precio de la compra de un cliente sin que se afecte la lógica de descuentos?
   ¿Crees que sería útil usar un setter para ajustar el precio antes de aplicar el descuento?
   B. ¿Qué tipo de acceso debería tener el descuento del cliente?
   ¿Cómo un getter podría facilitar la obtención del precio final sin exponer el cálculo interno?

Métodos Estáticos
1. Cálculo del Precio Final
   A. Imagina que deseas implementar un método que calcule el precio final después de aplicar el descuento correspondiente.
   ¿Por qué sería conveniente implementar este método como un método estático?
   B. ¿Qué ventajas tiene usar un método estático en este caso, en comparación con un método de instancia?
2. Implementación del Descuento
   A. Si decides crear un método estático ¿qué parámetros debería recibir este método y qué valor debería devolver? ¿Por qué?

Asertos e Invariantes
1. Verificación del Precio
   A. ¿Qué asertos consideras que serían útiles para asegurar que el precio de una compra no sea negativo?
   ¿Cómo evitarías que se realice una compra con un valor incorrecto?

2. Control de Descuentos y Validación del Tipo de Cliente
   A. ¿Qué invariante podrías establecer para asegurarte de que el descuento sólo se aplica si el tipo de cliente es válido (es decir, estudiante o académico)?
   B. ¿Cómo usarías asertos para verificar que el tipo de cliente ingresado esté dentro de los tipos válidos antes de aplicar el descuento?
"""
### Encapsulación y Atributos Privados ###
class Cliente:
    # 1) Deben encapsularse por dentro de una definición con los atributos tipo_cliente, estudiante, académico, funcionario y precio_compra,
    # Los atributos tipo_cliente y precio_compra deben ser privados y los atributos estudiante, académico y funcionario son públicos
    # Porque el tipo de cliente es personal y el precio de compra son personales
    def __init__(self, tipo_cliente, estudiante, académico, funcionario, precio_compra): 
        self._tipo_cliente = tipo_cliente
        self.estudiante = estudiante
        self.académico = académico
        self.funcionario = funcionario
        self._precio_compra = precio_compra

    #2) Se organizan con una definición de descuentos_disponibles
    # Los descuentos si deben ser privados dependiendo si el tipo de cliente es estudiante o académico
    def descuentos_disponibles(self):
        self._descuentos_disponibles = {}

### Variables de Clase ###
    # 1) Se definen con el nombre documentos(self):
    # Deben ser variables de clase los descuentos, porque así no debe obstruir con los demás datos y atributos
    def documentos(self):
        self.estudiante.DESCUENTO_ESTUDIANTE = 0.2 # 20%
        self.académico.DESCUENTO_ACADÉMICO = 0.1 # 10%

### Accesores y Mutadores ###
    # 1) Utilizando un setter 

### Métodos Estáticos ###
    # 1) El método estático permite que el precio final daría como resultado del precio de compra y por el descuento del tipo de cliente (estudiante o académico)
    @staticmethod

### Asertos e Invariantes ###
    # 1) Asegurar que el precio de la compra tenga un valor superior a 0 (positivo), al contrario, no serviría
    # Si se realiza una compra negativa, debe arrojar un mensaje de que el precio de la compra no debe ser negativo
    def verificación_precio(self, precio_compra):
        assert precio_compra > 0, f'El precio de la compra debe ser un valor positivo'
