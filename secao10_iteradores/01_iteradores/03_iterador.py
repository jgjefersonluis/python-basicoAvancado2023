iteravel = [1,2,3,4,5,6,7,8,9,10]
iterador = iter(iteravel)

while True: #Loop infinito
    try:
        elemento = next(iterador) #Elemento recebe cada caracter de iterável que foi transformada em iterador
        print(elemento)
    except StopIteration:
        break #Parar o loop infinito

print('------------------------------------')
#O modo acima é equivalente a:
iteravel = [1,2,3,4,5,6,7,8,9,10]

for elemento in iteravel:
    print(elemento)
