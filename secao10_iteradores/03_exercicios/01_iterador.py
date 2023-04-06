def desmembra_iteravel(iteravel): #Função que realiza a operação for
    iterador = iter(iteravel) #Transforma iteravel em iterador
    while True: #Loop infinito
        try:
            print(next(iterador)) #Imprime cada dado desmembrado do
                                  #iterador
        except StopIteration: #Caso chegue ao final do iterador faça:
            print('Chegamos ao ultimo elemento') #Aviso
            break #Quebra o loop infinito

desmembra_iteravel([1,2,3,4,5,6,7,8]) #Chamada de função com iterável
