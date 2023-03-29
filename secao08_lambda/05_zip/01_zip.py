alunos = ['Bianca', 'Vitor', 'Ariel']
notas = (10, 6, 8)

juntarTudo = zip(alunos, notas)
print(juntarTudo)
print(type(juntarTudo))

#print(list(juntarTudo))
print(dict(juntarTudo))
print(tuple(juntarTudo)) # Os valores se perdem após sua utilização
