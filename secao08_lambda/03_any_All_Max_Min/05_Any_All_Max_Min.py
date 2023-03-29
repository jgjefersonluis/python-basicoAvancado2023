alunos = ['Pedro', 'Isadora', 'Lucas', 'Camila', 'Samuel']
print(max(alunos)) #Samuel
print(min(alunos)) #Camila

print(max(alunos, key=lambda aluno: len(aluno))) #Isadora
print(min(alunos, key=lambda aluno: len(aluno))) #Pedro
