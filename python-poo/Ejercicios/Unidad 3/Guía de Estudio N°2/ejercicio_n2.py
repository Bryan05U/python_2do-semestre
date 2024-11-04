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