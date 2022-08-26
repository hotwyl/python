# Receber um numero
# Receber um Operador
# Receber um outro numero
# Mostrar o resultado

print("Digite o primeiro numero")
numero1 = int(input())

print("Digite um operador")
operador = input()

print("Digite o segundo numero")
numero2 = int(input())

if operador == '+':
    resultado = numero1 + numero2
    print(resultado)
elif operador == '-':
    resultado = numero1 - numero2
    print(resultado)
elif operador == '*':
    resultado = numero1 * numero2
    print(resultado)
elif operador == '/':
    resultado = numero1 / numero2
    print(resultado)
else:
    print("Operador incorreto")