/*
Crear un programa en Java que determine el precio de entrada a un museo en función de la edad de la persona.
El programa debe clasificar a la persona en una de las siguientes categorías:
● Niños (menores de 5 años): Entrada gratuita.
● Niños Mayores (entre 5 y 12 años): $1500.
● Jóvenes (entre 13 y 17 años): $3000.
● Adultos (entre 18 y 64 años): $5000.
● Adultos Mayores (65 años o más): $2000.
 */
package museo;
import java.util.Scanner;

public class Museo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Ingrese su edad:");
        int edad = scanner.nextInt();
        int precio;
        
        if (edad < 5) {
            precio = 0; // Entrada gratis
            System.out.println("Categoría: Niños");
        } else if (edad >= 5 && edad <= 12) {
            precio = 1500;
            System.out.println("Categoría: Niños Mayores");
        } else if (edad >= 13 && edad <= 17) {
            precio = 3000;
            System.out.println("Categoría: Jóvenes");
        } else if (edad >= 18 && edad <= 64) {
            precio = 5000;
            System.out.println("Categoría: Adultos");
        } else {
            precio = 2000;
            System.out.println("Categoría: Adultos Mayores");
        }
        
        System.out.println("El precio de la entrada al museo es de: $" + precio);
        
        scanner.close();
    }
}