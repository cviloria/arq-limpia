import pytest
from core.domain.models import Product, Cart


def test_add_product_with_negative_price():
    cart = Cart()
    with pytest.raises(ValueError, match="Price cannot be negative"):
        product = Product(1, 'Product 1', -10.0)
        cart.add_product(product)

def test_add_product():
    cart = Cart()
    product = Product(1, 'Product 1', 10.0)
    cart.add_product(product, 2)
    assert len(cart.items) == 1
    assert cart.items[0].quantity == 2
    assert cart.items[0].product.name == 'Product 1'

def test_remove_product():
    cart = Cart()
    product1 = Product(1, 'Product 1', 10.0)
    product2 = Product(2, 'Product 2', 20.0)
    cart.add_product(product1, 2)
    cart.add_product(product2, 1)
    cart.remove_product(1)
    assert len(cart.items) == 1
    assert cart.items[0].product.product_id == 2

def test_quantity_product_increse():
    cart = Cart()
    product1 = Product(1, 'Product 1', 10.0)
    cart.add_product(product1, 2)
    cart.add_product(product1, 1)
    assert len(cart.items) == 1
    assert cart.items[0].product.product_id == 1
    assert cart.items[0].quantity == 3

if __name__ == '__main__':
    pytest.main()