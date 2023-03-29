# Exemplos de filter
import math
numeros = [1, 4, 1, 3, 5, 6, 3, 2, 9, 7, 4, 6, 9]
result = filter(lambda num: num > math.pi, numeros)

print(result) #Retorna um filter object
print(type(result))

print(list(result)) #Os valores se perdem após sua utilização
print(list(result))

'''
def qualquer(*args):
    for num in args:
        if num > math.pi:
            return True
        else:
            return False
'''

# Filter com map
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#POR PARTES:
#filter(lambda num: num % 2 == 0, numeros)

#map(lambda n: n ** 2, filter(lambda num: num % 2 == 0, numeros))

result = list(map(lambda n: n ** 2, filter(lambda num: num % 2 == 0, numeros)))
print(result)
