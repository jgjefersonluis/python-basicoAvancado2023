try:
    operacao = int(input(
        'Escolha a operacao de acordo com o numero: \n 1 - Soma \n 2 - Subtracao \n 3 - Multiplicacao \n 4 - Divisao \n Opcao:'))
except ValueError:
    print('Deu ValueError')
else:
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))

    if operacao == 1:
        print(f'Resultado: {soma(num1, num2)}')
    elif operacao == 2:
        print(f'Resultado: {subtracao(num1, num2)}')
    elif operacao == 3:
        print(f'Resultado: {mul(num1, num2)}')
    elif operacao == 4:
        print(f'Resultado: {divisao(num1, num2)}')
finally:
    print('terminou o processo')

def soma(x, y):
    op = x + y
    return op


def subtracao(x, y):
    op = x - y
    return op


def mul(x, y):
    op = x * y
    return op


def divisao(x, y):
    try:
        op = x / y
    except ZeroDivisionError:
        print('O denominador nao pode ser zero')
        return 'Infinito'
    else:
        return op


try:
    operacao = int(input(
        'Escolha a operacao de acordo com o numero: \n 1 - Soma \n 2 - Subtracao \n 3 - Multiplicacao \n 4 - Divisao \n Opcao:'))
except ValueError:
    print('Deu ValueError')
else:
    try:
        num1 = int(input('Digite o primeiro numero: '))
    except ValueError:
        print('Deve ser um numero inteiro')
    else:
        try:
            num2 = int(input('Digite o segundo numero: '))
        except ValueError:
            print('Digite um numero inteiro')
        else:
            if operacao == 1:
                print(f'Resultado: {soma(num1, num2)}')
            elif operacao == 2:
                print(f'Resultado: {subtracao(num1, num2)}')
            elif operacao == 3:
                print(f'Resultado: {mul(num1, num2)}')
            elif operacao == 4:
                print(f'Resultado: {divisao(num1, num2)}')
finally:
    print('Terminou o processo')
