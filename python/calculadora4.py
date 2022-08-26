print('==========Calculadora==========')
print('===============================')
print('[1] Para Somar')
print('[2] Para Subtrair')
print('[3] Para Dividir')
print('[4] Para Multiplicar')
print('===============================')
D = int (input('O que você deseja fazer? '))

if D == 1 :
    n1 = int (input('Digite o primeiro número: '))
    n2 = int (input('Digite o segundo número: '))
    print('Resultado: ', n1, ' + ', n2, ' = ', n1 + n2)
elif D == 2 :
    n1 = int (input('Digite o primeiro número: '))
    n2 = int (input('Digite o segundo número: '))
    print('Resultado: ', n1, ' - ', n2, ' = ', n1 - n2)
elif D == 3 :
    n1 = int (input('Digite o primeiro número: '))
    n2 = int (input('Digite o segundo número: '))
    print('Resultado: ', n1, ' / ', n2, ' = ', n1 / n2)
elif D == 4 :
    n1 = int (input('Digite o primeiro número: '))
    n2 = int (input('Digite o segundo número: '))
    print('Resultado: ', n1, ' * ', n2, ' = ', n1 * n2)
else:
    print("Opção inválida.")