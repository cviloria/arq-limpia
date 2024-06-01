from flask import Blueprint, request, jsonify
from core.domain.models import Product, Cart
from core.use_cases.cart_use_cases import CartUseCase

cart_bp = Blueprint('cart_bp', __name__)

# Inicializar el carrito y el caso de uso
cart = Cart()
cart_use_case = CartUseCase(cart)

@cart_bp.route('/cart', methods=['POST'])
def add_product():
    data = request.get_json()
    product = Product(data['product_id'], data['name'], data['price'])
    quantity = data.get('quantity', 1)
    cart_use_case.add_product_to_cart(product, quantity)
    return jsonify({"message": "Product added to cart"}), 201

@cart_bp.route('/cart/<int:product_id>', methods=['DELETE'])
def remove_product(product_id):
    cart_use_case.remove_product_from_cart(product_id)
    return jsonify({"message": "Product removed from cart"}), 200

@cart_bp.route('/cart/total', methods=['GET'])
def get_total():
    total = cart_use_case.get_cart_total()
    return jsonify({"total": total}), 200