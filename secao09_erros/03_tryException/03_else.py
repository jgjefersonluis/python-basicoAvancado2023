try:
    operacao = int(input('Escolha a operacao de acordo com o numero: \n 1 - Soma \n 2 - Subtracao \n 3 - Multiplicacao \n 4 - Divisao \n Opcao:'))
except ValueError:
    print('Deu ValueError')
else:
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))

    if operacao == 1:
        print(f'Resultado: {soma(num1,num2)}')
    elif operacao == 2:
        print(f'Resultado: {subtracao(num1, num2)}')
    elif operacao == 3:
        print(f'Resultado: {mul(num1, num2)}')
    elif operacao == 4:
        print(f'Resultado: {divisao(num1, num2)}')
        