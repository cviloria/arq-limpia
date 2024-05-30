from basedatos import BaseDatos

class ManejadorBaseDatos:
    def procesar(self, bd: BaseDatos, datos:dict):
        bd.guardar(datos)
        bd.leer('SELECT * FROM usuarios')
        print("Procesando la información")
    