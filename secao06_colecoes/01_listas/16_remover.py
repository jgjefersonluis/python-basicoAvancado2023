# declaração de 01_listas:
lista1 = []
lista2 = [1, 2, 3, 3, 4, 5, 8, 8, 10]
lista3 = [3.4, 23.42, 532.12]
lista4 = [True, False, True, True]
lista5 = ['tatu', 'roxo', 'a']
lista6 = list('Silvio Santos 1898')
lista7 = [43, True, 23.1, 'abacate', 'Russia', 12, 'x', False, [1, 3, 5, 7]]

cor = 'azul'
animal = 'pavão'
numero = 42
lista8 = [cor, animal, numero]


# Remover elementos de uma lista - Pop: Remove e retorna o ultimo elemento de uma lista (padrão)
print(lista2)
print(lista2.pop())
print(lista2)

# Obs.: É possível indicar o índice do valor a ser removido
print(lista7)
lista7.pop(5)
print(lista7)
