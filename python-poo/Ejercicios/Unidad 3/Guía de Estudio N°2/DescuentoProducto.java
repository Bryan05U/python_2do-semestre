/*
Escribir un programa que calcule el precio final de un producto después de
aplicar un descuento.ine métodos para interactuar con estos atributos de
manera controlada.

Considera declarar las variables necesarias para almacenar el precio original del
producto y el porcentaje de descuento. Se debe mostrar el monto de descuento y el precio
final después del descuento. Por último, mostrar un mensaje indicando si el descuento fue
mayor o menor al 20% del precio original.
 */
package descuentoproducto;

import java.util.Scanner;

public class DescuentoProducto {
    private double precioOriginal;
    private double porcentajeDescuento;
    
    // Se utiliza un constructor
    public DescuentoProducto(double precioOriginal, double porcentajeDescuento) {
        this.precioOriginal = precioOriginal;
        this.porcentajeDescuento = porcentajeDescuento;
    }

    // Método para el calculo del monto de descuento
    public double calcularMontoDescuento() {
        return precioOriginal * (porcentajeDescuento / 100);
    }

    // Método para el calculo del precio final después del descuento
    public double calcularPrecioFinal() {
        return precioOriginal - calcularMontoDescuento();
    }

    // Método para determinar si el descuento es mayor o menor al 20%
    public String determinarDescuento() {
        if (porcentajeDescuento > 20) {
            return "El descuento es mayor al 20% del precio original.";
        } else {
            return "El descuento es menor o igual al 20% del precio original.";
        }
    }    

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // Se solicita el precio original y el porcentaje de descuento
        System.out.print("Ingrese el precio original del producto: ");
        double precioOriginal = scanner.nextDouble();
        System.out.print("Ingrese el porcentaje de descuento: ");
        double porcentajeDescuento = scanner.nextDouble();

        // Creación del objeto DescuentoProducto
        DescuentoProducto producto = new DescuentoProducto(precioOriginal, porcentajeDescuento);

        // Calcular y mostrar los resultados
        double montoDescuento = producto.calcularMontoDescuento();
        double precioFinal = producto.calcularPrecioFinal();
        String mensajeDescuento = producto.determinarDescuento();

        System.out.printf("Monto de descuento: %.2f%n", montoDescuento);
        System.out.printf("Precio final después del descuento: %.2f%n", precioFinal);
        System.out.println(mensajeDescuento);
    }
    
}
