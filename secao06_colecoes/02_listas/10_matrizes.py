lista1 = []
lista2 = [1, 2, 3, 3, 4, 5, 8, 8, 10]
lista3 = [3.4, 23.42, 532.12]
lista4 = [True, False, True, True]
lista5 = ['tatu', 'roxo', 'a']
lista6 = list('Silvio Santos 1898')
lista7 = [43, True, 23.1, 'abacate', 'Russia', 12, 'x', False, [1, 3, 5, 7]]

# Matrizes

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #Matriz 3x3

# Obs.: Cada lista interna é uma linha da matriz

#print(matriz[0])
#print(matriz[1])
#print(matriz[2])

#for linha in matriz:
#    print(linha)

#print(matriz[0][2]) #3
#print(matriz[2][2]) #9
#print(matriz[1][0]) #4

#for linha in matriz:
#    for numero in linha:
#        print(numero)

# Jogo de Velha com matriz

matriz = [[' ', ' ', ' '], [' ', 'O', 'X'], [' ', ' ', ' ']] #Matriz 3x3

print(matriz[0])
print(matriz[1])
print(matriz[2])

LP1 = int(input('Escolha a linha: '))
CP1 = int(input('Escolha a coluna: '))
matriz[LP1][CP1] = 'X'

LP2 = int(input('Escolha a linha: '))
CP2 = int(input('Escolha a coluna: '))
matriz[LP2][CP2] = 'O'

for linha in matriz:
    print(linha)
