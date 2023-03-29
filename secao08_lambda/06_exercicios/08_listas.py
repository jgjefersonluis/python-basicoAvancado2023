nomes = ['Maria Joaquina', 'Dom Pedro', 'Napoleão', 'Chaves', 'Jhennifer Lopez']
provaCorrida = [2, 7.5, 9, 8.67, 6.8]
provaEscalada = [1, 8, 4, 6.3, 9.1]
provaOperMatem = [0, 8.7, 5.8, 10, 4.3]

listaNotas = []

tabela = zip(provaCorrida, provaEscalada, provaOperMatem) #Agrupa as notas das 3 provas em uma
# tupla para cada participante
for notas in tabela:
    listaNotas.append(sum(notas)) #Soma as notas das 3 provas de cada participante e coloca na lista
# 'listaNotas'

tabelaFinal = zip(nomes, listaNotas) #Associa o nome de cada participante com sua
# respectiva nota final

dicioFinal = dict(tabelaFinal)

vencedor = ''
pontos = 0

for part, pts in dicioFinal.items():
    print(f'Participante: {part}. Pontos: {pts}')
    if pts > pontos: #Verificação de qual nota é maior
        pontos = pts
        vencedor = part

print(f'\n_____Vencedor: {vencedor} - Pontos: {pontos}_____')
