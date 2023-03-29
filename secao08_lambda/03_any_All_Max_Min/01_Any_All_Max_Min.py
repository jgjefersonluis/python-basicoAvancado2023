print(any([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) #True
print(any('Programando Ideias')) #True
print(any([0, False, {}, [], ()])) #False
print(any([0, False, {}, [], (), 89437])) #True
print(any([])) #False

numeros = [1, 2, 3, 4, 5, 6]
print(list(num % 5 == 0 for num in numeros))
print(any(num % 5 == 0 for num in numeros))
