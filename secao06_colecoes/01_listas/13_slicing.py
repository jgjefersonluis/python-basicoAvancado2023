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

print(lista7[::-1]) #slicing

# Obs.: lista[inicio:fim:passo]
print(lista7)
print(lista7[2:]) #Do índice 2 ao final
print(lista7[2:6]) #Do indice 2 ao 6
print(lista7[2:7:2]) #Do indice 2 ao 7, de dois em dois elementos

# Acessar elementos de uma lista
print(lista7[2])
print(lista7[4])
print(lista7[-2])
print(lista7[-4])
print(lista7[5])

#print(lista7[15]) #IndexError
#print(lista7[-15]) #IndexError