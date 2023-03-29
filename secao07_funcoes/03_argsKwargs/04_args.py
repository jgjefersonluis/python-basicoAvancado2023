def idades(**kwargs):
    print(kwargs)
    for nome, idade in kwargs.items():
        print(f'A idade de {nome} é {idade}')

idades(maria=5, isadora=20, pedro=14)
