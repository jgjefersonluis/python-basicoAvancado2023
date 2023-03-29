from functools import reduce

numeros = [2, 1, 2, 3]

result = reduce(lambda x, y: x ** y, numeros)
print(result)
