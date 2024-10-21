class Producto:
    def __init__(self, name, price, stock):
        # Atributos privados
        self.__name = name
        self.__price = price
        self.__stock = stock
    
    def get_name(self):
        return self.__name

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("El precio debe ser mayor que 0")
        
    def get_price(self):
        return self.__price
    
    def get_stock(self):
        return self.__stock
    
    def set_stock(self, cantidad):
        if cantidad >= 0:
            self.__stock = cantidad
        else:
            print("La cantidad de stock no debe ser negativa")