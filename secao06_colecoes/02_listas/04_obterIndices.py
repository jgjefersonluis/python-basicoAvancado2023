lista1 = []
lista2 = [1, 2, 3, 3, 4, 5, 8, 8, 10]
lista3 = [3.4, 23.42, 532.12]
lista4 = [True, False, True, True]
lista5 = ['tatu', 'roxo', 'a']
lista6 = list('Silvio Santos 1898')
lista7 = [43, True, 23.1, 'abacate', 'Russia', 12, 'x', False, [1, 3, 5, 7]]

# Obter indices da lista
jogos = ['Sonic', 'Super Mario', 'GTA', 'GoW', 'PES']
for indice, jogo in enumerate(jogos):
    print(indice, jogo)

print(lista2.index(2))

print(lista2.index(8))  # Primeiro 8 encontrado
# print(lista2.index(80)) #ValueError

print(lista2.index(5, 4))  # Busca A PARTIR do índice 4
# print(lista2.index(5, 20)) #ValueError

print(lista2.index(5, 3, 6))  # Busca ENTRE os índices 3 e 6
