from basedatos import BaseDatos


class Mysql(BaseDatos):
    def __init__(self):
        self.connection = None

    def conectar(self):
        print("Conectando a la base de datos des mysql")
    
    def guardar(self,dato):
        self.conectar()
        print(f"Guardando en mysql {dato}")
        self.close()

    def leer(self,query):
        self.conectar()
        print(f"Leyendo en mysql con el siguiente query {query}")
        self.close()

    def close(self):
        print("Cerrando la conexión a la base de datos de mysql")