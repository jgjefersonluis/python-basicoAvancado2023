def operacao():
    contador = 60 #Isso é uma variavel local ou global?? Local
    contador += 2
    print(f'Contador = {contador}')

print(operacao()) #Quando não há return dentro da função retorna None
