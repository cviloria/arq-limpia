from flask import Flask
from controllers.user_controller import UserController
from models.mysql_user_repository import MySQLUserRepository

app = Flask(__name__)

# Configurar la base de datos (ajusta los parámetros según tu configuración)
user_repository = MySQLUserRepository(
    host="localhost",
    database="test_db",
    user="root",
    password="password"
)

user_controller = UserController(user_repository)
# para probar use el id 12 http://127.0.0.1:5000/users/12
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return user_controller.get_user(user_id)


if __name__ == "__main__":
    app.run(debug=True)