from flask import Flask
from interfaces.api.cart_controller import cart_bp

app = Flask(__name__)

# Registrar el blueprint
app.register_blueprint(cart_bp)

if __name__ == "__main__":
    app.run(debug=True)