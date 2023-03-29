
#Utilizando loop for
n = int(input('Fatorial de: '))
fat = 1

for i in range(1, n+1): #O range deve começar em 1, pois se houvesse uma multiplicação por 0, o
#resultado seria 0. E deve terminar em n+1 para o valor de n ser incluído na multiplicação.
    fat *= i #Multiplica todos os termos do range

print(f'Fatorial loop for: {fat}')
'''
Ex.: n = 4
range(1, 5) = 1, 2, 3, 4
(1) fat = fat * 1 = 1
(2) fat = fat * 2 = 2
(3) fat = fat * 3 = 6
(4) fat = fat * 4 = 24
'''

#Utilizando reduce
from functools import reduce #Importando a função reduce()

lista = [1] #Colcoando o valor 1 como primeiro elemento da lista, para não haver
# problema caso o usuário escolha n == 0.

lista.extend(range(1, n+1))

fat = reduce(lambda x, y: x * y, lista)
print(f'Fatorial reduce: {fat}')
