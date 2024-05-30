from mysql import Mysql
from mongo import Mongo
from manejadorbasedatos import ManejadorBaseDatos

def main():
    print("Init")

    conexion_mysql = Mysql()

    procesar = ManejadorBaseDatos()
    usuario_mysql ={"nombre":"Juan"}

    procesar.procesar(conexion_mysql, usuario_mysql )

    conexion_mongo = Mongo()
    usuario_mongo={"nombre":"Pedro"}
    procesar.procesar(conexion_mongo, usuario_mongo )

if __name__ == "__main__":
    main()
