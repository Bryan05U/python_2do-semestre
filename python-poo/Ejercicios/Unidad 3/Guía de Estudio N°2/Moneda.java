/*
Desarrollar un programa que convierta una cantidad de dinero en pesos chilenos
a otra moneda (dólares, euros, yenes, yuanes, libras esterlinas) utilizando un
valor predeterminado para el tipo de cambio.
Utilizar una estructura de control para elegir la moneda de destino según el valor de opción:
○ 1: Dólares (tipo de cambio = 0.0011)
○ 2: Euros (tipo de cambio = 0.00095)
○ 3: Yenes (tipo de cambio = 0.15)
○ 4: Libras Esterlinas (tipo de cambio = 0.00084)
○ 5: Yuanes (tipo de cambio = 0.0073)
Calcular el monto convertido y mostrar el resultado. Si la opción no es válida, se debe
mostrar un mensaje de error.
*/
package moneda;

import java.util.Scanner;

public class Moneda {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Tipo de  moneda
        final double TIPO_DOLARES = 0.0011;
        final double TIPO_EUROS = 0.00095;
        final double TIPO_YENES = 0.15;
        final double TIPO_LIBRAS_ESTERLINAS = 0.00084;
        final double TIPO_YUANES = 0.0073;
        
        System.out.println("Ingrese la cantidad de pesos chilenos a convertir: ");
        double pesosChilenos = scanner.nextDouble();
        
        System.out.println("Escoga un tipo de moneda de destino");
        System.out.println("1) Dolares");
        System.out.println("2) Euros");
        System.out.println("3) Yenes");
        System.out.println("4) Libras Esterlinas");
        System.out.println("5) Yuanes");
        System.out.print("Opción:");
        int opcion = scanner.nextInt();
        
        double montoConvertido = 0;
        
        switch (opcion) {
            case 1:
                montoConvertido = pesosChilenos * TIPO_DOLARES;
                System.out.printf("El monto de pesos chilenos a Dólares es de: %.2f\n", montoConvertido);
                break;
            case 2:
                montoConvertido = pesosChilenos * TIPO_EUROS;
                System.out.printf("El monto de pesos chilenos a Euros es de: %.2f\n", montoConvertido);
                break;
            case 3:
                montoConvertido = pesosChilenos * TIPO_YENES;
                System.out.printf("El monto de pesos chilenos a Yenes es de: %.2f\n", montoConvertido);
                break;
            case 4:
                montoConvertido = pesosChilenos * TIPO_LIBRAS_ESTERLINAS;
                System.out.printf("El monto de pesos chilenos a Libras Esterlinas es de: %.2f\n", montoConvertido);
                break;
            case 5:
                montoConvertido = pesosChilenos * TIPO_YUANES;
                System.out.printf("El monto de pesos chilenos a Yuanes es de: %.2f\n", montoConvertido);
                break;
            default:
                System.out.printf("La opción que ingresaste es inválida. Por favor, escoga una opción entre 1 y 5.");
                break;
        }
        scanner.close();       
    }
}
