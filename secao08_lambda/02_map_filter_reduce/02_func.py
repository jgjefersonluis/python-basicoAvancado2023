nascimento = lambda dado: f'Ano de nascimento: {dado[0] - dado[1]}'

dados = [(1998, 22), (1815, 88), (2027, 3)]

print(list(map(nascimento, dados)))
