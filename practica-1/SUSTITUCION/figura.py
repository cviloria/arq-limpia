from abc import ABC, abstractmethod
class Figura(ABC):

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass

    def __str__(self):
        return "Figura: " + self.nombre
