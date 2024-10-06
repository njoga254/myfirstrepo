class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def stock_value(self):
        value = self.price * self.quantity
        return f"{self.name} which goes for ksh{self.price} per piece is worth {value} in stock."
    
#instances
product_catalog = Product ("Nivea body lotion", 250, 50)
print(product_catalog.stock_value())
