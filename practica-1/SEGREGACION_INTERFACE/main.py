
from perro import Perro
from vaca import Vaca

def main():
    print("Init")

  
    perro = Perro('Firulais')

    print(f"El perro {perro.nombre} dice: {perro.ladrar()}")
    print(perro.respirar())
    print(perro.dormir())
    print(perro.comer())

    vaca = Vaca('Lola')

    vaca.respirar()
    vaca.pastar()
    vaca.dormir()

   
if __name__ == "__main__":
    main()