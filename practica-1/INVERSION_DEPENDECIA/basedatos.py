from abc import  abstractmethod
class BaseDatos:

    @abstractmethod
    def guardar(self,dato):
        pass

    @abstractmethod
    def leer(self,query):
        pass