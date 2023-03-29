def apresentarNotas(joao, carlos, jessica):
    print(f'Joao: {joao}, Carlos: {carlos}, Jessica: {jessica}')

notas = {'joao': 7, 'carlos': 10, 'jessica': 9}
#notas = {'joao': 7, 'carlos': 10, 'jessic': 9} #TypeError
apresentarNotas(**notas)

