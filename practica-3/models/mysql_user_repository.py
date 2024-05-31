
from models.user import User

class MySQLUserRepository:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def get_user(self, user_id):
        # mock a la base de datos MySQL
        connection = {
            "host": self.host,
            "user": self.user,
            "password": self.password,
            "database": self.database
        }

        # Ejecutar la consulta para obtener los datos del usuario
        query = "SELECT * FROM users WHERE id = %s"

        
        # Si se encontró el usuario, devolver un objeto User con los datos
        if user_id == 12:
            user = User('Usuario desde la BD', 'a@a.com',"secret")
            return user

        # Si no se encontró el usuario, devolver None
        return None
