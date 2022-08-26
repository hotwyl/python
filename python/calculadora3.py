# Receber um numero
# Receber um Operador
# Receber um outro numero
# Mostrar o resultado

import operator

dict_operadores ={
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

print("Digite o primeiro numero")
numero1 = int(input())

print("Digite um operador")
operador = input()

print("Digite o segundo numero")
numero2 = int(input())

print(dict_operadores[operador](numero1,numero2))