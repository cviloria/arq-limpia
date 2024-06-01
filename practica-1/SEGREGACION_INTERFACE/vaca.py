from hervivoro import HervivoroInterface

class Vaca(HervivoroInterface):
    def __init__(self, nombre):
        self.nombre = nombre


    def comer(self):
        print("Vaca comiendo pasto")

    def respirar(self):
        print("Vaca respirando")
    
    def dormir(self):
        print("Vaca duerme en el pasto")

    def pastar(self):
        print("Vaca pastando")

