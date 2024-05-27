from figura import Figura
from cuadrado import Cuadrado
from rectangulo import Rectangulo

def main():
    print("Init")

    cuadrado_carlos= Cuadrado(5)
    print(f"Cuadrado area: {cuadrado_carlos.area()}")
  
    print(f"Cuadrado perimetrorea: {cuadrado_carlos.perimetro()}")

    rectangulo_carlos= Rectangulo(8, 5)
    print(f"rectangulo area: {rectangulo_carlos.area()}")

    
    print(f"rectangulo perimetro: {rectangulo_carlos.perimetro()}")



if __name__ == "__main__":
    main()
