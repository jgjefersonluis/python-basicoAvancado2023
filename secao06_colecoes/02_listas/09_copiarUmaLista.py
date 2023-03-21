lista1 = []
lista2 = [1, 2, 3, 3, 4, 5, 8, 8, 10]
lista3 = [3.4, 23.42, 532.12]
lista4 = [True, False, True, True]
lista5 = ['tatu', 'roxo', 'a']
lista6 = list('Silvio Santos 1898')
lista7 = [43, True, 23.1, 'abacate', 'Russia', 12, 'x', False, [1, 3, 5, 7]]

# Copiar uma lista - Deep Copy
print(lista2)
lista1 = lista2.copy()
print(lista1)

lista1.append(11)
print(lista2)
print(lista1)


# Obs.: A deep copy copia as listas e as torna independentes entre si, ou seja,
# quaqluer modificação em uma NÃO afeta a outra.

# Copiar uma lista - Shallow Copy
print(lista2)
lista1 = lista2
print(lista1)

lista1.append(11)
print(lista2)
print(lista1)

# Obs.: A shallow copy copia as listas e as conecta, ou seja,
# qualquer modificação em uma AFETA a outra.