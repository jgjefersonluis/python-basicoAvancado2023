# Exemplos de generators

#Exemplo 1
numeros = list(range(1, 11))
maiores = (numero for numero in numeros if numero > 5)
print(type(maiores))
print(maiores)
for i in maiores:
    print(i, end=' ')

for i in maiores:
    print(i, end=' ')

# Obs.: O objeto generator é perdido após sua iteração
