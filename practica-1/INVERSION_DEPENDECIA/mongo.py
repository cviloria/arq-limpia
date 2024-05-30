from basedatos import BaseDatos


class Mongo(BaseDatos):
    def __init__(self):
        self.connection = None

    def conectar(self):
        print("Conectando a la base de datos desde mongo")
    
    def guardar(self,dato):
        self.conectar()
        print(f"Guardando en mongo {dato}")

    def leer(self,query):
        self.conectar()
        print(f"Leyendo en mongo con el siguiente query {query}")
        self.close()

    def close(self):
        print("Cerrando la conexión a la base de datos de mongo")