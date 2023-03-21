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

# Adicionar valores em uma lista - Extend: Adiciona multiplos elementos
lista5.extend(['abacaxi', 1.98, 'Kg'])
print(lista5)

#lista5.extend(12) #TypeError

#lista5.extend([1, True], [0, False]) #TypeError