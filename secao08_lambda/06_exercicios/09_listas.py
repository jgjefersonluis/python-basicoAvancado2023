companhias = ['GOL', 'LATAM', 'Azul']
voo1 = [115, 95, 110]
voo2 = [195, 80, 225]

voos1e2 = zip(voo1, voo2) #Junta os numeros de passageiros de cada companhia
maxPass = map(lambda voos: max(voos), voos1e2) #Determina o valor max de passageiros por companhia
# entre os voos 1 e 2
listamaxPass = list(maxPass)

compMax = zip(companhias, listamaxPass)
listacompMax = list(compMax)

umaEst = list(filter(lambda valMax: valMax[1] < 100, listacompMax)) #Filtra a companhia aérea que tem
# menos de 100 passageiros em seu valor máximo e depois converte o resultado para uma lista.
duasEst = list(filter(lambda valMax: valMax[1] > 100 and valMax[1] <= 200, listacompMax))
tresEst = list(filter(lambda valMax: valMax[1] > 200 and valMax[1] <= 300, listacompMax))

print(f'Uma estrela: {umaEst[0][0]} - Max Passageiros: {umaEst[0][1]}')
print(f'Duas estrelas: {duasEst[0][0]} - Max Passageiros: {duasEst[0][1]}')
print(f'Tres estrela: {tresEst[0][0]} - Max Passageiros: {tresEst[0][1]}')
