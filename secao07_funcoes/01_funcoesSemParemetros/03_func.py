def teste_frase(): #Não há parametros de entrada
    print('Estou na funcao')

frase = teste_frase #Quando crio variaveis do tipo função, deve ser SEM PARENTESES
print(type(frase))
frase()
#Quando utiliza parenteses, chama a execução da função, sem parenteses apenas chama o objeto função.
