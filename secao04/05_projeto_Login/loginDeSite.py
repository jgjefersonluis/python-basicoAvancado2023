login = False
print('Bem vindo(a) ao cadastro do site!')
user = input('Crie seu nome de usuário: ')
senha = input('Crie sua senha: ')

print('\n___________LOGIN_____________')
if input('Usuário: ') == user and input('senha: ') == senha:
    login = True

if login:
    print(f'\nBem vindo(a) {user}')
else:
    print('\nTente novamente!')
