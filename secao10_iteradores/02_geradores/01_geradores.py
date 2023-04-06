def funcao_geradora():
    while True: #Loop infinito
        palavra = input('Fale: ')
        yield palavra

resultado = funcao_geradora()
print(resultado)
#Ele irá gerar loops de acordo com a quantidade de next()
print(next(resultado))
print(next(resultado))
print(next(resultado))
