from basedatos import BaseDatos
import mysql.connector

class Mysql(BaseDatos):
    def __init__(self):
        self.connection = None

    def conectar(self):
        self.connection = mysql.connect()
    
    def guardar(self,dato):
        self.connection = mysql.connect()

    def leer(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def close(self):
        self.connection.close()