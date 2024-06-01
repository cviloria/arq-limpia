from carnivoro import CarnivoroInterface

class Perro(CarnivoroInterface): 
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        return "Guau guau"
    
    def respirar(self):
        return "Respirando desde el perro"
    
    def comer(self):
        return "Comiendo desde el perro"
    
    def dormir(self):
        return "Durmiendo desde el perro"
    
    def matar(self):
        return "El perro no mata solo como lo que le pone el amo"