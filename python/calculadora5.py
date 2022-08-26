# Calculadora Soma / Subitração / Divisão / Multiplicação

num1 = float(input("Digite o Primeiro Valor: "))
num2 = float(input("Digite o Segundo Valor: "))

print("Qual operação você deseja fazer?")
print("\t 1 - Soma")
print("\t 2 - Subitração")
print("\t 3 - Divisão")
print("\t 4 - Multiplicação")

op = input("Digite um valor entre (1-4): ")

if(op == "1"):
    print( num1, ' + ', num2, ' = ', num1 + num2)
elif(op == "2"):
    print( num1, ' - ', num2, ' = ', num1 - num2)
elif(op == "3"):
    print( num1, ' / ', num2, ' = ', num1 / num2)
elif(op == "4"):
    print( num1, ' * ', num2, ' = ', num1 * num2)
else:
    print("Você escolheu uma opção inválida. Tente novamente!")