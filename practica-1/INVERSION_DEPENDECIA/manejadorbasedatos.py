from basedatos import BaseDatos

class ManejadorBaseDatos:
    def procesar(self, bd: BaseDatos):
        bd.guardar("Guardando información")
        datos = bd.leer()
        print("Procesando la información", datos)
    