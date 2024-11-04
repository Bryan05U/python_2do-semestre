/*
Crear un programa que determine el precio de la entrada a un parque de
diversiones en función de la edad de la persona. Clasificar a la persona en una de
las siguientes categorías:
● Niños (menores de 12 años): $2000
● Adolescentes (entre 12 y 17 años): $3500
● Adultos (mayores de 17 años): $5000
Establecer las condiciones y mostrar el precio correspondiente a la categoría en la que
pertenece la persona.
 */
package parquediversiones;

import java.util.Scanner;

public class ParqueDiversiones {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Ingrese su edad:");
        int edad = scanner.nextInt();
        int precio;
        
        if (edad < 12) {
            precio = 2000;
            System.out.println("Categoría: Niños");
        } else if (edad >= 12 && edad <= 17) {
            precio = 3500;
            System.out.println("Categoría: Adolescentes");
        } else {
            precio = 5000;
            System.out.println("Categoría: Adultos");
        }
        
        System.out.println("El precio de la entrada es: $" + precio);
        
        scanner.close();
    }
}
