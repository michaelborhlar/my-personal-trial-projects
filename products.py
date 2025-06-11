class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_stock_value(self):
        stock_value = self.price * self.quantity
        return f"THE TOTAL STOCK VALUE FOR {self.name} is: {stock_value}"
    
my_product_name = str(input("Enter your product name: "))
my_product_price = int(input("Enter your product price "))
my_product_quantity = int(input("Enter the total quantity of your product: "))
my_product = product(my_product_name, my_product_price, my_product_quantity)
print(my_product.total_stock_value())
            