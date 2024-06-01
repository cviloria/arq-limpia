class Calculadora:
    def __init__(self,title:str):
        self.title = title 

    def nombre(self):
        return self.title

    def suma(self, a:int, b:int) -> int:
        result = a + b
        print(f"Resultado de la suma es= {result}")
    
    def restar(self, a:int, b:int) -> int:
        result = a - b
        print(f"Resultado de la resta es= {result}")
    
    def multiplicar(self, a:int, b:int) ->int:
        result = a * b
        print(f"Resultado de la multiplicacion es= {result}")
    
    def dividir(self, a:int, b:int) ->float:
        result = a / b 
        print(f"Resultado de la division es= {result}")