numero = int(input('Digite o numero de multiplos de 5 que deseja: ')) #Recebe numero como inteiro para entrar no range()
for num in range(1,numero+1): #Para cada num no intervalo de 1 a numero+1 faça:
    print(f'{5 * num}') #Imprime 5 vezes num
