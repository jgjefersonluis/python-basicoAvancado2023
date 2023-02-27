soma = 0 # Inicializa variavel soma
numero = int(input('Digite o numero: ')) #Pede o numero para o usuario
for num in range(1,numero+1): #Para cada num dentro do intervalo 1 e numero+1 faça:
    if numero % num == 0: #Se o resto da divisão de numero por num for zero faça:
        soma = soma + num #atualiza soma com num
print(soma) #Imprime a soma final
