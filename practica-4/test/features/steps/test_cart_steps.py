import pytest
from pytest_bdd import scenarios, given, when, then
from core.domain.models import Product, Cart

# Define the location of the feature file
scenarios('../cart.feature')

@pytest.fixture
def cart():
    return Cart()

@given('a shopping cart with no products')
def empty_cart(cart):
    cart.items = []

@when('I add a product with price 200.0')
def add_expensive_product_to_cart(cart):
    product = Product(1, 'Product 1', 200.0)
    cart.add_product(product, 1)

@then('the cart the total should be 180.0')
def verify_cart_total(cart):
    assert cart.calculate_total() == 180.0

## Price 150
@given('a shopping cart with no products')
def empty_cart(cart):
    cart.items = []

@when('I add a product with price 150.0')
def add_expensive_product_to_cart(cart):
    product = Product(1, 'Product 1', 150.0)
    cart.add_product(product, 1)

@then('the cart the total should be 135.0')
def verify_cart_total(cart):
    assert cart.calculate_total() == 135.0
