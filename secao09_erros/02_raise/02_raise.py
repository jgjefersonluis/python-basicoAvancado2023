def divisao(num1,num2):
    if num2 == 0:
        raise ZeroDivisionError('Numero 2 não pode ser zero, pois e denominador')
    divisao = num1/num2
    print(f'{divisao}')

divisao(1,2)
