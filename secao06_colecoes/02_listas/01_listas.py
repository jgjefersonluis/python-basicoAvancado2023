# Exemplos de declaração de listas:
lista1 = []
lista2 = [1, 2, 3, 3, 4, 5, 8, 8, 10]
lista3 = [3.4, 23.42, 532.12]
lista4 = [True, False, True, True]
lista5 = ['tatu', 'roxo', 'a']
lista6 = list('Silvio Santos 1898')
lista7 = [43, True, 23.1, 'abacate', 'Russia', 12, 'x', False, [1, 3, 5, 7]]

# Obs.: Listas são ordenadas, ou seja, seus índices são importantes.

listaNova = []
for numero in range(1, 11):
    listaNova.append(numero)

print(listaNova)

listaNova2 = list(range(1, 11))
print(listaNova2)

