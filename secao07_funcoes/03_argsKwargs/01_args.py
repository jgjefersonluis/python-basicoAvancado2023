def cadastro(nome, idade, *args):
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    print(args)
    print(f'Profissão: ', end=' ')
    for prof in args:
        print(prof, end=' ')

cadastro('Agnaldo', 87, 'carpinteiro', 'lutador', 'garçom')
