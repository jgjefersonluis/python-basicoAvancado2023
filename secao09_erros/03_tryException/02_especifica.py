try:
    operacao = int(input('Escolha a operacao de acordo com o numero: \n 1 - Soma \n 2 - Subtracao \n 3 - Multiplicacao \n 4 - Divisao \n Opcao:'))
except TypeError:
    print('Deu TypeError')
except ValueError:
    print('Deu ValueError')
except: #Deve sempre finalizar como um default
    print('Nao sei qual erro deu')
