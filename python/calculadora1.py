class calculadora1:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def somar(self):
        return self.a+self.b
    def subtrair(self):
        return self.a-self.b
    def multiplicar(self):
        return self.a*self.b
    def dividir(self):
        return self.a/self.b

    c = calculadora1(5,7)
    print(c.somar()) #12
    print(c.subtrair()) #-2
    print(c.multiplicar()) #0.qqr coisa
    print(c.dividir()) # 35