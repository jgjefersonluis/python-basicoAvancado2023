numeroInt = 1
listaNumeros = []

while numeroInt != 0:
    numeroInt = int(input('Digite um número inteiro: '))
    if numeroInt != 0:
        listaNumeros.append(numeroInt)

ordenada = sorted(listaNumeros) #Ordena a lista 'listaNumeros'
tamanho = len(listaNumeros) #Obtém o tamanho da lista 'listaNumeros'

print(f'Maior valor: {ordenada[tamanho - 1]}') #O -1 é porque o len retorna a quantidade
# de elementos da lista, ou seja, começando do 1 até o ultimo elemento. Mas os índices começam do 0,
# então, o último é o tamanho da lista - 1.

invertida = reversed(ordenada) #Inverte a lista
listaInvertida = list(invertida)

if tamanho % 2 == 1:
    print(f'Valor intermediário: {listaInvertida[tamanho // 2]}')
else:
    print(f'Valor intermediário: '
          f'{(listaInvertida[tamanho // 2] + listaInvertida[(tamanho // 2) - 1]) / 2}')
