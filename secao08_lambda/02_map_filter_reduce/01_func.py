def maiorq10(num):
    if num > 10:
        print('Maior')
    else:
        print('Menor')

#maiorq10(27)
#maiorq10(8)

numeros = [4, 6, 5, 91, 8, 7, 14, 16, 98, 4, 1.3, 75.4, 3]

result = map(maiorq10, numeros)
print(result) #Retorna um map object
print(type(result))

print(list(result))
#print(list(result)) #Os valores se perdem após sua utilização
