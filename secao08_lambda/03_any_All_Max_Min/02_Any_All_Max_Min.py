print(all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) #True
print(all('Programando Ideias')) #True
print(all([0, False, {}, [], ()])) #False
print(all([0, False, {}, [], (), 89437])) #False
print(all([])) #True

numeros = [2, 4, 6, 8, 10, 11]
print(list(num % 2 == 0 for num in numeros))
print(all(num % 2 == 0 for num in numeros))

