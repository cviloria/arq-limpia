from core.domain.models import Cart, Product

class CartUseCase:
    def __init__(self, cart: Cart):
        self.cart = cart

    def add_product_to_cart(self, product: Product, quantity=1):
        self.cart.add_product(product, quantity)

    def remove_product_from_cart(self, product_id):
        self.cart.remove_product(product_id)

    def get_cart_total(self):
        return self.cart.calculate_total()