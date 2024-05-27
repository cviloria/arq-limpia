from mysql import Mysql
from manejadorbasedatos import ManejadorBaseDatos

def main():
    print("Init")

    conexion = Mysql('localhost')

    procesar = ManejadorBaseDatos(conexion)

    procesar.procesar()
if __name__ == "__main__":
    main()
