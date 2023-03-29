listaSF = []
stop = 0

def fibonacci(stop, a, b, aux): #1, 1, 2, 3, 5, 8, 13, 21, 34...
    global listaSF #Utiliza uma variável global dentro de uma função
    listaSF.append(a) #Adiciona os valores na lista 'listaSF'
    a, b = b, a + b #Acumula os valores para determinar os proximos numeros da sequencia.
#Essa é a logica da sequencia de fibonacci, o proximo termo é sempre a soma dos dois
# termos anteriores
    aux += 1
    if stop == aux:
        print(listaSF)
        return 0
    else:
        return fibonacci(stop, a, b, aux) #Chama a própra função até que stop == aux.

while stop < 1:
    stop = int(input('Digite a quantidade de termos: '))

fibonacci(stop, a=1, b=1, aux=0)
