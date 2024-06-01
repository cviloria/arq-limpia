from abc import abstractmethod
from animal import AnimalInterface

class CarnivoroInterface(AnimalInterface):
    @abstractmethod
    def matar(self):
        pass