anterior = 0 #Numero antecessor da sequencia
proximo = 1 #Numero posterior da sequencia
parada = 1 #Variavel de parada para impressao dos 5 numeros
soma = 0 #Variavel que armazena a soma para realizar a média
while parada <= 5: #Enquanto parada for menor ou igual a 5 faça:
    proximo = proximo + anterior #Proximo recebe ele mesmo e anterior para atualizar o numero posterior
    anterior = proximo - anterior #Anterior recebe proximo menos anterior para atualizar
    divisor = 1 #Variavel que será o divisor
    num_divisores_inteiros = 0 #Contagem de numero de divisores
    while divisor <= proximo: #Loop para realizar as divisões de proximo por todos os divisores começando de 1 até proximo
        if proximo % divisor == 0: #Caso a divisão tenha resto zero
            num_divisores_inteiros += 1 #incrementa o contador de divisores
        divisor += 1 #Incrementa divisor para realizar outro loop
    if num_divisores_inteiros == 2: #Caso tenha apenas dois divisores, é um numero primo
        soma = soma + proximo #Atualiza soma com o numero primo proximo
        print(proximo) #Apenas imprime o numero primo para verificação
        parada += 1 #Incrementa a variavel parada para achar o proximo numero primo

print(soma/5) #Imprime a media
