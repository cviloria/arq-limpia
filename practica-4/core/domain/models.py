class Product:
    def __init__(self, product_id, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.product_id = product_id
        self.name = name
        self.price = price

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        if product.price > 100:
            product.price *= 0.9  # Apply 10% discount
        for item in self.items:
            if item.product.product_id == product.product_id:
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))

    def remove_product(self, product_id):
        self.items = [item for item in self.items if item.product.product_id != product_id]

    def calculate_total(self):
        return sum(item.product.price * item.quantity for item in self.items)