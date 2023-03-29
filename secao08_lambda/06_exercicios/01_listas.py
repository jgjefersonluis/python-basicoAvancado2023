lista1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
lista2 = [160, 11, 50, 22, 43, 24, -12, 24, 542, 217]
lista3 = []

lista2.reverse() #Inverte os valores da lista2
soma = lambda lista1, lista2: [lista1[ind] + lista2[ind] for ind in range(0, 10)] #Soma os elementos
#correspondentes das listas. Ex: Elemento 0 (10) + Elemento 0 (217) ...
result = soma(lista1, lista2)
lista3.append(result)
print(lista3)