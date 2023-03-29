def apresentarNotas(**kwargs):
    print(kwargs)
    for aluno in kwargs:
        print(f'{aluno}: {kwargs[aluno]}')

notas = {'joao':7, 'carlos':10, 'jessica':9}
#apresentarNotas(notas) #TypeError
apresentarNotas(**notas)
#apresentarNotas()
