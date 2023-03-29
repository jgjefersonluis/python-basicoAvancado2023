#Map
listaAmostras = [(62, 1.73), (90, 1.86), (76, 2.12), (54, 1.56), (69, 1.76), (112, 1.63), (98, 1.59)]

def calculoIMC(amostra):
    imc = amostra[0] / (amostra[1] ** 2)
    return imc #Retorna o valor do imc calculado

imc = map(calculoIMC, listaAmostras)

resultadoIMC = list(imc)
resultIMC = []

for num in resultadoIMC:
    resultIMC.append(round(num)) #Arredonda os valores da lista 'resultadoIMC' e adiciona cada um
# na lista 'resultIMC'.

print(resultIMC)

#Filter
#IMC > 25 -> Sobrepeso
sobrepeso = filter(lambda imc: imc > 25, resultIMC) #Testa se os valores da lista 'resultIMC' são
#maiores do que 25
print(f'IMCs acima do peso: {list(sobrepeso)}')
