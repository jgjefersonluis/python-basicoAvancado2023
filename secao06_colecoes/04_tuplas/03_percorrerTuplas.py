tupla1 = (1, 2, 3, 4, 5)
tupla2 = 1, 2, 3, 4, 5
tupla3 = 1,
tupla4 = (1,)
tupla5 = ('futebol', 'moto', 'França')
tupla6 = ('pizza', True, 18, 5j, 0.43, 'x', True)
tupla7 = tuple(range(11))
tupla8 = tuple(['azul', True, 'x', 10, 12.1, 'correio', [1, 2, 3], (1, 2, 3)])

# Percorer tuplas (iterar)
# For

for elemento in tupla1:
    print(elemento, end=' ')

total = 0
for elemento in tupla1:
    total = total + elemento
print(f'\n{total/len(tupla1)}')

# While

total = 0
cont = 0
while cont < len(tupla1):
    total += tupla1[cont] #total = total + tupla1[cont]
    cont += 1 #cont = cont + 1
print(total/cont)

