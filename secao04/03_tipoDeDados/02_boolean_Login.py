login = False
senha = 'bol'

key = input('Digite sua senha: ')

if key == senha:
    login = True
else:
    print('Senha incorreta!')

if login == True:
    print('Bem-vindo admin!')
else:
    print('Tente novamente!')
