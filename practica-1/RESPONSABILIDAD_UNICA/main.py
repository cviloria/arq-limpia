from calculadora import Calculadora
def main():
    calculadora = Calculadora("Calculadora Carlos")
    
    calculadora.suma(25,27)

    calculadora.dividir(70,20)

    calculadora.multiplicar(1225, 200)

    calculadora.restar(430, -80)

    print(f"Mi calculadora es {calculadora.nombre()}")

if __name__ == "__main__":
    main()