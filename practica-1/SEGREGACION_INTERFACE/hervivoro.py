from abc import abstractmethod
from animal import AnimalInterface

class HervivoroInterface(AnimalInterface):
    @abstractmethod
    def pastar(self):
        pass

